import './styles/base.css';
import './styles/netexam.css';
import './styles/apple-theme.css';
import katex from 'katex';
import confetti from 'canvas-confetti';
import quizData from './data/quizzes.json';
import { generateGeminiMasterPrompt } from './utils/promptGenerator.js';

// Application State
const state = {
  view: 'dashboard', // 'dashboard' | 'quiz' | 'review'
  currentModuleId: 'PAS',
  activeQuestionIndex: 0,
  hardestOnly: false,
  shuffle: false,
  theme: localStorage.getItem('netexam_theme') || 'netexam', // 'netexam' | 'apple'
  learningMode: true, // show answers on demand
  timerSeconds: 7200, // 2 hours
  timerInterval: null,
  // User answers per module: { [moduleId]: { [qId]: { answers: {}, flagged: false, checked: false } } }
  userResponses: {},
  submittedModules: {}
};

// Initialize responses storage
Object.keys(quizData).forEach(mId => {
  state.userResponses[mId] = {};
  quizData[mId].questions.forEach(q => {
    state.userResponses[mId][q.id] = {
      answers: {},
      flagged: false,
      checked: false
    };
  });
});

// DOM Mount
const app = document.getElementById('app');

function applyTheme(theme) {
  state.theme = theme;
  localStorage.setItem('netexam_theme', theme);
  document.body.className = `theme-${theme}`;
}

// Show Toast Notification
function showToast(message, icon = '📋') {
  let container = document.querySelector('.toast-container');
  if (!container) {
    container = document.createElement('div');
    container.className = 'toast-container';
    document.body.appendChild(container);
  }

  const toast = document.createElement('div');
  toast.className = 'toast toast-success';
  toast.innerHTML = `<span class="toast-icon">${icon}</span> <span>${message}</span>`;
  container.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateY(10px)';
    toast.style.transition = 'all 0.25s ease-out';
    setTimeout(() => toast.remove(), 250);
  }, 3200);
}

// LaTeX Renderer Helper using KaTeX
function renderLatex(text) {
  if (!text) return '';
  
  // Replace block math $$...$$
  let formatted = text.replace(/\$\$([\s\S]*?)\$\$/g, (match, formula) => {
    try {
      return katex.renderToString(formula.trim(), { displayMode: true, throwOnError: false });
    } catch (e) {
      return match;
    }
  });

  // Replace inline math $...$
  formatted = formatted.replace(/\$([^\$\n]+?)\$/g, (match, formula) => {
    try {
      return katex.renderToString(formula.trim(), { displayMode: false, throwOnError: false });
    } catch (e) {
      return match;
    }
  });

  return formatted;
}

// Filter or Shuffle Questions for Current Module
function getActiveQuestions() {
  const mod = quizData[state.currentModuleId];
  if (!mod) return [];

  let list = [...mod.questions];

  if (state.hardestOnly) {
    // Priority order: Expert > Hard > Medium > Easy
    const rank = { 'Expert': 4, 'Hard': 3, 'Medium': 2, 'Easy': 1 };
    list.sort((a, b) => (rank[b.difficulty] || 0) - (rank[a.difficulty] || 0));
    list = list.slice(0, 20); // Top 20 hardest
  }

  if (state.shuffle) {
    // Deterministic shuffle or randomized
    list = [...list].sort(() => 0.5 - Math.random());
  }

  return list;
}

// Start Timer
function startTimer() {
  clearInterval(state.timerInterval);
  state.timerInterval = setInterval(() => {
    if (state.timerSeconds > 0) {
      state.timerSeconds--;
      updateTimerDisplay();
    } else {
      clearInterval(state.timerInterval);
      submitExam();
    }
  }, 1000);
}

