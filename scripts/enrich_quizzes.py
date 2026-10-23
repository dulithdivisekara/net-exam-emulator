import json

with open("/home/dulith/Projects/net_exam_emulator/src/data/quizzes.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# =========================================================================
# ADDITIONAL PAS QUESTIONS (Total will be 20)
# =========================================================================
pas_extra = [
    {
        "id": "PAS-EXTRA-12",
        "paper": "Final Exam Past Papers Compilation",
        "questionNumber": 7,
        "topic": "Discrete Distributions: Binomial Probability",
        "marks": 10.00,
        "difficulty": "Medium",
        "prompt": "An automated testing suite tests 10 microservices. Each service has a probability $p = 0.05$ of failing a build, independently of other services. Let $X$ be the number of failed microservices.\n\nCalculate the probability that exactly 2 microservices fail the build: $P(X = 2) = \\binom{n}{x} p^x (1-p)^{n-x}$.",
        "type": "mcq",
        "options": [
            "0.0746",
            "0.0105",
            "0.0025",
            "0.1937"
        ],
        "answer": 0,
        "solution": "n = 10, x = 2, p = 0.05, 1-p = 0.95. P(X = 2) = (10! / (2! * 8!)) * (0.05)^2 * (0.95)^8 = 45 * 0.0025 * 0.66342 = 0.0746.",
        "theorySummary": "Binomial distribution X ~ Bin(n, p) applies to n independent trials with two outcomes (success/failure) and constant probability p. Mean = np, Variance = np(1-p)."
    },
    {
        "id": "PAS-EXTRA-13",
        "paper": "Final Exam Past Papers Compilation",
        "questionNumber": 8,
        "topic": "Discrete Distributions: Poisson Rate Process",
        "marks": 10.00,
        "difficulty": "Medium",
        "prompt": "A web server receives on average $\\lambda = 4$ incoming API requests per minute. Assuming arrivals follow a Poisson distribution:\n\nWhat is the probability of receiving at most 1 request in a given minute?",
        "type": "mcq",
        "options": [
            "0.0916",
            "0.0183",
            "0.0733",
            "0.1465"
        ],
        "answer": 0,
        "solution": "P(X <= 1) = P(X = 0) + P(X = 1). P(X = 0) = (e^-4 * 4^0) / 0! = e^-4 ≈ 0.0183. P(X = 1) = (e^-4 * 4^1) / 1! = 4 * 0.0183 = 0.0733. Total = 0.0183 + 0.0733 = 0.0916.",
        "theorySummary": "Poisson distribution models event arrivals in a fixed interval of time or space: P(X = x) = (e^-λ * λ^x) / x!. Mean = λ, Variance = λ."
    },
    {
        "id": "PAS-EXTRA-14",
        "paper": "Lockdown Exam Revision",
        "questionNumber": 9,
        "topic": "Two-Sample t-Test for Independent Means",
        "marks": 15.00,
        "difficulty": "Expert",
        "prompt": "Two database index configurations A and B are evaluated for query latency. A sample of 15 queries on Index A gives $\\bar{x}_1 = 45\\text{ms}, s_1 = 6\\text{ms}$. A sample of 15 queries on Index B gives $\\bar{x}_2 = 52\\text{ms}, s_2 = 8\\text{ms}$. Assume equal population variances $\\sigma_1^2 = \\sigma_2^2$.\n\n1. Calculate the pooled variance estimate $s_p^2 = \\frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1 + n_2 - 2}$.\n2. Calculate the calculated t-statistic $t = \\frac{\\bar{x}_1 - \\bar{x}_2}{s_p \\sqrt{\\frac{1}{n_1} + \\frac{1}{n_2}}}$.",
        "type": "multipart",
        "subquestions": [
            {
                "id": "sq1",
                "label": "Pooled variance sp^2:",
                "type": "text",
                "answer": "50",
                "acceptedAnswers": ["50", "50.0"],
                "hint": "sp^2 = [14(36) + 14(64)] / 28 = 14(100) / 28 = 50.0."
            },
            {
                "id": "sq2",
                "label": "Calculated t-statistic (round to 2 decimals):",
                "type": "text",
                "answer": "-2.71",
                "acceptedAnswers": ["-2.71", "-2.7", "2.71"],
                "hint": "sp = √50 = 7.071. SE = 7.071 * √(2/15) = 7.071 * 0.36515 = 2.582. t = (45 - 52) / 2.582 = -7 / 2.582 = -2.71."
            }
        ],
        "theorySummary": "When comparing two independent means with unknown but assumed equal variances, pool the sample variances: sp² = [(n1-1)s1² + (n2-1)s2²] / (n1+n2-2). Degrees of freedom df = n1 + n2 - 2."
    },
    {
        "id": "PAS-EXTRA-15",
        "paper": "Lockdown Exam Revision",
        "questionNumber": 10,
        "topic": "Simple Linear Regression & Coefficient of Determination",
        "marks": 15.00,
        "difficulty": "Hard",
        "prompt": "In a regression study predicting system memory usage ($Y$, in GB) from concurrent user sessions ($X$), an analysis of variance (ANOVA) table yields:\n- Sum of Squares Regression ($SSR$) = 450\n- Sum of Squares Error ($SSE$) = 50\n- Total Sum of Squares ($SST$) = 500\n\n1. What is the coefficient of determination $R^2 = \\frac{SSR}{SST}$?\n2. What is the interpretation of this $R^2$ value?",
        "type": "multipart",
        "subquestions": [
            {
                "id": "sq1",
                "label": "R-squared value:",
                "type": "text",
                "answer": "0.9",
                "acceptedAnswers": ["0.9", "0.90", "90%"],
                "hint": "R² = 450 / 500 = 0.90."
            },
            {
                "id": "sq2",
                "label": "Interpretation:",
                "type": "dropdown",
                "options": [
                    "90% of the total variation in memory usage is explained by the number of concurrent sessions",
                    "The correlation coefficient between X and Y is exactly 0.90",
                    "There is a 90% chance that the regression slope is statistically significant",
                    "10% of memory usage is caused by user sessions"
                ],
                "answer": "90% of the total variation in memory usage is explained by the number of concurrent sessions",
                "hint": "R² measures the proportion of total variation in the dependent variable Y explained by the independent variable X."
            }
        ],
        "theorySummary": "SST = SSR + SSE. The coefficient of determination R² = SSR / SST = 1 - (SSE / SST) represents the fraction of variance explained by the model."
    },
    {
        "id": "PAS-EXTRA-16",
        "paper": "Lockdown Exam Revision",
        "questionNumber": 11,
        "topic": "One-Way ANOVA F-Test for Multiple Groups",
        "marks": 15.00,
        "difficulty": "Expert",
        "prompt": "An experiment compares the page load times across 3 different web browsers ($k = 3$) with 10 test runs per browser ($N = 30$).\nThe ANOVA results show:\n- Between-groups sum of squares ($SSB$) = 120\n- Within-groups sum of squares ($SSW$) = 270\n\nCalculate the F-test statistic: $F = \\frac{MSB}{MSW} = \\frac{SSB / (k-1)}{SSW / (N-k)}$.",
        "type": "mcq",
        "options": [
            "6.00",
            "4.50",
            "2.25",
            "0.44"
        ],
        "answer": 0,
        "solution": "df_between = k - 1 = 3 - 1 = 2. MSB = 120 / 2 = 60. df_within = N - k = 30 - 3 = 27. MSW = 270 / 27 = 10. F = MSB / MSW = 60 / 10 = 6.00.",
        "theorySummary": "One-Way ANOVA evaluates H0: μ1 = μ2 = ... = μk vs H1: at least one mean differs. The test statistic F = MSB / MSW follows an F-distribution with (k-1, N-k) degrees of freedom."
    },
    {
        "id": "PAS-EXTRA-17",
        "paper": "Final Exam Past Papers Compilation",
        "questionNumber": 12,
        "topic": "Central Limit Theorem Properties",
        "marks": 5.00,
        "difficulty": "Medium",
        "prompt": "According to the Central Limit Theorem (CLT), as the sample size $n$ increases ($n \\ge 30$), which of the following statements is TRUE regarding the sampling distribution of the sample mean $\\bar{X}$?",
        "type": "mcq",
        "options": [
            "The sampling distribution approaches a Normal distribution with mean μ and standard error σ / √n, regardless of the population distribution shape.",
            "The standard error of the sample mean increases proportionally with the square root of n.",
            "The sampling distribution becomes identical to the original population distribution.",
            "CLT applies only when the underlying population is strictly normally distributed."
        ],
        "answer": 0,
        "solution": "CLT states that for any population with mean μ and finite variance σ², the distribution of X̄ approaches N(μ, σ²/n) as n becomes large (typically n >= 30).",
        "theorySummary": "Central Limit Theorem is the foundation of inferential statistics. It ensures that sample means are normally distributed for large samples, with SE = σ / √n."
    },
    {
        "id": "PAS-EXTRA-18",
        "paper": "Lockdown Exam Revision",
        "questionNumber": 13,
        "topic": "Hypothesis Testing: Type I and Type II Errors",
        "marks": 8.00,
        "difficulty": "Hard",
        "prompt": "In statistical hypothesis testing, rejecting the null hypothesis $H_0$ when $H_0$ is actually TRUE is known as:",
        "type": "mcq",
        "options": [
            "Type I error (False Positive) with probability α",
            "Type II error (False Negative) with probability β",
            "Power of the test (1 - β)",
            "Sampling error"
        ],
        "answer": 0,
        "solution": "Type I error is the probability of rejecting a true null hypothesis, denoted by α (the significance level). Type II error is failing to reject a false null hypothesis, denoted by β.",
        "theorySummary": "Hypothesis testing decision grid: Reject H0 when true = Type I error (α). Fail to reject H0 when false = Type II error (β). Correctly rejecting false H0 = Power (1 - β)."
    },
    {
        "id": "PAS-EXTRA-19",
        "paper": "Final Exam Past Papers Compilation",
        "questionNumber": 14,
        "topic": "Simple Linear Regression Slope Formula",
        "marks": 10.00,
        "difficulty": "Hard",
        "prompt": "In simple linear regression $\\hat{y} = \\beta_0 + \\beta_1 x$, given the sample summary statistics:\n$n = 10, \\quad \\sum x = 50, \\quad \\sum y = 120, \\quad \\sum xy = 750, \\quad \\sum x^2 = 350$.\n\nCalculate the slope coefficient $\\beta_1 = \\frac{n \\sum xy - (\\sum x)(\\sum y)}{n \\sum x^2 - (\\sum x)^2}$.",
        "type": "mcq",
        "options": [
            "1.50",
            "2.40",
            "0.75",
            "-1.50"
        ],
        "answer": 0,
        "solution": "Numerator = 10(750) - (50)(120) = 7500 - 6000 = 1500. Denominator = 10(350) - (50)^2 = 3500 - 2500 = 1000. β1 = 1500 / 1000 = 1.50.",
        "theorySummary": "The least-squares estimator minimizes the sum of squared vertical residuals Σ(y - ŷ)². Slope β1 = SSxy / SSxx, and intercept β0 = ȳ - β1 * x̄."
    },
    {
        "id": "PAS-EXTRA-20",
        "paper": "Final Exam Past Papers Compilation",
        "questionNumber": 15,
        "topic": "Paired Difference t-Test",
        "marks": 10.00,
        "difficulty": "Expert",
        "prompt": "A paired-sample experiment measures execution time of 16 database queries before and after applying a query optimizer index. The sample mean difference is $\\bar{d} = 4.2\\text{ms}$ with standard deviation of differences $s_d = 2.4\\text{ms}$.\n\nCalculate the paired t-statistic $t = \\frac{\\bar{d}}{s_d / \\sqrt{n}}$ to test $H_0: \\mu_d = 0$.",
        "type": "mcq",
        "options": [
            "7.00",
            "1.75",
            "3.50",
            "4.20"
        ],
        "answer": 0,
        "solution": "Standard error of difference SE = sd / √n = 2.4 / √16 = 2.4 / 4 = 0.60. t = 4.2 / 0.60 = 7.00.",
        "theorySummary": "Paired t-test is applied when observations are matched in pairs (e.g. before-after measurements on the same subject), reducing variance by controlling for subject heterogeneity."
    }
]

data["PAS"]["questions"].extend(pas_extra)

# =========================================================================
# ADDITIONAL AIML QUESTIONS (Total will be 20)
# =========================================================================
aiml_extra = [
    {
        "id": "AIML-06",
        "paper": "2024 Final Revision Session",
        "questionNumber": 6,
        "topic": "Hierarchical Clustering & Linkage Metrics",
        "marks": 15.00,
        "difficulty": "Expert",
        "prompt": "In Agglomerative Hierarchical Clustering, what is the key distinction between Single Linkage and Complete Linkage when measuring distance between two clusters $A$ and $B$?",
        "type": "mcq",
        "options": [
            "Single Linkage uses the minimum pairwise distance min d(x, y), whereas Complete Linkage uses the maximum pairwise distance max d(x, y)",
            "Single Linkage uses cluster centroids, whereas Complete Linkage uses the average of all pairs",
            "Single Linkage creates a single cluster, whereas Complete Linkage creates completely separated clusters",
            "Single Linkage is non-hierarchical, whereas Complete Linkage is hierarchical"
        ],
        "answer": 0,
        "solution": "Single Linkage (minimum distance) merges clusters whose closest points are nearest (susceptible to chaining). Complete Linkage (maximum distance) considers the furthest points, producing compact spherical clusters.",
        "theorySummary": "Agglomerative clustering is bottom-up. Linkage criteria: Single (min distance), Complete (max distance), Average (mean distance), Ward's (minimum variance increase)."
    },
    {
        "id": "AIML-07",
        "paper": "2024 Final Revision Session",
        "questionNumber": 7,
        "topic": "Feature Scaling: Min-Max vs Z-Score Normalization",
        "marks": 10.00,
        "difficulty": "Medium",
        "prompt": "A feature $X$ has minimum value $X_{\\min} = 20$, maximum value $X_{\\max} = 100$, mean $\\mu = 50$, and standard deviation $\\sigma = 15$.\nFor an observed value $x = 60$:\n\n1. Calculate the Min-Max scaled value $x' = \\frac{x - X_{\\min}}{X_{\\max} - X_{\\min}}$.\n2. Calculate the Z-score standardized value $z = \\frac{x - \\mu}{\\sigma}$.",
        "type": "multipart",
        "subquestions": [
            {
                "id": "sq1",
                "label": "Min-Max scaled value (in [0, 1]):",
                "type": "text",
                "answer": "0.5",
                "acceptedAnswers": ["0.5", "0.50"],
                "hint": "x' = (60 - 20) / (100 - 20) = 40 / 80 = 0.50."
            },
            {
                "id": "sq2",
                "label": "Z-score standardized value (round to 2 decimals):",
                "type": "text",
                "answer": "0.67",
                "acceptedAnswers": ["0.67", "0.667"],
                "hint": "z = (60 - 50) / 15 = 10 / 15 = 0.67."
            }
        ],
        "theorySummary": "Min-Max scaling bounds data strictly to [0, 1]. Z-score standardization centers data at mean 0 with unit variance, preserving outlier information."
    },
    {
        "id": "AIML-08",
        "paper": "Deep Learning Structure Revision",
        "questionNumber": 8,
        "topic": "Activation Functions: Dying ReLU Problem",
        "marks": 8.00,
        "difficulty": "Hard",
        "prompt": "What causes the 'Dying ReLU' problem in deep neural networks, and how does Leaky ReLU address it?",
        "type": "mcq",
        "options": [
            "For inputs z <= 0, standard ReLU has gradient 0, preventing weight updates; Leaky ReLU allows a small positive slope (e.g. 0.01z) for z < 0.",
            "Standard ReLU produces values greater than 1, causing exploding gradients.",
            "ReLU cannot be computed using GPU hardware accelerators.",
            "Dying ReLU occurs only during inference, not during training."
        ],
        "answer": 0,
        "solution": "ReLU(z) = max(0, z). When z <= 0, its derivative is 0. If a neuron's weights update such that it always receives negative input, it never activates again. Leaky ReLU introduces a small gradient α for negative inputs.",
        "theorySummary": "ReLU f(z) = max(0, z) accelerates training by solving vanishing gradients for positive inputs, but can suffer from dead neurons. Variants like Leaky ReLU and ELU provide nonzero gradients for negative inputs."
    },
    {
        "id": "AIML-09",
        "paper": "Deep Learning Structure Revision",
        "questionNumber": 9,
        "topic": "Convolutional Neural Networks: Output Feature Map Size",
        "marks": 12.00,
        "difficulty": "Expert",
        "prompt": "An input image of size $32 \\times 32$ is passed through a convolutional layer with $5 \\times 5$ filters, stride $S = 1$, and zero padding $P = 2$.\n\nCalculate the spatial dimensions $(W_{\\text{out}} \\times H_{\\text{out}})$ of the output feature map using the formula: $W_{\\text{out}} = \\frac{W_{\\text{in}} - F + 2P}{S} + 1$.",
        "type": "mcq",
        "options": [
            "32 x 32 (Same padding preserves spatial dimension)",
            "28 x 28",
            "30 x 30",
            "36 x 36"
        ],
        "answer": 0,
        "solution": "W_out = (32 - 5 + 2*2) / 1 + 1 = (32 - 5 + 4) + 1 = 31 + 1 = 32. Dimensions are 32 x 32.",
        "theorySummary": "Convolutional feature map spatial dimensions depend on input size, kernel size F, stride S, and padding P. Padding P = (F-1)/2 maintains identical dimensions."
    },
    {
        "id": "AIML-10",
        "paper": "Deep Learning Structure Revision",
        "questionNumber": 10,
        "topic": "Pooling Layers: Max Pooling vs Average Pooling",
        "marks": 6.00,
        "difficulty": "Medium",
        "prompt": "In CNNs, what is the primary role of a $2 \\times 2$ Max Pooling layer with stride 2?",
        "type": "mcq",
        "options": [
            "Downsample spatial dimensions by 50%, reducing parameter count and computational load while providing translational invariance.",
            "Increase the number of channel filters in the network.",
            "Normalize activations across the mini-batch.",
            "Perform non-linear activation like Sigmoid."
        ],
        "answer": 0,
        "solution": "Max pooling extracts the maximum value in each 2x2 neighborhood, halving width and height, reducing memory and computation, and retaining dominant features.",
        "theorySummary": "Pooling layers downsample feature maps without adding learnable parameters, enhancing spatial invariance and reducing overfitting."
    },
    {
        "id": "AIML-11",
        "paper": "2024 Final Revision Session",
        "questionNumber": 11,
        "topic": "Gradient Descent Optimization & Learning Rate",
        "marks": 10.00,
        "difficulty": "Hard",
        "prompt": "A single weight $w$ in a model currently has value $w = 2.0$. The gradient of the loss function with respect to $w$ is $\\frac{\\partial L}{\\partial w} = 3.5$. The learning rate is $\\eta = 0.1$.\n\nCalculate the updated weight value $w_{\\text{new}} = w - \\eta \\frac{\\partial L}{\\partial w}$.",
        "type": "mcq",
        "options": [
            "1.65",
            "2.35",
            "1.50",
            "-1.50"
        ],
        "answer": 0,
        "solution": "w_new = 2.0 - 0.1 * (3.5) = 2.0 - 0.35 = 1.65.",
        "theorySummary": "Gradient descent updates parameters in the direction opposite to the gradient: θ = θ - η * ∇L. Small learning rates cause slow convergence; large rates cause divergence."
    },
    {
        "id": "AIML-12",
        "paper": "Deep Learning Structure Revision",
        "questionNumber": 12,
        "topic": "Regularization: Dropout in Deep Networks",
        "marks": 8.00,
        "difficulty": "Medium",
        "prompt": "How does Dropout regularization prevent overfitting during the training phase of a deep neural network?",
        "type": "mcq",
        "options": [
            "It randomly deactivates a fraction p of neurons during each forward pass, forcing network units to learn co-independent features.",
            "It adds the sum of squared weights to the loss function.",
            "It clamps all negative weights to zero.",
            "It normalizes inputs to have mean zero."
        ],
        "answer": 0,
        "solution": "Dropout temporarily removes random units (and their incoming/outgoing edges) with probability p during training, preventing complex co-adaptations between neurons.",
        "theorySummary": "Dropout acts as an ensemble of exponentially many thinned networks. During evaluation/inference, all units are active, scaled by (1 - p)."
    },
    {
        "id": "AIML-13",
        "paper": "2024 Final Revision Session",
        "questionNumber": 13,
        "topic": "Ensemble Learning: Bagging vs Boosting",
        "marks": 10.00,
        "difficulty": "Hard",
        "prompt": "What is the key structural difference between Random Forests (Bagging) and Gradient Boosting Machines (Boosting)?",
        "type": "mcq",
        "options": [
            "Random Forests train trees independently in parallel on bootstrap samples; Boosting trains trees sequentially, each correcting the residual errors of prior trees.",
            "Random Forests are for classification only; Boosting is for regression only.",
            "Random Forests use deep neural nets as base learners; Boosting uses linear models.",
            "Boosting reduces variance only, while Bagging reduces bias only."
        ],
        "answer": 0,
        "solution": "Bagging (Bootstrap Aggregating) trains models independently in parallel to reduce variance. Boosting builds models iteratively in sequence to reduce bias.",
        "theorySummary": "Bagging builds independent models on random subsets and averages predictions. Boosting assigns higher weights to misclassified instances to iteratively correct errors."
    },
    {
        "id": "AIML-14",
        "paper": "2024 Final Revision Session",
        "questionNumber": 14,
        "topic": "Support Vector Machines (SVM): Hyperplane Margin",
        "marks": 10.00,
        "difficulty": "Expert",
        "prompt": "In a linear Support Vector Machine with separating hyperplane $\\mathbf{w}^T \\mathbf{x} + b = 0$, what is the geometric margin distance between the two canonical support vector hyperplanes $\\mathbf{w}^T \\mathbf{x} + b = 1$ and $\\mathbf{w}^T \\mathbf{x} + b = -1$?",
        "type": "mcq",
        "options": [
            "2 / ||w||",
            "1 / ||w||^2",
            "||w|| / 2",
            "w^T w"
        ],
        "answer": 0,
        "solution": "The perpendicular distance between the positive margin hyperplane and negative margin hyperplane is 2 / ||w||. Maximizing the margin corresponds to minimizing (1/2)||w||².",
        "theorySummary": "SVM searches for the Maximum Margin Hyperplane that maximizes distance to the closest training points (support vectors), providing strong generalization guarantees."
    },
    {
        "id": "AIML-15",
        "paper": "Deep Learning Structure Revision",
        "questionNumber": 15,
        "topic": "Loss Functions: Binary Cross-Entropy",
        "marks": 10.00,
        "difficulty": "Hard",
        "prompt": "For a binary classification instance with ground truth label $y = 1$, the model outputs predicted probability $\\hat{y} = 0.8$. Calculate the Binary Cross-Entropy loss $L = -[y \\ln(\\hat{y}) + (1-y) \\ln(1-\\hat{y})]$. (Given $\\ln(0.8) \\approx -0.2231$).",
        "type": "mcq",
        "options": [
            "0.2231",
            "0.8000",
            "0.5108",
            "1.6094"
        ],
        "answer": 0,
        "solution": "Since y = 1, L = -[1 * ln(0.8) + 0] = -(-0.2231) = 0.2231.",
        "theorySummary": "Cross-Entropy loss penalizes confident wrong predictions severely (as ŷ -> 0 when y = 1, loss -> ∞), ensuring steep gradients during backpropagation."
    }
]

data["AIML"]["questions"].extend(aiml_extra)

# =========================================================================
# ADDITIONAL DDD / DMS QUESTIONS (Total will be 20)
# =========================================================================
dms_extra = [
    {
        "id": "DDD-05",
        "paper": "2023 Final Examination",
        "questionNumber": 5,
        "topic": "EER Specialization: Disjoint vs Overlapping Constraints",
        "marks": 12.00,
        "difficulty": "Medium",
        "prompt": "In the 2023 Final Exam EER model, an entity `AcademicStaff` has subclasses `Supervisor` and `PanelMember` with the constraint `{overlap}`. What does the `{overlap}` constraint mean?",
        "type": "mcq",
        "options": [
            "A single academic staff member can simultaneously act as both a Supervisor and a Panel Member.",
            "An academic staff member must be either a Supervisor or a Panel Member, but cannot be both.",
            "All academic staff members must be supervisors.",
            "Supervisors and Panel Members must have the exact same attributes."
        ],
        "answer": 0,
        "solution": "Overlapping specialization allows an entity instance to be a member of more than one subclass simultaneously. In contrast, disjoint ({d}) requires mutual exclusivity.",
        "theorySummary": "EER constraints include Disjointness (Disjoint vs Overlap) and Completeness (Total vs Partial participation)."
    },
    {
        "id": "DDD-06",
        "paper": "2023 Final Examination",
        "questionNumber": 6,
        "topic": "Relational Synthesis: Candidate Key Derivation",
        "marks": 15.00,
        "difficulty": "Expert",
        "prompt": "Consider relation $R(A, B, C, D, E, F, G)$ with functional dependencies:\n$F = \\{ A \\rightarrow BC, \\quad B \\rightarrow D, \\quad C \\rightarrow EF, \\quad AC \\rightarrow G \\}$\n\nFind the candidate key for relation $R$ using the attribute closure method.",
        "type": "mcq",
        "options": [
            "A",
            "AB",
            "AC",
            "ABC"
        ],
        "answer": 0,
        "solution": "Compute A+: Start with {A}. A -> BC adds B, C -> {A, B, C}. B -> D adds D -> {A, B, C, D}. C -> EF adds E, F -> {A, B, C, D, E, F}. AC -> G adds G -> {A, B, C, D, E, F, G}. Since A+ contains all attributes, A is the unique Candidate Key.",
        "theorySummary": "If a single attribute's closure contains all attributes of R, that single attribute is a minimal candidate key and no composite key containing it can be minimal."
    },
    {
        "id": "DDD-07",
        "paper": "2023 Final Examination",
        "questionNumber": 7,
        "topic": "Normalization: Testing 3NF and BCNF Violations",
        "marks": 15.00,
        "difficulty": "Expert",
        "prompt": "For relation $R(A, B, C, D, E, F, G)$ with candidate key $A$ and functional dependencies:\n$A \\rightarrow BC, \\quad B \\rightarrow D, \\quad C \\rightarrow EF, \\quad AC \\rightarrow G$.\n\nIs relation $R$ in 3NF, and why?",
        "type": "mcq",
        "options": [
            "No, because B -> D and C -> EF represent transitive dependencies where the determinant is not a superkey and the right-hand side is not prime.",
            "Yes, because A is a candidate key.",
            "Yes, because all functional dependencies are non-trivial.",
            "No, because it violates 1NF atomicity."
        ],
        "answer": 0,
        "solution": "3NF requires that for every non-trivial X -> Y, X is a superkey OR Y is a prime attribute. In B -> D, B is not a superkey and D is not part of any candidate key (not prime). This is a transitive dependency violating 3NF.",
        "theorySummary": "2NF eliminates partial dependencies on composite keys. 3NF eliminates transitive dependencies (non-key determining non-key)."
    },
    {
        "id": "DDD-08",
        "paper": "2023 Final Examination",
        "questionNumber": 8,
        "topic": "SQL Server Security: Fixed Server Roles",
        "marks": 10.00,
        "difficulty": "Medium",
        "prompt": "In Microsoft SQL Server / T-SQL, which fixed server role should be assigned to an administrator who requires complete, unrestricted permissions across all databases and server configurations?",
        "type": "mcq",
        "options": [
            "sysadmin",
            "db_owner",
            "securityadmin",
            "serveradmin"
        ],
        "answer": 0,
        "solution": "sysadmin is the fixed server role that grants all privileges on the entire SQL Server instance. db_owner is a database-level role.",
        "theorySummary": "Server-level roles (sysadmin, securityadmin, serveradmin) govern instance-wide management, while Database roles (db_owner, db_datareader, db_datawriter) control specific databases."
    },
    {
        "id": "DDD-09",
        "paper": "2023 Final Examination",
        "questionNumber": 9,
        "topic": "SQL Queries: Aggregation with HAVING Clause",
        "marks": 12.00,
        "difficulty": "Hard",
        "prompt": "Which SQL clause is used to filter aggregated group results (e.g. showing only departments with more than 5 employees) after `GROUP BY` has grouped the rows?",
        "type": "mcq",
        "options": [
            "HAVING COUNT(*) > 5",
            "WHERE COUNT(*) > 5",
            "ORDER BY COUNT(*) > 5",
            "FILTER BY COUNT(*) > 5"
        ],
        "answer": 0,
        "solution": "WHERE filters individual rows before aggregation; HAVING filters groups after aggregation.",
        "theorySummary": "SQL execution order: FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY."
    },
    {
        "id": "DDD-10",
        "paper": "2022 Final Examination",
        "questionNumber": 10,
        "topic": "Lossless-Join Decomposition & Chase Test",
        "marks": 15.00,
        "difficulty": "Expert",
        "prompt": "A relation $R(A, B, C)$ is decomposed into $R_1(A, B)$ and $R_2(B, C)$. Under what functional dependency condition is this decomposition guaranteed to be LOSSLESS?",
        "type": "mcq",
        "options": [
            "Either B -> A or B -> C must hold in F+ (The common attribute B must be a candidate key for at least one decomposed relation).",
            "Both A -> B and C -> B must hold simultaneously.",
            "The intersection R1 ∩ R2 must equal the empty set.",
            "All functional dependencies must have only one attribute on each side."
        ],
        "answer": 0,
        "solution": "A binary decomposition of R into (R1, R2) is lossless if and only if (R1 ∩ R2) -> R1 or (R1 ∩ R2) -> R2 holds in F+. Here, R1 ∩ R2 = {B}.",
        "theorySummary": "Lossless join ensures that natural joining the decomposed relations reconstructs the original relation exactly without introducing spurious tuples."
    },
    {
        "id": "DDD-11",
        "paper": "Lockdown Compilation",
        "questionNumber": 11,
        "topic": "Serializability & Precedence Graphs",
        "marks": 15.00,
        "difficulty": "Expert",
        "prompt": "Given a schedule $S$ with transactions $T_1, T_2$: $S = r_1(X), \\; w_2(X), \\; w_1(X), \\; c_1, \\; c_2$. Is schedule $S$ conflict serializable?",
        "type": "mcq",
        "options": [
            "No, because there is a cycle in the precedence graph: r1(X) -> w2(X) creates edge T1 -> T2, and w2(X) -> w1(X) creates edge T2 -> T1.",
            "Yes, because both transactions commit.",
            "Yes, because all write operations are serialized.",
            "No, because transactions must execute on different data items."
        ],
        "answer": 0,
        "solution": "Conflicting operations on data item X: r1(X) precedes w2(X) => edge T1 -> T2. w2(X) precedes w1(X) => edge T2 -> T1. The precedence graph contains a cycle T1 <-> T2, so S is not conflict serializable.",
        "theorySummary": "Two operations conflict if they belong to different transactions, access the same item, and at least one is a write. A schedule is conflict serializable iff its precedence graph is acyclic."
    },
    {
        "id": "DDD-12",
        "paper": "Lockdown Compilation",
        "questionNumber": 12,
        "topic": "Deadlock Handling: Wait-Die vs Wound-Wait",
        "marks": 10.00,
        "difficulty": "Hard",
        "prompt": "In deadlock prevention based on timestamp ordering, how does the 'Wait-Die' non-preemptive scheme behave when an older transaction $T_O$ requests a lock held by a younger transaction $T_Y$?",
        "type": "mcq",
        "options": [
            "The older transaction TO is allowed to wait for TY.",
            "The older transaction TO dies (aborts and restarts).",
            "The younger transaction TY is immediately wounded (aborted).",
            "Both transactions are rolled back."
        ],
        "answer": 0,
        "solution": "Wait-Die: Older transaction can wait for younger (Old -> Young = wait). If young requests from old, young dies (Young -> Old = die).",
        "theorySummary": "Timestamp schemes prevent cycles: Wait-Die is non-preemptive (older waits, younger dies). Wound-Wait is preemptive (older wounds younger, younger waits)."
    },
    {
        "id": "DDD-13",
        "paper": "2021 Final Exam Answers",
        "questionNumber": 13,
        "topic": "Stored Procedures & Explicit Transaction Control",
        "marks": 10.00,
        "difficulty": "Medium",
        "prompt": "In an SQL stored procedure transferring funds between bank accounts, which statement should be placed inside the `CATCH` block to undo changes if an error occurs?",
        "type": "mcq",
        "options": [
            "ROLLBACK TRANSACTION",
            "COMMIT TRANSACTION",
            "DROP TRANSACTION",
            "SAVEPOINT FINISH"
        ],
        "answer": 0,
        "solution": "ROLLBACK TRANSACTION cancels all modifications made since BEGIN TRANSACTION, restoring database state to maintain Atomicity.",
        "theorySummary": "ACID Atomicity: All operations in a transaction succeed (COMMIT) or all are completely undone (ROLLBACK)."
    },
    {
        "id": "DDD-14",
        "paper": "2022 Final Examination",
        "questionNumber": 14,
        "topic": "Indexing: B+ Tree Index Characteristics",
        "marks": 8.00,
        "difficulty": "Medium",
        "prompt": "Why are B+ Tree index structures widely preferred over binary search trees for disk-based relational database management systems?",
        "type": "mcq",
        "options": [
            "High branching fanout minimizes tree height and disk I/O operations, and linked leaf nodes provide fast range scans.",
            "B+ trees require no disk space.",
            "B+ trees execute in O(1) constant time regardless of dataset size.",
            "B+ trees eliminate the need for primary keys."
        ],
        "answer": 0,
        "solution": "Each B+ tree node matches a disk block holding hundreds of keys, keeping tree depth shallow (3-4 levels) to minimize disk page reads. Doubly-linked leaf nodes enable linear range traversals.",
        "theorySummary": "B+ Tree is a self-balancing search tree where internal nodes store search keys as routers and leaf nodes store actual data pointers linked sequentially."
    },
    {
        "id": "DDD-15",
        "paper": "2024 Final Examination",
        "questionNumber": 15,
        "topic": "Referential Integrity: ON DELETE CASCADE",
        "marks": 8.00,
        "difficulty": "Medium",
        "prompt": "When creating a foreign key constraint with `ON DELETE CASCADE`, what occurs in the child table if a referenced row in the parent table is deleted?",
        "type": "mcq",
        "options": [
            "All referencing rows in the child table are automatically deleted.",
            "The deletion in the parent table is blocked with an integrity error.",
            "The foreign key values in the child table are set to NULL.",
            "The parent table row is retained as a tombstone."
        ],
        "answer": 0,
        "solution": "ON DELETE CASCADE propagates deletion from parent to all matching foreign key child records automatically.",
        "theorySummary": "Referential integrity actions: CASCADE (delete children), SET NULL (set child FK to null), RESTRICT/NO ACTION (reject deletion if children exist)."
    }
]

data["DDD"]["questions"].extend(dms_extra)

# =========================================================================
# ADDITIONAL SE QUESTIONS (Total will be 20)
# =========================================================================
se_extra = [
    {
        "id": "SE-05",
        "paper": "2024 June Final Exam",
        "questionNumber": 5,
        "topic": "UML Sequence Diagrams: Message Types & Fragments",
        "marks": 15.00,
        "difficulty": "Medium",
        "prompt": "In a UML 2.x Sequence Diagram, how is an asynchronous message visually distinguished from a synchronous message?",
        "type": "mcq",
        "options": [
            "Asynchronous has an open stick arrowhead (—>); synchronous has a solid filled arrowhead (—►).",
            "Asynchronous uses a dashed line; synchronous uses a solid line.",
            "Asynchronous has a circle at the end; synchronous has an arrow.",
            "Asynchronous messages cannot be drawn in sequence diagrams."
        ],
        "answer": 0,
        "solution": "UML standard: Synchronous calls (blocking) use a solid line with a filled arrowhead. Asynchronous signals (non-blocking) use a solid line with an open stick arrowhead. Reply messages use a dashed line with an open arrowhead.",
        "theorySummary": "Sequence diagrams model dynamic interaction over time. Lifelines represent participant objects; activation bars show execution duration; combined fragments (alt, opt, loop) express conditional logic."
    },
    {
        "id": "SE-06",
        "paper": "2024 June Final Exam",
        "questionNumber": 6,
        "topic": "UML Component Diagrams: Provided vs Required Interfaces",
        "marks": 15.00,
        "difficulty": "Hard",
        "prompt": "In the 2024 Final Exam Library System, component `UserVerification` offers the `iVerify` interface, while component `Registration` depends on it.\nHow are Provided and Required interfaces represented in UML Component notation?",
        "type": "mcq",
        "options": [
            "Provided interface is drawn as a ball / lollipop (—○); Required interface is drawn as a socket / cup (—⊃).",
            "Provided interface is drawn as a dashed box; Required is a solid diamond.",
            "Provided is a socket; Required is a lollipop.",
            "Both are drawn as solid rectangles."
        ],
        "answer": 0,
        "solution": "The ball-and-socket notation: 'Ball' (lollipop) represents an interface provided/realized by the component. 'Socket' (half-circle) represents an interface required/demanded by the client.",
        "theorySummary": "Component diagrams show software modularity and dependencies via well-defined provided and required interfaces."
    },
    {
        "id": "SE-07",
        "paper": "2024 June Final Exam",
        "questionNumber": 7,
        "topic": "Behavioral Design Patterns: Observer Pattern",
        "marks": 20.00,
        "difficulty": "Expert",
        "prompt": "In the 2024 Final Exam Question 4(a): A vehicle fleet monitoring system tracks metrics (speed, fuel, location). Multiple stakeholders (fleet managers, drivers) must be notified in real-time when metrics change or thresholds are exceeded, and new stakeholders will be added in the future.\n\nWhich design pattern is best suited for this requirement, and why?",
        "type": "mcq",
        "options": [
            "Observer Pattern: It defines a one-to-many dependency where multiple observers register and automatically receive updates when the vehicle subject changes state.",
            "Singleton Pattern: It ensures only one vehicle exists in memory.",
            "Adapter Pattern: It converts incompatible interfaces between trucks and cars.",
            "Decorator Pattern: It attaches graphical borders to fleet reports."
        ],
        "answer": 0,
        "solution": "The Observer pattern establishes a 1-to-many subscription mechanism: the Fleet Monitoring System acts as the Subject/Observable, notifying all registered Stakeholder Observers without tight coupling.",
        "theorySummary": "Observer pattern encapsulates publish-subscribe semantics, decoupling subjects from concrete observer implementations."
    },
    {
        "id": "SE-08",
        "paper": "2024 June Final Exam",
        "questionNumber": 8,
        "topic": "Structural Design Patterns: Facade Pattern",
        "marks": 15.00,
        "difficulty": "Hard",
        "prompt": "In the 2024 Final Exam Question 4(c), a class `RentalService` provides simplified methods like `rentMovie(customerId, title)` that internally coordinate multiple complex subsystems: `MovieDatabase.searchMovie()`, `CustomerDatabase.getRentalHistory()`, and `BillingSystem.charge()`.\n\nWhat design pattern is this?",
        "type": "mcq",
        "options": [
            "Facade Pattern: Provides a unified, high-level interface that makes complex subsystem classes easier to use.",
            "Proxy Pattern: Controls access to remote database instances.",
            "Composite Pattern: Builds tree hierarchies of rental items.",
            "Bridge Pattern: Decouples abstraction from implementation."
        ],
        "answer": 0,
        "solution": "The Facade pattern provides a simplified interface to a library, framework, or complex set of classes, wrapping subsystem interactions behind a single clean entry point.",
        "theorySummary": "Facade shields clients from subsystem complexities and promotes loose coupling."
    },
    {
        "id": "SE-09",
        "paper": "2024 June Final Exam",
        "questionNumber": 9,
        "topic": "State Machine Triggers",
        "marks": 10.00,
        "difficulty": "Hard",
        "prompt": "In a UML State Machine diagram, which trigger type occurs upon the satisfaction of a Boolean expression or variable change (e.g. `when(temperature > 100)`)?",
        "type": "mcq",
        "options": [
            "Change Trigger",
            "Call Trigger",
            "Signal Trigger",
            "Time Trigger"
        ],
        "answer": 0,
        "solution": "Change trigger evaluates a Boolean condition continuously until it becomes true. Call trigger is an operation invocation. Signal trigger is receipt of an asynchronous signal. Time trigger specifies duration expiration (after/at).",
        "theorySummary": "Four types of UML state triggers: Signal (async event), Call (operation dispatch), Time (after(5s)), Change (when(condition))."
    },
    {
        "id": "SE-10",
        "paper": "2024 June Final Exam",
        "questionNumber": 10,
        "topic": "Software Quality: Verification vs Validation",
        "marks": 8.00,
        "difficulty": "Medium",
        "prompt": "What is the classic distinction between Verification and Validation in software testing?",
        "type": "mcq",
        "options": [
            "Verification asks 'Are we building the product right?' (conformance to specs); Validation asks 'Are we building the right product?' (satisfying user needs).",
            "Verification is done by clients; Validation is done by developers.",
            "Verification involves automated tests; Validation involves manual testing only.",
            "Verification happens only in production; Validation happens in development."
        ],
        "answer": 0,
        "solution": "Boehm's famous definitions: Verification checks whether artifacts correctly satisfy conditions imposed by prior specifications. Validation ensures the software meets real operational requirements and customer expectations.",
        "theorySummary": "Verification = reviews, walkthroughs, static analysis, unit tests against specs. Validation = acceptance testing, beta tests with actual users."
    },
    {
        "id": "SE-11",
        "paper": "2022 Final Exam",
        "questionNumber": 11,
        "topic": "Creational Patterns: Singleton Pattern",
        "marks": 10.00,
        "difficulty": "Hard",
        "prompt": "In Java, what is the purpose of the `volatile` keyword when implementing the thread-safe Double-Checked Locking Singleton pattern?",
        "type": "mcq",
        "options": [
            "It prevents CPU instruction reordering so that other threads cannot observe a partially initialized Singleton instance.",
            "It makes the Singleton class immutable.",
            "It automatically serializes the instance to disk.",
            "It prevents garbage collection of the instance."
        ],
        "answer": 0,
        "solution": "Without volatile, the compiler or CPU can reorder instructions (allocating memory, assigning pointer, then running constructor), allowing another thread to see a non-null but uninitialized object.",
        "theorySummary": "Singleton pattern guarantees a class has only one instance and provides a global access point. Thread safety requires double-checked locking with volatile."
    },
    {
        "id": "SE-12",
        "paper": "2022 Final Exam",
        "questionNumber": 12,
        "topic": "Creational Patterns: Factory Method vs Abstract Factory",
        "marks": 12.00,
        "difficulty": "Hard",
        "prompt": "What is the primary architectural difference between the Factory Method pattern and the Abstract Factory pattern?",
        "type": "mcq",
        "options": [
            "Factory Method relies on inheritance to create one product; Abstract Factory uses object composition to create families of related products.",
            "Factory Method can only create singletons.",
            "Abstract Factory does not use interfaces.",
            "Factory Method is behavioral; Abstract Factory is structural."
        ],
        "answer": 0,
        "solution": "Factory Method defines an interface for creating a single object, letting subclasses decide which class to instantiate. Abstract Factory provides an interface for creating families of related or dependent objects.",
        "theorySummary": "Factory Method: single product via subclass override. Abstract Factory: family of distinct products created via factory composition."
    },
    {
        "id": "SE-13",
        "paper": "2022 May Revision",
        "questionNumber": 13,
        "topic": "Structural Patterns: Decorator Pattern",
        "marks": 12.00,
        "difficulty": "Hard",
        "prompt": "Which design pattern attaches additional responsibilities to an object dynamically at runtime as an alternative to subclassing?",
        "type": "mcq",
        "options": [
            "Decorator Pattern",
            "Proxy Pattern",
            "Composite Pattern",
            "Flyweight Pattern"
        ],
        "answer": 0,
        "solution": "The Decorator pattern wraps an object in an enclosing decorator class conforming to the same interface, layering new behaviors dynamically without class explosion.",
        "theorySummary": "Decorator follows Open-Closed Principle: open for extension, closed for modification. Examples include Java IO Streams (e.g. BufferedReader(new FileReader))."
    },
    {
        "id": "SE-14",
        "paper": "2022 May Revision",
        "questionNumber": 14,
        "topic": "Structural Patterns: Adapter Pattern",
        "marks": 10.00,
        "difficulty": "Medium",
        "prompt": "An existing third-party logging library has method `logMessage(int priority, String msg)`, but your application's `ILogger` interface requires `info(String msg)`. Which pattern bridges this incompatibility?",
        "type": "mcq",
        "options": [
            "Adapter Pattern (Wrapper)",
            "Bridge Pattern",
            "Strategy Pattern",
            "Template Method Pattern"
        ],
        "answer": 0,
        "solution": "The Adapter pattern converts the interface of a class into another interface clients expect, enabling classes with incompatible interfaces to work together.",
        "theorySummary": "Adapter pattern matches two existing incompatible interfaces via Object Adapter (composition) or Class Adapter (multiple inheritance)."
    },
    {
        "id": "SE-15",
        "paper": "2018 Model Paper",
        "questionNumber": 15,
        "topic": "Agile Methodologies: Scrum Framework",
        "marks": 8.00,
        "difficulty": "Medium",
        "prompt": "In the Scrum framework, who is solely responsible for prioritizing and managing the items in the Product Backlog?",
        "type": "mcq",
        "options": [
            "Product Owner",
            "Scrum Master",
            "Development Team Lead",
            "Project Stakeholder"
        ],
        "answer": 0,
        "solution": "The Product Owner has sole authority over the content, ordering, and prioritization of the Product Backlog.",
        "theorySummary": "Scrum roles: Product Owner (manages product backlog and business value), Scrum Master (servant-leader removing impediments), Developers (deliver increments)."
    }
]

data["SE"]["questions"].extend(se_extra)

with open("/home/dulith/Projects/net_exam_emulator/src/data/quizzes.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("Enrichment complete! Final counts:")
for k, v in data.items():
    print(f" - {k}: {len(v['questions'])} total questions")
