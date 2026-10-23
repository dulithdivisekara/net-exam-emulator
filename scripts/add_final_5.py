import json

with open("/home/dulith/Projects/net_exam_emulator/src/data/quizzes.json", "r", encoding="utf-8") as f:
    data = json.load(f)

aiml_5 = [
    {
        "id": "AIML-16",
        "paper": "Deep Learning Structure Revision",
        "questionNumber": 16,
        "topic": "Vanishing Gradient Problem in Deep Networks",
        "marks": 10.00,
        "difficulty": "Expert",
        "prompt": "Why does the standard Sigmoid activation function $\\sigma(z) = \\frac{1}{1 + e^{-z}}$ cause the Vanishing Gradient problem during backpropagation in deep neural networks?",
        "type": "mcq",
        "options": [
            "The derivative of Sigmoid is bounded by a maximum of 0.25 (when z = 0). Multiplying many fractions <= 0.25 through multiple layers drives gradients exponentially toward 0.",
            "Sigmoid values can become negative, causing calculations to abort.",
            "Sigmoid functions cannot be computed on modern GPUs.",
            "The derivative is always greater than 1, causing exploding gradients."
        ],
        "answer": 0,
        "solution": "dσ/dz = σ(z)(1 - σ(z)). The maximum value of this derivative is 0.25 at z = 0. In deep networks, the chain rule multiplies these gradients across layers, leading to near-zero gradients at early layers.",
        "theorySummary": "Vanishing gradients prevent early layers from learning effectively. Non-saturating activations like ReLU and Residual Connections (ResNets) solve this."
    },
    {
        "id": "AIML-17",
        "paper": "2024 Final Revision Session",
        "questionNumber": 17,
        "topic": "Evaluation Metrics: ROC Curve and AUC",
        "marks": 8.00,
        "difficulty": "Hard",
        "prompt": "In a Receiver Operating Characteristic (ROC) curve, what are the axes plotted, and what does an Area Under the Curve (AUC) of 0.5 represent?",
        "type": "mcq",
        "options": [
            "Y-axis: True Positive Rate (Sensitivity); X-axis: False Positive Rate (1 - Specificity). An AUC of 0.5 indicates random guessing performance.",
            "Y-axis: Precision; X-axis: Recall. AUC of 0.5 indicates perfect performance.",
            "Y-axis: Accuracy; X-axis: Loss. AUC of 0.5 represents a balanced dataset.",
            "Y-axis: Training error; X-axis: Validation error."
        ],
        "answer": 0,
        "solution": "The ROC curve plots TPR vs FPR across all classification thresholds. An AUC of 1.0 is perfect; 0.5 represents a worthless classifier no better than flipping a coin.",
        "theorySummary": "ROC-AUC evaluates ranking quality independently of classification threshold and class imbalance."
    },
    {
        "id": "AIML-18",
        "paper": "2024 Final Revision Session",
        "questionNumber": 18,
        "topic": "Regularization: L1 (Lasso) vs L2 (Ridge)",
        "marks": 10.00,
        "difficulty": "Hard",
        "prompt": "Why does L1 regularization (Lasso: penalty $\\lambda \\sum |w_i|$) produce sparse models (setting some weight coefficients exactly to zero), whereas L2 regularization (Ridge: penalty $\\lambda \\sum w_i^2$) does not?",
        "type": "mcq",
        "options": [
            "The L1 diamond-shaped constraint boundary has sharp corners along the axes, where contours of the objective function frequently intersect at w_i = 0.",
            "L1 regularization uses smaller learning rates.",
            "L2 regularization eliminates more features than L1.",
            "L1 regularization is computationally impossible to solve."
        ],
        "answer": 0,
        "solution": "The geometric contour of the L1 penalty |w1| + |w2| <= t is a diamond with corners on axes, causing intersections where non-critical weights become exactly 0 (performing automatic feature selection).",
        "theorySummary": "L1 (Lasso) yields sparse models and feature selection. L2 (Ridge) shrinks weights smoothly toward zero without setting them exactly to zero."
    },
    {
        "id": "AIML-19",
        "paper": "Deep Learning Structure Revision",
        "questionNumber": 19,
        "topic": "Multi-Class Classification: Softmax Output",
        "marks": 10.00,
        "difficulty": "Hard",
        "prompt": "A neural network's final output layer produces unnormalized logits: $z_1 = 1.0, z_2 = 2.0, z_3 = 3.0$.\n\nCalculate the Softmax probability for class 3: $P(y = 3) = \\frac{e^{z_3}}{\\sum_{j=1}^3 e^{z_j}}$.\n(Given: $e^1 \\approx 2.72, e^2 \\approx 7.39, e^3 \\approx 20.09$).",
        "type": "mcq",
        "options": [
            "0.665",
            "0.333",
            "0.245",
            "0.500"
        ],
        "answer": 0,
        "solution": "Sum of exponentials = 2.718 + 7.389 + 20.086 = 30.193. Softmax(z3) = 20.086 / 30.193 = 0.665 (66.5%).",
        "theorySummary": "Softmax transforms K unnormalized real scores into a valid probability distribution where each p_i in (0, 1) and Σ p_i = 1."
    },
    {
        "id": "AIML-20",
        "paper": "2024 Final Revision Session",
        "questionNumber": 20,
        "topic": "Bias-Variance Tradeoff & Model Complexity",
        "marks": 8.00,
        "difficulty": "Medium",
        "prompt": "Which of the following conditions characterizes a machine learning model suffering from HIGH VARIANCE (Overfitting)?",
        "type": "mcq",
        "options": [
            "Near-zero training error combined with significantly higher error on the validation/test set.",
            "High error on both training data and validation data.",
            "The model is too simple to capture underlying patterns.",
            "The model's predictions never change across different training subsets."
        ],
        "answer": 0,
        "solution": "High variance means the model fits training data noise too closely, performing exceptionally on training data but generalizing poorly to unseen validation data.",
        "theorySummary": "Total Error = Bias² + Variance + Irreducible Error. High Bias = underfitting (oversimplified model). High Variance = overfitting (memorizing training noise)."
    }
]