function updateTimerDisplay() {
  const el = document.getElementById('timerDigits');
  if (!el) return;
  const hours = Math.floor(state.timerSeconds / 3600);
  const minutes = Math.floor((state.timerSeconds % 3600) / 60);
  const seconds = state.timerSeconds % 60;
  
  const formatted = `${hours}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
  el.textContent = formatted;

  const box = el.closest('.netexam-timer-box');
  if (box) {
    if (state.timerSeconds < 300) {
      box.classList.add('warning');
    } else {
      box.classList.remove('warning');
    }
  }
}

// Copy Gemini Master Prompt
function handleCopyPrompt(q) {
  const mod = quizData[state.currentModuleId];
  const prompt = generateGeminiMasterPrompt(q, mod);

  navigator.clipboard.writeText(prompt).then(() => {
    showToast('Gemini Master Prompt copied! Paste into gemini.com for zero-knowledge, full theory explanation.', '✨');
  }).catch(() => {
    // Fallback if clipboard API restricted
    const textarea = document.createElement('textarea');
    textarea.value = prompt;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    textarea.remove();
    showToast('Gemini Master Prompt copied to clipboard!', '✨');
  });
}

// Open Prompt Preview Modal
function openPromptModal(q) {
  const mod = quizData[state.currentModuleId];
  const prompt = generateGeminiMasterPrompt(q, mod);

  const modal = document.createElement('div');
  modal.className = 'modal-overlay';
  modal.innerHTML = `
    <div class="modal-card">
      <div class="modal-header">
        <h3>✨ Gemini Theory Master Prompt (${q.topic})</h3>
        <button class="modal-close" id="closePromptModal" style="font-size: 20px; color: #64748b;">✕</button>
      </div>
      <div class="modal-body">
        <p style="margin-bottom: 12px; font-weight: 600; color: #2563eb;">
          This prompt is pre-configured for zero-knowledge learners, using everyday real-world analogies (strictly NO gaming analogies), LaTeX formulas, and complete theoretical coverage of the entire lecture:
        </p>
        <pre style="background: #0f172a; color: #f8fafc; padding: 16px; border-radius: 8px; font-size: 12.5px; white-space: pre-wrap; word-break: break-word; max-height: 400px; overflow-y: auto;">${prompt.replace(/</g, '&lt;').replace(/>/g, '&gt;')}</pre>
      </div>
      <div class="modal-footer">
        <button class="netexam-btn-solution" id="copyFromModalBtn">📋 Copy to Clipboard</button>
        <button class="netexam-btn-nav" id="closeFromModalBtn">Done</button>
      </div>
    </div>
  `;
  document.body.appendChild(modal);

  modal.querySelector('#closePromptModal').onclick = () => modal.remove();
  modal.querySelector('#closeFromModalBtn').onclick = () => modal.remove();
  modal.querySelector('#copyFromModalBtn').onclick = () => {
    navigator.clipboard.writeText(prompt).then(() => {
      showToast('Master prompt copied to clipboard!', '✨');
      modal.remove();
    });
  };
}

// Render Dashboard View
function renderDashboard() {
  const modules = Object.values(quizData);

  app.innerHTML = `
    <header class="netexam-header">
      <div class="netexam-brand">
        <div class="netexam-logo-text">
          <div class="netexam-logo-main">
            SLIIT <span class="netexam-badge-uni">UNI</span> NetExam
          </div>
          <div class="netexam-logo-sub">Online Examination Platform</div>
        </div>
        <nav class="netexam-nav-links">
          <a href="#" class="netexam-nav-link active">Dashboard</a>
          <a href="#" class="netexam-nav-link" id="navExamLink">Examinations</a>
          <a href="#" class="netexam-nav-link">Lockdown Browser</a>
          <a href="#" class="netexam-nav-link">Practice Test</a>
        </nav>
      </div>
      <div class="netexam-user-area">
        <div class="netexam-user-badge">
          <div class="netexam-user-avatar">RD</div>
          <div class="netexam-user-name">IT22117182 ROOPASINGHE M.D.</div>
        </div>
        <button class="hardest-toggle-chip" id="themeToggleBtn" title="Switch Theme">
          ${state.theme === 'netexam' ? '🖥️ NetExam Lab' : '🍎 Apple Clean'}
        </button>
      </div>
    </header>

    <main>
      <section class="dashboard-hero">
        <div class="hero-pill">Year 2 Semester 1 • Final Examination Past Papers Simulator</div>
        <h1>SLIIT NetExam <span>Interactive Simulator</span></h1>
        <p>
          Master your examinations with exact NetExam computer-based questions, past paper model sets, 
          LaTeX equation rendering, a one-click <strong>Ask Gemini</strong> master prompt generator for zero-knowledge theory mastery, 
          and the <strong>Top 20 Hardest Questions</strong> quick-prep filter.
        </p>

        <div class="dashboard-actions">
          <div class="hero-feature-badge">⚡ Top 20 Hardest Questions Filter</div>
          <div class="hero-feature-badge">📋 Gemini Zero-Knowledge Prompt Copy</div>
          <div class="hero-feature-badge">⏱️ Live 2-Hour Moodle Countdown Timer</div>
          <div class="hero-feature-badge">📐 KaTeX Mathematical Equations</div>
        </div>
      </section>

      <section class="modules-grid">
        ${modules.map(mod => `
          <div class="module-card" style="--module-accent: ${mod.accent};">
            <div>
              <div class="module-header">
                <span class="module-code-badge">${mod.code}</span>
                <span class="module-qcount-badge">📝 ${mod.questions.length} Past Questions</span>
              </div>
              <h2 class="module-title">${mod.title}</h2>
              <p class="module-desc">${mod.description}</p>
              
              <div class="module-papers-list">
                ${mod.papers.map(p => `
                  <div class="paper-chip">
                    <span class="paper-dot"></span>
                    <span>${p}</span>
                  </div>
                `).join('')}
              </div>
            </div>

            <div class="module-card-actions">
              <button class="btn-launch-full" data-module="${mod.id}" data-hardest="false">
                <span>Start Full Exam</span> →
              </button>
              <button class="btn-launch-hardest" data-module="${mod.id}" data-hardest="true">
                <span>⚡ Top 20 Hardest</span>
              </button>
            </div>
          </div>
        `).join('')}
      </section>
    </main>
  `;

  // Bind Dashboard Buttons
  app.querySelectorAll('.btn-launch-full').forEach(btn => {
    btn.onclick = () => {
      const mId = btn.dataset.module;
      launchQuiz(mId, false);
    };
  });

  app.querySelectorAll('.btn-launch-hardest').forEach(btn => {
    btn.onclick = () => {
      const mId = btn.dataset.module;
      launchQuiz(mId, true);
    };
  });

  const themeBtn = document.getElementById('themeToggleBtn');
  if (themeBtn) {
    themeBtn.onclick = () => {
      const nextTheme = state.theme === 'netexam' ? 'apple' : 'netexam';
      applyTheme(nextTheme);
      renderDashboard();
    };
  }
}

// Launch Quiz for a Module
function launchQuiz(moduleId, hardestOnly = false) {
  state.currentModuleId = moduleId;
  state.hardestOnly = hardestOnly;
  state.activeQuestionIndex = 0;
  state.view = 'quiz';
  state.timerSeconds = 7200; // 2 hours
  startTimer();
  renderQuiz();
}

// Render Quiz View (Exact NetExam Replication)
function renderQuiz() {
  const mod = quizData[state.currentModuleId];
  const questions = getActiveQuestions();
  const currentQ = questions[state.activeQuestionIndex];
  const qState = state.userResponses[state.currentModuleId][currentQ.id];
  const isAnswered = Object.keys(qState.answers).length > 0;

  app.innerHTML = `
    <!-- Top Header -->
    <header class="netexam-header">
      <div class="netexam-brand">
        <div class="netexam-logo-text">
          <div class="netexam-logo-main">
            SLIIT <span class="netexam-badge-uni">UNI</span> NetExam
          </div>
          <div class="netexam-logo-sub">Online Examination Platform</div>
        </div>
        <nav class="netexam-nav-links">
          <a href="#" class="netexam-nav-link" id="navDashboardLink">Dashboard</a>
          <a href="#" class="netexam-nav-link active">Examinations</a>
          <a href="#" class="netexam-nav-link">Lockdown Browser</a>
          <a href="#" class="netexam-nav-link">Practice Test</a>
        </nav>
      </div>
      <div class="netexam-user-area">
        <div class="netexam-user-badge">
          <div class="netexam-user-avatar">RD</div>
          <div class="netexam-user-name">IT22117182 ROOPASINGHE M.D.</div>
        </div>
        <button class="hardest-toggle-chip" id="themeToggleBtn">
          ${state.theme === 'netexam' ? '🖥️ NetExam Lab' : '🍎 Apple Clean'}
        </button>
      </div>
    </header>

    <!-- Module Banner -->
    <div class="netexam-module-banner">
      <div>
        <h1 class="netexam-module-title">${mod.title} — ${mod.code}</h1>
        <div class="netexam-module-sub">${currentQ.paper} • ${mod.semester}</div>
      </div>
      <button class="netexam-finish-link" id="exitToDashboardBtn" style="margin-bottom: 0;">
        ← Back to Dashboard
      </button>
    </div>

    <!-- Controls Bar -->
    <div class="netexam-controls-bar">
      <div class="netexam-breadcrumbs">
        <a href="#" id="crumbDashboard">Dashboard</a> / 
        <a href="#">My courses</a> / 
        <a href="#">${mod.code}</a> / 
        <span>Final Exam Simulator</span>
      </div>

      <div class="netexam-toggles-group">
        <!-- Top 20 Hardest Questions Toggle -->
        <label class="toggle-switch-wrap" title="Toggle Top 20 Hardest Questions">
          <span style="font-size: 12.5px; font-weight: 600;">⚡ Top 20 Hardest Theory Mode:</span>
          <div class="toggle-switch ${state.hardestOnly ? 'active' : ''}" id="hardestToggle">
            <div class="toggle-slider"></div>
          </div>
        </label>

        <!-- Shuffle Toggle -->
        <label class="toggle-switch-wrap" title="Shuffle questions order">
          <span style="font-size: 12.5px; font-weight: 600;">🔀 Shuffle:</span>
          <div class="toggle-switch ${state.shuffle ? 'active' : ''}" id="shuffleToggle">
            <div class="toggle-slider"></div>
          </div>
        </label>

        <!-- Learning Mode / Instant Check Toggle -->
        <label class="toggle-switch-wrap" title="Enable instant solution checking">
          <span style="font-size: 12.5px; font-weight: 600;">💡 Instant Check:</span>
          <div class="toggle-switch ${state.learningMode ? 'active' : ''}" id="learningToggle">
            <div class="toggle-slider"></div>
          </div>
        </label>
      </div>
    </div>

    <!-- Main Exam Container -->
    <div class="netexam-container">
      <!-- Left & Center: Question Shell -->
      <section>
        <div class="netexam-question-shell">
          <!-- Left Meta Card -->
          <div class="netexam-meta-box">
            <div class="netexam-qnumber">Question ${state.activeQuestionIndex + 1}</div>
            <div class="netexam-qstatus ${isAnswered ? 'answered' : ''}">
              ${isAnswered ? 'Answer saved' : 'Not yet answered'}
            </div>
            <div class="netexam-qmarks">Marked out of ${currentQ.marks.toFixed(2)}</div>
            <button class="netexam-flag-btn ${qState.flagged ? 'flagged' : ''}" id="flagBtn">
              <span>${qState.flagged ? '🚩' : '⚐'}</span>
              <span>${qState.flagged ? 'Remove flag' : 'Flag question'}</span>
            </button>
          </div>

          <!-- Middle Question Formulation Card -->
          <div class="netexam-formulation-card">
            <div class="netexam-question-topbar">
              <span class="netexam-topic-tag">📌 ${currentQ.topic}</span>
              <div style="display: flex; gap: 8px;">
                <button class="ask-gemini-btn" id="askGeminiBtn" title="Copy zero-knowledge prompt for Gemini">
                  <span class="gemini-sparkle-icon">✨</span> Ask Gemini (Copy Theory Prompt)
                </button>
                <button class="netexam-flag-btn" id="previewPromptBtn" title="Preview Gemini prompt">
                  👁️ Preview
                </button>
              </div>
            </div>

            <!-- Question Stem Text -->
            <div class="netexam-prompt-text">
              ${renderLatex(currentQ.prompt)}
            </div>

            <!-- Embedded Image (if question has chart/diagram) -->
            ${currentQ.image ? `
              <div class="netexam-image-box">
                <img src="${currentQ.image}" alt="Question Diagram" />
              </div>
            ` : ''}

            <!-- Subquestions / Inputs -->
            <div class="netexam-subquestions">
              ${renderQuestionInputs(currentQ, qState)}
            </div>

            <!-- Solution & Marking Scheme (shown if checked or in review) -->
            ${qState.checked ? `
              <div class="netexam-solution-box">
                <div class="netexam-solution-header">
                  <span>✅ Official Solution & Step-by-Step Marking Theory:</span>
                </div>
                <div>${renderLatex(currentQ.solution || currentQ.theorySummary)}</div>
              </div>
            ` : ''}

            <!-- Action Navigation Buttons -->
            <div class="netexam-actions-bar">
              <button class="netexam-btn-nav" id="prevBtn" ${state.activeQuestionIndex === 0 ? 'disabled' : ''}>
                Previous page
              </button>

              <div style="display: flex; gap: 10px;">
                ${state.learningMode && !qState.checked ? `
                  <button class="netexam-btn-solution" id="checkAnswerBtn">
                    Check Answer & Theory
                  </button>
                ` : ''}
                <button class="netexam-btn-nav" id="nextBtn">
                  ${state.activeQuestionIndex === questions.length - 1 ? 'Finish attempt ...' : 'Next page'}
                </button>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Right Column: Quiz Navigation Block -->
      <aside class="netexam-nav-drawer">
        <div class="netexam-nav-drawer-header">
          <span>≡ Quiz navigation</span>
        </div>

        <!-- 1..N Square Matrix Grid -->
        <div class="netexam-grid-matrix">
          ${questions.map((q, idx) => {
            const resp = state.userResponses[state.currentModuleId][q.id];
            const answered = Object.keys(resp.answers).length > 0;
            const flagged = resp.flagged;
            const isActive = idx === state.activeQuestionIndex;
            return `
              <button class="netexam-qbox ${isActive ? 'active' : ''} ${answered ? 'answered' : ''} ${flagged ? 'flagged' : ''}" data-index="${idx}">
                ${idx + 1}
              </button>
            `;
          }).join('')}
        </div>

        <button class="netexam-finish-link" id="finishAttemptLink">
          Finish attempt ...
        </button>

        <!-- Live Countdown Timer -->
        <div class="netexam-timer-box">
          <span>Time left</span>
          <span class="netexam-timer-digits" id="timerDigits">1:58:10</span>
        </div>
      </aside>
    </div>
  `;

  updateTimerDisplay();
  bindQuizEvents(currentQ, questions);
}

// Render Inputs (Dropdowns, Textboxes, Radios)
function renderQuestionInputs(q, qState) {
  if (q.type === 'multipart' && q.subquestions) {
    return q.subquestions.map((sq, i) => {
      const val = qState.answers[sq.id] || '';
      if (sq.type === 'dropdown') {
        return `
          <div class="netexam-subquestion-row">
            <label class="netexam-subquestion-label">${renderLatex(sq.label)}</label>
            ${sq.instruction ? `<div class="netexam-instruction-note">${sq.instruction}</div>` : ''}
            <select class="netexam-select" data-sqid="${sq.id}">
              <option value="">Choose...</option>
              ${sq.options.map(opt => `
                <option value="${opt}" ${val === opt ? 'selected' : ''}>${opt}</option>
              `).join('')}
            </select>
          </div>
        `;
      } else if (sq.type === 'text') {
        return `
          <div class="netexam-subquestion-row">
            <label class="netexam-subquestion-label">${renderLatex(sq.label)}</label>
            ${sq.instruction ? `<div class="netexam-instruction-note">${sq.instruction}</div>` : ''}
            <input type="text" class="netexam-text-input" data-sqid="${sq.id}" value="${val}" placeholder="Type answer here..." />
          </div>
        `;
      } else if (sq.type === 'radio') {
        return `
          <div class="netexam-subquestion-row">
            <label class="netexam-subquestion-label">${renderLatex(sq.label)}</label>
            <div class="netexam-radio-list">
              ${sq.options.map((opt, oi) => `
                <label class="netexam-radio-item">
                  <input type="radio" name="${sq.id}" value="${oi}" ${val === oi.toString() ? 'checked' : ''} data-sqid="${sq.id}" />
                  <span>${renderLatex(opt)}</span>
                </label>
              `).join('')}
            </div>
          </div>
        `;
      }
    }).join('');
  } else if (q.options) {
    // Single MCQ question
    const val = qState.answers['mcq'] || '';
    return `
      <div class="netexam-radio-list">
        ${q.options.map((opt, oi) => `
          <label class="netexam-radio-item">
            <input type="radio" name="mcq_${q.id}" value="${oi}" ${val === oi.toString() ? 'checked' : ''} data-sqid="mcq" />
            <span><strong>${String.fromCharCode(65 + oi)}.</strong> ${renderLatex(opt)}</span>
          </label>
        `).join('')}
      </div>
    `;
  }
  return '';
}

// Bind Quiz Events
function bindQuizEvents(currentQ, questions) {
  // Navigation Links
  const navDash = document.getElementById('navDashboardLink');
  const exitBtn = document.getElementById('exitToDashboardBtn');
  const crumbDash = document.getElementById('crumbDashboard');
  [navDash, exitBtn, crumbDash].forEach(btn => {
    if (btn) btn.onclick = (e) => {
      e.preventDefault();
      clearInterval(state.timerInterval);
      state.view = 'dashboard';
      renderDashboard();
    };
  });

  // Next / Previous Buttons
  const prevBtn = document.getElementById('prevBtn');
  if (prevBtn) {
    prevBtn.onclick = () => {
      if (state.activeQuestionIndex > 0) {
        state.activeQuestionIndex--;
        renderQuiz();
      }
    };
  }

  const nextBtn = document.getElementById('nextBtn');
  if (nextBtn) {
    nextBtn.onclick = () => {
      if (state.activeQuestionIndex < questions.length - 1) {
        state.activeQuestionIndex++;
        renderQuiz();
      } else {
        openFinishModal();
      }
    };
  }

  // Jump to Question Box
  app.querySelectorAll('.netexam-qbox').forEach(btn => {
    btn.onclick = () => {
      state.activeQuestionIndex = parseInt(btn.dataset.index, 10);
      renderQuiz();
    };
  });

  // Flag Question Toggle
  const flagBtn = document.getElementById('flagBtn');
  if (flagBtn) {
    flagBtn.onclick = () => {
      const qState = state.userResponses[state.currentModuleId][currentQ.id];
      qState.flagged = !qState.flagged;
      renderQuiz();
    };
  }

  // Check Answer Button (Learning mode)
  const checkBtn = document.getElementById('checkAnswerBtn');
  if (checkBtn) {
    checkBtn.onclick = () => {
      const qState = state.userResponses[state.currentModuleId][currentQ.id];
      qState.checked = true;
      renderQuiz();
    };
  }

  // Ask Gemini Copy Button
  const askGeminiBtn = document.getElementById('askGeminiBtn');
  if (askGeminiBtn) {
    askGeminiBtn.onclick = () => handleCopyPrompt(currentQ);
  }

  const previewPromptBtn = document.getElementById('previewPromptBtn');
  if (previewPromptBtn) {
    previewPromptBtn.onclick = () => openPromptModal(currentQ);
  }

  // Save Input Values
  app.querySelectorAll('.netexam-select').forEach(sel => {
    sel.onchange = (e) => {
      const sqId = e.target.dataset.sqid;
      state.userResponses[state.currentModuleId][currentQ.id].answers[sqId] = e.target.value;
      updateSidebarBoxes();
    };
  });

  app.querySelectorAll('.netexam-text-input').forEach(inp => {
    inp.oninput = (e) => {
      const sqId = e.target.dataset.sqid;
      state.userResponses[state.currentModuleId][currentQ.id].answers[sqId] = e.target.value.trim();
      updateSidebarBoxes();
    };
  });

  app.querySelectorAll('input[type="radio"]').forEach(rad => {
    rad.onchange = (e) => {
      const sqId = e.target.dataset.sqid;
      state.userResponses[state.currentModuleId][currentQ.id].answers[sqId] = e.target.value;
      updateSidebarBoxes();
    };
  });

  // Toggles
  const hardestToggle = document.getElementById('hardestToggle');
  if (hardestToggle) {
    hardestToggle.onclick = () => {
      state.hardestOnly = !state.hardestOnly;
      state.activeQuestionIndex = 0;
      renderQuiz();
    };
  }

  const shuffleToggle = document.getElementById('shuffleToggle');
  if (shuffleToggle) {
    shuffleToggle.onclick = () => {
      state.shuffle = !state.shuffle;
      state.activeQuestionIndex = 0;
      renderQuiz();
    };
  }

  const learningToggle = document.getElementById('learningToggle');
  if (learningToggle) {
    learningToggle.onclick = () => {
      state.learningMode = !state.learningMode;
      renderQuiz();
    };
  }

  const finishAttemptLink = document.getElementById('finishAttemptLink');
  if (finishAttemptLink) {
    finishAttemptLink.onclick = () => openFinishModal();
  }

  const themeBtn = document.getElementById('themeToggleBtn');
  if (themeBtn) {
    themeBtn.onclick = () => {
      const nextTheme = state.theme === 'netexam' ? 'apple' : 'netexam';
      applyTheme(nextTheme);
      renderQuiz();
    };
  }
}

function updateSidebarBoxes() {
  const currentQ = getActiveQuestions()[state.activeQuestionIndex];
  const qState = state.userResponses[state.currentModuleId][currentQ.id];
  const isAnswered = Object.keys(qState.answers).length > 0;

  const currentBox = document.querySelector(`.netexam-qbox[data-index="${state.activeQuestionIndex}"]`);
  if (currentBox) {
    if (isAnswered) currentBox.classList.add('answered');
    else currentBox.classList.remove('answered');
  }

  const statusText = document.querySelector('.netexam-qstatus');
  if (statusText) {
    statusText.textContent = isAnswered ? 'Answer saved' : 'Not yet answered';
    if (isAnswered) statusText.classList.add('answered');
    else statusText.classList.remove('answered');
  }
}

// Finish Attempt Modal
function openFinishModal() {
  const mod = quizData[state.currentModuleId];
  const questions = getActiveQuestions();

  let answeredCount = 0;
  let flaggedCount = 0;

  questions.forEach(q => {
    const r = state.userResponses[state.currentModuleId][q.id];
    if (Object.keys(r.answers).length > 0) answeredCount++;
    if (r.flagged) flaggedCount++;
  });

  const modal = document.createElement('div');
  modal.className = 'modal-overlay';
  modal.innerHTML = `
    <div class="modal-card">
      <div class="modal-header">
        <h3>Summary of Attempt — ${mod.code}</h3>
        <button class="modal-close" id="closeFinishModal" style="font-size: 20px; color: #64748b;">✕</button>
      </div>
      <div class="modal-body">
        <p style="margin-bottom: 16px; font-size: 15px;">
          You have answered <strong>${answeredCount}</strong> of <strong>${questions.length}</strong> questions.
          ${flaggedCount > 0 ? `<br><span style="color: #dc2626;">🚩 ${flaggedCount} question(s) flagged for review.</span>` : ''}
        </p>

        <table style="width: 100%; border-collapse: collapse; font-size: 13.5px;">
          <thead>
            <tr style="background: #f1f5f9; text-align: left;">
              <th style="padding: 8px 12px; border: 1px solid #e2e8f0;">Question</th>
              <th style="padding: 8px 12px; border: 1px solid #e2e8f0;">Status</th>
            </tr>
          </thead>
          <tbody>
            ${questions.map((q, idx) => {
              const r = state.userResponses[state.currentModuleId][q.id];
              const ans = Object.keys(r.answers).length > 0;
              return `
                <tr>
                  <td style="padding: 8px 12px; border: 1px solid #e2e8f0;">
                    Question ${idx + 1} (${q.topic})
                  </td>
                  <td style="padding: 8px 12px; border: 1px solid #e2e8f0; font-weight: 600; color: ${ans ? '#15803d' : '#64748b'};">
                    ${ans ? 'Answer saved' : 'Not yet answered'} ${r.flagged ? '🚩' : ''}
                  </td>
                </tr>
              `;
            }).join('')}
          </tbody>
        </table>
      </div>
      <div class="modal-footer">
        <button class="netexam-btn-solution" id="returnAttemptBtn" style="background: #64748b;">
          Return to attempt
        </button>
        <button class="netexam-btn-nav" id="submitAllBtn">
          Submit all and finish
        </button>
      </div>
    </div>
  `;
  document.body.appendChild(modal);

  modal.querySelector('#closeFinishModal').onclick = () => modal.remove();
  modal.querySelector('#returnAttemptBtn').onclick = () => modal.remove();
  modal.querySelector('#submitAllBtn').onclick = () => {
    modal.remove();
    submitExam();
  };
}

// Final Submission & Score Calculation
function submitExam() {
  clearInterval(state.timerInterval);
  confetti({ particleCount: 120, spread: 70, origin: { y: 0.6 } });

  const questions = getActiveQuestions();
  let correctCount = 0;
  let totalScore = 0;
  let maxMarks = 0;

  questions.forEach(q => {
    maxMarks += q.marks;
    const r = state.userResponses[state.currentModuleId][q.id];
    let qEarned = 0;

    if (q.type === 'multipart' && q.subquestions) {
      let subCorrect = 0;
      q.subquestions.forEach(sq => {
        const userVal = (r.answers[sq.id] || '').toString().toLowerCase();
        const expected = (sq.answer || '').toString().toLowerCase();
        const accepted = (sq.acceptedAnswers || []).map(a => a.toLowerCase());

        if (userVal && (userVal === expected || accepted.includes(userVal))) {
          subCorrect++;
        }
      });
      qEarned = (subCorrect / q.subquestions.length) * q.marks;
      if (subCorrect === q.subquestions.length) correctCount++;
    } else if (q.options) {
      const userVal = r.answers['mcq'];
      if (userVal === q.answer.toString()) {
        correctCount++;
        qEarned = q.marks;
      }
    }
    totalScore += qEarned;
  });

  const percentage = maxMarks > 0 ? ((totalScore / maxMarks) * 100).toFixed(1) : '0';

  // Mark all questions as checked so full solutions show
  questions.forEach(q => {
    state.userResponses[state.currentModuleId][q.id].checked = true;
  });

  // Display results modal
  const modal = document.createElement('div');
  modal.className = 'modal-overlay';
  modal.innerHTML = `
    <div class="modal-card">
      <div class="modal-header">
        <h3>🎉 Examination Review & Score Breakdown</h3>
        <button class="modal-close" id="closeReviewModal" style="font-size: 20px; color: #64748b;">✕</button>
      </div>
      <div class="modal-body" style="text-align: center; padding: 32px 24px;">
        <div style="font-size: 54px; font-weight: 900; color: #2563eb; margin-bottom: 8px;">
          ${percentage}%
        </div>
        <div style="font-size: 18px; font-weight: 700; color: #1e293b; margin-bottom: 8px;">
          Total Score: ${totalScore.toFixed(1)} / ${maxMarks.toFixed(1)} Marks
        </div>
        <p style="color: #64748b; font-size: 14px; margin-bottom: 24px;">
          You got <strong>${correctCount}</strong> out of <strong>${questions.length}</strong> questions completely correct.<br>
          All step-by-step mathematical solutions and grading schemes are now unlocked on each question card.
        </p>
      </div>
      <div class="modal-footer" style="justify-content: center;">
        <button class="netexam-btn-nav" id="viewDetailedSolutionsBtn">
          Review Detailed Solutions
        </button>
        <button class="netexam-btn-solution" id="backToHomeBtn">
          Back to Dashboard
        </button>
      </div>
    </div>
  `;
  document.body.appendChild(modal);

  modal.querySelector('#closeReviewModal').onclick = () => modal.remove();
  modal.querySelector('#viewDetailedSolutionsBtn').onclick = () => {
    modal.remove();
    state.activeQuestionIndex = 0;
    renderQuiz();
  };
  modal.querySelector('#backToHomeBtn').onclick = () => {
    modal.remove();
    state.view = 'dashboard';
    renderDashboard();
  };
}

// Bootstrap
applyTheme(state.theme);
renderDashboard();