ddd_5 = [
    {
        "id": "DDD-16",
        "paper": "2023 Final Examination",
        "questionNumber": 16,
        "topic": "SQL Window Functions: ROW_NUMBER vs RANK",
        "marks": 10.00,
        "difficulty": "Hard",
        "prompt": "In SQL, given three students tied with an equal exam mark of 85 at the top, how do `ROW_NUMBER()`, `RANK()`, and `DENSE_RANK()` assign rank values ordered descending?",
        "type": "mcq",
        "options": [
            "ROW_NUMBER assigns 1, 2, 3; RANK assigns 1, 1, 1 (next is 4); DENSE_RANK assigns 1, 1, 1 (next is 2).",
            "All three functions produce the exact same sequence 1, 2, 3.",
            "RANK assigns 1, 2, 3; DENSE_RANK assigns 1, 1, 1 (next is 4).",
            "ROW_NUMBER cannot be used with ORDER BY."
        ],
        "answer": 0,
        "solution": "ROW_NUMBER assigns unique sequential integers. RANK assigns identical ranks to ties and skips subsequent numbers. DENSE_RANK assigns identical ranks to ties without skipping subsequent numbers.",
        "theorySummary": "Window functions compute values across a set of table rows related to the current row without collapsing rows like GROUP BY."
    },
    {
        "id": "DDD-17",
        "paper": "Lockdown Compilation",
        "questionNumber": 17,
        "topic": "Multi-Valued Dependencies & Fourth Normal Form (4NF)",
        "marks": 12.00,
        "difficulty": "Expert",
        "prompt": "Under what condition does a relation $R$ violate Fourth Normal Form (4NF)?",
        "type": "mcq",
        "options": [
            "When R contains a non-trivial multi-valued dependency X ->> Y where X is NOT a superkey.",
            "When R has a transitive functional dependency.",
            "When R has composite foreign keys.",
            "When R contains NULL values."
        ],
        "answer": 0,
        "solution": "A relation is in 4NF if it is in BCNF and for every non-trivial multi-valued dependency X ->> Y, X is a superkey.",
        "theorySummary": "4NF addresses multi-valued dependencies where two independent 1-to-many relationships are incorrectly modeled in a single table, causing tuple proliferation."
    },
    {
        "id": "DDD-18",
        "paper": "2022 Final Examination",
        "questionNumber": 18,
        "topic": "Concurrency Control: Lock Conversions",
        "marks": 10.00,
        "difficulty": "Hard",
        "prompt": "In multi-granularity locking, what lock conversion is required when a transaction reading a record decides to update it?",
        "type": "mcq",
        "options": [
            "Upgrade from a Shared Lock (S) to an Exclusive Lock (X)",
            "Downgrade from an Exclusive Lock (X) to a Shared Lock (S)",
            "Release the lock immediately before writing",
            "Acquire an Intent Shared Lock (IS)"
        ],
        "answer": 0,
        "solution": "Upgrading converts a Shared (read-only) lock into an Exclusive (read-write) lock. If another transaction holds an S-lock on the same item, the upgrading transaction must wait.",
        "theorySummary": "Lock upgrading (S -> X) occurs during the growing phase; lock downgrading (X -> S) can occur during the shrinking phase."
    },
    {
        "id": "DDD-19",
        "paper": "2021 Final Exam Answers",
        "questionNumber": 19,
        "topic": "Database Recovery: Write-Ahead Logging (WAL)",
        "marks": 10.00,
        "difficulty": "Hard",
        "prompt": "What is the core rule of Write-Ahead Logging (WAL) in database recovery protocols?",
        "type": "mcq",
        "options": [
            "The log record for an update must be flushed to stable disk storage BEFORE the corresponding database page is written to disk.",
            "Data pages must be written to disk before the log record.",
            "Logs are only written after the transaction commits.",
            "Disk caches must be disabled entirely."
        ],
        "answer": 0,
        "solution": "WAL ensures Durability and Atomicity: before any dirty database buffer page overwrites existing disk data, the corresponding undo/redo log records must already reside safely on non-volatile storage.",
        "theorySummary": "WAL protocol guarantees that if a crash occurs at any moment, uncommitted updates can be UNDONE and committed updates can be REDONE using the disk log."
    },
    {
        "id": "DDD-20",
        "paper": "2024 Final Examination",
        "questionNumber": 20,
        "topic": "SQL Subqueries: NOT IN vs NOT EXISTS with NULLs",
        "marks": 12.00,
        "difficulty": "Expert",
        "prompt": "Why can `WHERE column_id NOT IN (SELECT foreign_id FROM other_table)` return ZERO rows if `other_table` contains even a single NULL value in `foreign_id`?",
        "type": "mcq",
        "options": [
            "In three-valued logic, `x NOT IN (1, 2, NULL)` evaluates to `UNKNOWN`, which is treated as FALSE in WHERE clauses.",
            "SQL aborts subqueries that encounter NULLs.",
            "NOT IN automatically converts NULL to zero.",
            "NOT IN requires unique non-null indexes to function."
        ],
        "answer": 0,
        "solution": "`x NOT IN (val, NULL)` is equivalent to `x != val AND x != NULL`. Since `x != NULL` evaluates to UNKNOWN, `TRUE AND UNKNOWN` is UNKNOWN. A WHERE clause requires TRUE to output rows. Using `NOT EXISTS` avoids this pitfall.",
        "theorySummary": "SQL three-valued logic (TRUE, FALSE, UNKNOWN) makes NOT IN dangerous when nullable columns are involved. NOT EXISTS uses two-valued logic and is NULL-safe."
    }
]

se_5 = [
    {
        "id": "SE-16",
        "paper": "2024 June Final Exam",
        "questionNumber": 16,
        "topic": "Software Architecture: Microservices vs Monolith",
        "marks": 12.00,
        "difficulty": "Hard",
        "prompt": "Which of the following is a recognized advantage of a Microservices Architecture over a Monolithic Architecture?",
        "type": "mcq",
        "options": [
            "Independent deployability and granular scalability of individual business capabilities using heterogeneous technology stacks.",
            "Zero network latency between inter-service communications.",
            "Simpler transactional consistency and distributed debugging.",
            "Elimination of API gateways and load balancers."
        ],
        "answer": 0,
        "solution": "Microservices isolate services along business domain boundaries, allowing independent scaling, autonomous team deployments, and polyglot tech stacks.",
        "theorySummary": "Microservices trade local complexity for operational/network complexity (distributed data management, eventual consistency, network latency)."
    },
    {
        "id": "SE-17",
        "paper": "2024 June Final Exam",
        "questionNumber": 17,
        "topic": "UML Class Diagrams: Association vs Aggregation vs Composition",
        "marks": 12.00,
        "difficulty": "Hard",
        "prompt": "In UML Class modeling, how is Composition distinguished from Aggregation?",
        "type": "mcq",
        "options": [
            "Composition represents a strong 'part-of' relationship with coincident lifetime (represented by a filled black diamond); if the whole is destroyed, the parts are destroyed.",
            "Aggregation has coincident lifetime; Composition does not.",
            "Composition is represented by a hollow diamond.",
            "There is no difference between Aggregation and Composition."
        ],
        "answer": 0,
        "solution": "Composition (solid diamond): The part cannot exist without the whole (e.g. Order and OrderLine). Aggregation (hollow diamond): The part can exist independently of the whole (e.g. Department and Employee).",
        "theorySummary": "Relationships in UML: Dependency (uses-a, dashed arrow) < Association (has-a) < Aggregation (shared whole-part, hollow diamond) < Composition (composite whole-part, filled diamond) < Generalization (is-a, triangle)."
    },
    {
        "id": "SE-18",
        "paper": "2022 Final Exam",
        "questionNumber": 18,
        "topic": "Software Quality Attributes (ISO/IEC 25010)",
        "marks": 8.00,
        "difficulty": "Medium",
        "prompt": "According to the ISO/IEC 25010 software product quality model, 'Mean Time to Failure (MTTF)' and 'Fault Tolerance' are sub-characteristics of which quality attribute?",
        "type": "mcq",
        "options": [
            "Reliability",
            "Performance Efficiency",
            "Maintainability",
            "Portability"
        ],
        "answer": 0,
        "solution": "Reliability comprises Maturity, Availability, Fault Tolerance, and Recoverability.",
        "theorySummary": "ISO 25010 defines 8 quality characteristics: Functional Suitability, Performance Efficiency, Compatibility, Usability, Reliability, Security, Maintainability, and Portability."
    },
    {
        "id": "SE-19",
        "paper": "2022 May Revision",
        "questionNumber": 19,
        "topic": "Refactoring Techniques & Code Smells",
        "marks": 10.00,
        "difficulty": "Medium",
        "prompt": "Which refactoring technique is most appropriate when a single method has grown excessively long and performs multiple distinct tasks with high internal cohesion within each segment?",
        "type": "mcq",
        "options": [
            "Extract Method",
            "Inline Method",
            "Introduce Foreign Method",
            "Pull Up Method"
        ],
        "answer": 0,
        "solution": "Extract Method isolates contiguous code doing one specific thing into a well-named private method, improving readability, testability, and reuse.",
        "theorySummary": "Refactoring improves internal structure without altering external observable behavior. Common techniques: Extract Method, Extract Class, Replace Conditional with Polymorphism."
    },
    {
        "id": "SE-20",
        "paper": "2018 Model Paper",
        "questionNumber": 20,
        "topic": "Requirements Engineering: Functional vs Non-Functional",
        "marks": 8.00,
        "difficulty": "Medium",
        "prompt": "Which of the following requirements represents a NON-FUNCTIONAL requirement?",
        "type": "mcq",
        "options": [
            "The system must process and return search results in under 500 milliseconds for 99% of requests with 1,000 concurrent users.",
            "The user can reset their account password via email.",
            "The administrator can export student records as a CSV file.",
            "The patient can book an appointment with a doctor."
        ],
        "answer": 0,
        "solution": "Functional requirements define what the system must do (features, services). Non-functional requirements define how well it must do it (performance, security, scalability, constraints).",
        "theorySummary": "Non-functional requirements (NFRs) specify criteria that judge the operation of a system rather than specific behaviors."
    }
]

data["AIML"]["questions"].extend(aiml_5)
data["DDD"]["questions"].extend(ddd_5)
data["SE"]["questions"].extend(se_5)

with open("/home/dulith/Projects/net_exam_emulator/src/data/quizzes.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("Final dataset compilation:")
for k, v in data.items():
    print(f" - {k} ({v['title']}): {len(v['questions'])} questions")
