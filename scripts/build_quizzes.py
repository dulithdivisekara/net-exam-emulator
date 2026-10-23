import json
import os

modules_data = {
    "PAS": {
        "id": "PAS",
        "code": "IT2110 / IT2120",
        "title": "Probability and Statistics",
        "semester": "Year 2, Semester 1",
        "description": "Computer-Based Exam questions, hypothesis testing, confidence intervals, distributions, outlier analysis, Chi-Square, and time series.",
        "icon": "chart-scatter",
        "accent": "#0d9488",
        "papers": ["Computer-Based Exam (Lab Replica)", "Final Exam Past Papers Compilation", "Lockdown Exam Revision"],
        "questions": []
    },
    "AIML": {
        "id": "AIML",
        "code": "IT2011",
        "title": "Artificial Intelligence and Machine Learning",
        "semester": "Year 2, Semester 1",
        "description": "Supervised/unsupervised learning, Gini index, K-Means clustering, evaluation metrics, deep neural network structures, and backpropagation.",
        "icon": "brain",
        "accent": "#7c3aed",
        "papers": ["2024 Final Revision Session", "Deep Learning Structure Revision", "Past Papers MCQ & Essay"],
        "questions": []
    },
    "DDD": {
        "id": "DDD",
        "code": "IT2040 / IT2140",
        "title": "Database Design and Development",
        "semester": "Year 2, Semester 1",
        "description": "EER to relational mapping, functional dependencies, 2NF/3NF/BCNF normalization, transaction ACID, 2PL concurrency, and SQL procedures.",
        "icon": "database",
        "accent": "#2563eb",
        "papers": ["2024 Final Examination", "2023 Final Examination", "2022 Final Examination", "Lockdown Compilation"],
        "questions": []
    },
    "SE": {
        "id": "SE",
        "code": "IT2020 / SE2030",
        "title": "Software Engineering",
        "semester": "Year 2, Semester 1",
        "description": "Use case robustness analysis (B-C-E), GoF design patterns, black-box & white-box testing, cyclomatic complexity, and state machines.",
        "icon": "code-2",
        "accent": "#ea580c",
        "papers": ["2024 June Final Exam", "2022 Final Exam", "2022 May Revision", "2018 Model Paper"],
        "questions": []
    }
}

# -------------------------------------------------------------
# 1. PAS QUESTIONS (Including all unique Computer-Based Exam photos)
# -------------------------------------------------------------

modules_data["PAS"]["questions"] = [
    {
        "id": "PAS-CBE-01",
        "source": "Computer_Based_Exam/Question_01.jpg",
        "paper": "Computer-Based Exam (Lab Replica)",
        "questionNumber": 3,
        "topic": "Confidence Intervals for One Mean (Small Sample)",
        "marks": 12.00,
        "difficulty": "Hard",
        "prompt": "A company monitors the average response time of its cloud servers to ensure optimal performance for users. The response time is measured in seconds, and the company wants to estimate the true mean response time of all servers. A random sample of 25 servers shows an average response time of 1.75 seconds with a standard deviation of 0.25 seconds. Construct a 95% confidence interval for the true mean response time.",
        "type": "multipart",
        "subquestions": [
            {
                "id": "sq1",
                "label": "1. Lower limit equation:",
                "type": "dropdown",
                "options": [
                    "x̄ - t(α/2, n-1) * (s / √n)",
                    "x̄ + t(α/2, n-1) * (s / √n)",
                    "x̄ - z(α/2) * (σ / √n)",
                    "x̄ + z(α/2) * (s / √n)"
                ],
                "answer": "x̄ - t(α/2, n-1) * (s / √n)",
                "hint": "Since population standard deviation σ is unknown and n = 25 < 30, the Student's t-distribution with df = 24 is used."
            },
            {
                "id": "sq2",
                "label": "2. Upper limit equation:",
                "type": "dropdown",
                "options": [
                    "x̄ + t(α/2, n-1) * (s / √n)",
                    "x̄ - t(α/2, n-1) * (s / √n)",
                    "x̄ + z(α/2) * (σ / √n)",
                    "x̄ - z(α/2) * (s / √n)"
                ],
                "answer": "x̄ + t(α/2, n-1) * (s / √n)",
                "hint": "Upper limit adds the margin of error to the sample mean."
            },
            {
                "id": "sq3",
                "label": "3. Critical value:",
                "instruction": "(Type your answer here and keep the answer with all decimal places. Do not mention the sign. Mention only the number)",
                "type": "text",
                "answer": "2.0639",
                "acceptedAnswers": ["2.0639", "2.064", "2.06"],
                "hint": "For 95% confidence, α = 0.05. Two-tailed tail area = 0.025 with degrees of freedom df = 25 - 1 = 24. From t-tables, t_0.025,24 = 2.0639."
            },
            {
                "id": "sq4",
                "label": "4. Lower limit value:",
                "instruction": "(Type your answer here and keep the answer with four decimal places)",
                "type": "text",
                "answer": "1.6468",
                "acceptedAnswers": ["1.6468", "1.6467", "1.647"],
                "hint": "Lower = 1.75 - 2.0639 * (0.25 / 5) = 1.75 - 0.103195 = 1.6468."
            },
            {
                "id": "sq5",
                "label": "5. Upper limit value:",
                "instruction": "(Type your answer here and keep the answer with four decimal places)",
                "type": "text",
                "answer": "1.8532",
                "acceptedAnswers": ["1.8532", "1.8533", "1.853"],
                "hint": "Upper = 1.75 + 2.0639 * (0.25 / 5) = 1.75 + 0.103195 = 1.8532."
            },
            {
                "id": "sq6",
                "label": "6. Lets assume that lower limit is a and upper limit is b. Interpret the confidence interval:",
                "type": "radio",
                "options": [
                    "We are 95% confident that the true mean response time will be between a and b",
                    "We are 5% confident that the true mean response time will be between a and b",
                    "We are 2.5% confident that the true mean response time will not be between a and b",
                    "We are 95% confident that the true mean response time will not be between a and b",
                    "We are 2.5% confident that the true mean response time will be between a and b"
                ],
                "answer": 0,
                "hint": "A 95% confidence interval means we are 95% confident that the unknown true population parameter μ lies between the calculated lower and upper bounds."
            }
        ],
        "theorySummary": "When estimating an unknown population mean μ from a small sample (n < 30) with unknown population variance σ², we apply Student's t-distribution with ν = n - 1 degrees of freedom. The margin of error is E = t_{α/2, n-1} * (s / √n)."
    },
    {
        "id": "PAS-CBE-02",
        "source": "Computer_Based_Exam/Question_08.jpg",
        "paper": "Computer-Based Exam (Lab Replica)",
        "questionNumber": 2,
        "topic": "One-Sample Hypothesis Testing (Left-Tailed Z-Test)",
        "marks": 14.00,
        "difficulty": "Expert",
        "prompt": "A software company claims that its new algorithm reduces the average response time of its server from the current average of 250 milliseconds. A random sample of 40 server response times after implementing the new algorithm has a mean response time of 245 milliseconds with a standard deviation of 18 milliseconds. The company wants to test whether the new algorithm has significantly reduced the server response time than 250 milliseconds. Test the company's claim at 5% level of significance.",
        "type": "multipart",
        "subquestions": [
            {
                "id": "sq1",
                "label": "1. What is the hypothesis?",
                "type": "dropdown",
                "options": [
                    "H0: μ ≥ 250 vs H1: μ < 250",
                    "H0: μ = 250 vs H1: μ ≠ 250",
                    "H0: μ ≤ 250 vs H1: μ > 250",
                    "H0: μ = 245 vs H1: μ < 245"
                ],
                "answer": "H0: μ ≥ 250 vs H1: μ < 250",
                "hint": "The claim is that the algorithm reduces response time (< 250). The research hypothesis H1 takes the strict inequality (< 250)."
            },
            {
                "id": "sq2",
                "label": "2. What is the distribution of test statistic?",
                "type": "dropdown",
                "options": [
                    "Standard Normal distribution",
                    "Student's t-distribution with 39 df",
                    "Chi-Square distribution with 40 df",
                    "F-distribution"
                ],
                "answer": "Standard Normal distribution",
                "hint": "Since sample size n = 40 ≥ 30, the Central Limit Theorem ensures that the sample mean distribution is approximately normal, and Z-test is applicable."
            },
            {
                "id": "sq3",
                "label": "3. What is the critical value?",
                "instruction": "(Type your answer here and keep the answer with two decimal places. Mention only the number)",
                "type": "text",
                "answer": "1.65",
                "acceptedAnswers": ["1.65", "1.64", "1.645"],
                "hint": "For a left-tailed test at α = 0.05, Z_0.05 = 1.645 ≈ 1.65 (magnitude)."
            },
            {
                "id": "sq4",
                "label": "4. Select correct rejection region for the test.",
                "type": "dropdown",
                "options": [
                    "Z_calc < -1.645 (or Z < -Z_0.05)",
                    "Z_calc > 1.645",
                    "Z_calc < -1.96 or Z_calc > 1.96",
                    "Z_calc > 1.96"
                ],
                "answer": "Z_calc < -1.645 (or Z < -Z_0.05)",
                "hint": "Because H1 has '<', the entire rejection area lies in the extreme left tail."
            },
            {
                "id": "sq5",
                "label": "5. What is the test statistic value?",
                "instruction": "(Type your answer here and round off the answer up to four decimal places)",
                "type": "text",
                "answer": "-1.7568",
                "acceptedAnswers": ["-1.7568", "-1.7569", "-1.76"],
                "hint": "Z = (245 - 250) / (18 / √40) = -5 / 2.84605 = -1.7568."
            },
            {
                "id": "sq6",
                "label": "6. Give the scientific conclusion:",
                "type": "dropdown",
                "options": [
                    "Reject H0 at 5% significance level since Z_calc falls in the rejection region",
                    "Fail to reject H0 at 5% significance level since Z_calc does not fall in the rejection region",
                    "Reject H1 at 5% significance level",
                    "Accept H0 as proven true"
                ],
                "answer": "Reject H0 at 5% significance level since Z_calc falls in the rejection region",
                "hint": "-1.7568 < -1.645, which lies inside the critical rejection zone."
            },
            {
                "id": "sq7",
                "label": "7. What is the general conclusion?",
                "type": "dropdown",
                "options": [
                    "There is sufficient evidence to conclude that the new algorithm significantly reduces the server response time",
                    "There is insufficient evidence to conclude that the new algorithm reduces response time",
                    "The new algorithm has no effect on server response time",
                    "The server response time has increased significantly"
                ],
                "answer": "There is sufficient evidence to conclude that the new algorithm significantly reduces the server response time",
                "hint": "Rejecting H0 means supporting the company's research claim at the 5% level."
            }
        ],
        "theorySummary": "Hypothesis testing: Formulate H0 and H1. Determine test statistic Z = (X̄ - μ0)/(s/√n). Compare with critical value -Z_α. If Z_calc < -Z_α, reject H0."
    },
    {
        "id": "PAS-CBE-03",
        "source": "Computer_Based_Exam/Question_11.jpg",
        "paper": "Computer-Based Exam (Lab Replica)",
        "questionNumber": 4,
        "topic": "Descriptive Statistics, Quartiles, and Outlier Analysis",
        "marks": 20.00,
        "difficulty": "Hard",
        "prompt": "Consider the following set of execution times (in milliseconds) for different algorithms on various datasets:\n26, 32, 45, 32, 24, 29, 23, 33, 43, 37, 15, 32, 22, 52, 27, 19, 24, 35, 43, 32, 41, 35, 19, 32, 34, 29, 37, 34, 34, 49, 23\n(Type your answers within the given spaces except for part 3)",
        "type": "multipart",
        "subquestions": [
            {
                "id": "sq1_1",
                "label": "1.1 Mode:",
                "instruction": "(Keep all decimal places in the answer)",
                "type": "text",
                "answer": "32",
                "acceptedAnswers": ["32"],
                "hint": "Value 32 occurs 5 times, which is the highest frequency."
            },
            {
                "id": "sq1_2",
                "label": "1.2 Q1 (First quartile):",
                "instruction": "(Keep all decimal places in the answer)",
                "type": "text",
                "answer": "24",
                "acceptedAnswers": ["24"],
                "hint": "For N = 31 sorted data, position = 0.25 * (31 + 1) = 8th value = 24."
            },
            {
                "id": "sq1_3",
                "label": "1.3 Median:",
                "instruction": "(Keep all decimal places in the answer)",
                "type": "text",
                "answer": "32",
                "acceptedAnswers": ["32"],
                "hint": "The 16th value in the sorted list of 31 items is 32."
            },
            {
                "id": "sq1_4",
                "label": "1.4 Q3 (Third quartile):",
                "instruction": "(Keep all decimal places in the answer)",
                "type": "text",
                "answer": "37",
                "acceptedAnswers": ["37"],
                "hint": "Position = 0.75 * (31 + 1) = 24th value = 37."
            },
            {
                "id": "sq1_5",
                "label": "1.5 Mean:",
                "instruction": "(Keep all decimal places in the answer)",
                "type": "text",
                "answer": "32",
                "acceptedAnswers": ["32", "32.0", "32.00"],
                "hint": "Sum of all 31 observations = 992. Mean = 992 / 31 = 32.0."
            },
            {
                "id": "sq1_6",
                "label": "1.6 IQR:",
                "instruction": "(Keep all decimal places in the answer)",
                "type": "text",
                "answer": "13",
                "acceptedAnswers": ["13"],
                "hint": "IQR = Q3 - Q1 = 37 - 24 = 13."
            },
            {
                "id": "sq2_1",
                "label": "2.1 Upper boundary to check outliers:",
                "instruction": "(Keep all decimal places in the answer)",
                "type": "text",
                "answer": "56.5",
                "acceptedAnswers": ["56.5"],
                "hint": "Upper Fence = Q3 + 1.5 * IQR = 37 + 1.5 * 13 = 37 + 19.5 = 56.5."
            },
            {
                "id": "sq2_2",
                "label": "2.2 Lower boundary to check outliers:",
                "instruction": "(Keep all decimal places in the answer)",
                "type": "text",
                "answer": "4.5",
                "acceptedAnswers": ["4.5"],
                "hint": "Lower Fence = Q1 - 1.5 * IQR = 24 - 1.5 * 13 = 24 - 19.5 = 4.5."
            },
            {
                "id": "sq2_3",
                "label": "2.3 How many outliers are there in the data set:",
                "type": "text",
                "answer": "0",
                "acceptedAnswers": ["0"],
                "hint": "Minimum value is 15 (> 4.5) and maximum is 52 (< 56.5). Therefore, 0 outliers."
            },
            {
                "id": "sq3",
                "label": "3. Which of the following statistics would remain unchanged if a constant value was added to every execution time in the dataset?",
                "type": "dropdown",
                "options": [
                    "Interquartile range (IQR)",
                    "Mean",
                    "Median",
                    "Mode"
                ],
                "answer": "Interquartile range (IQR)",
                "hint": "Measures of dispersion (Variance, Standard Deviation, IQR, Range) are invariant under constant addition/shifting: IQR(X + c) = IQR(X)."
            }
        ],
        "theorySummary": "Quartiles divide sorted data into four quarters. Fences for outliers are defined as [Q1 - 1.5*IQR, Q3 + 1.5*IQR]. Adding a constant k to each observation shifts central tendencies by k but leaves measures of dispersion unchanged."
    },
    {
        "id": "PAS-CBE-04",
        "source": "Computer_Based_Exam/Question_02.jpg",
        "paper": "Computer-Based Exam (Lab Replica)",
        "questionNumber": 5,
        "topic": "Continuous Probability: Normal Distribution Applications",
        "marks": 6.00,
        "difficulty": "Hard",
        "prompt": "Most graduate schools of computer science require applicants to take a Programming Aptitude Test (PAT). Scores on the PAT are approximately normally distributed with a mean of 680 and a standard deviation of 75.\nFind the answers to the following questions (Type the answer in the given space).",
        "type": "multipart",
        "subquestions": [
            {
                "id": "sq1",
                "label": "1) What is the probability of an individual scoring above 700 on the PAT?",
                "instruction": "(Keep all decimal places in the answer)",
                "type": "text",
                "answer": "0.3948",
                "acceptedAnswers": ["0.3948", "0.395", "0.394"],
                "hint": "Z = (700 - 680) / 75 = 20 / 75 = 0.27. P(X > 700) = P(Z > 0.27) = 1 - Φ(0.27) = 1 - 0.6064 = 0.3948 (or 0.3949)."
            },
            {
                "id": "sq2",
                "label": "2) How high must an individual score on the PAT in order to score in the highest 2%?",
                "instruction": "(Round off the answer up to 2 decimal places)",
                "type": "text",
                "answer": "834.03",
                "acceptedAnswers": ["834.03", "834.0", "834", "834.13"],
                "hint": "Highest 2% corresponds to area 0.98 to the left. Critical Z_0.02 = 2.054 (or 2.05). X = μ + Z*σ = 680 + 2.0537 * 75 = 834.03."
            },
            {
                "id": "sq3",
                "label": "3) What is the probability of an individual scoring below 600 on the PAT?",
                "instruction": "(Keep all decimal places in the answer)",
                "type": "text",
                "answer": "0.1431",
                "acceptedAnswers": ["0.1431", "0.143", "0.1423"],
                "hint": "Z = (600 - 680) / 75 = -80 / 75 = -1.07. P(X < 600) = Φ(-1.07) = 0.1423 to 0.1431."
            }
        ],
        "theorySummary": "Standardization converts any normal distribution X ~ N(μ, σ²) to the standard normal Z = (X - μ) / σ ~ N(0, 1). To find cutoffs for top percentiles, solve X = μ + Z*σ."
    },
    {
        "id": "PAS-CBE-05",
        "source": "Computer_Based_Exam/Question_14.jpg",
        "paper": "Computer-Based Exam (Lab Replica)",
        "questionNumber": 5,
        "topic": "Exploratory Data Analysis and Distribution Skewness",
        "marks": 20.00,
        "difficulty": "Hard",
        "prompt": "Consider the variations in response times observed when a mobile application retrieves fitness tracking data from different cloud-hosted APIs.\n12, 18, 27, 23, 18, 14, 17, 25, 34, 33, 16, 27, 31, 39, 35, 26, 28, 37, 40, 42, 30, 36, 38, 24, 41, 13, 15, 14, 23, 43, 18\n(Type your answers within the given spaces except for part 3)",
        "type": "multipart",
        "subquestions": [
            {
                "id": "sq1_1",
                "label": "1.1 Mode:",
                "instruction": "(If you have any, keep all decimal places in the answer)",
                "type": "text",
                "answer": "18",
                "acceptedAnswers": ["18"],
                "hint": "Value 18 appears 3 times in the sample."
            },
            {
                "id": "sq1_2",
                "label": "1.2 Q1 (First quartile):",
                "instruction": "(If you have any, keep all decimal places in the answer)",
                "type": "text",
                "answer": "18",
                "acceptedAnswers": ["18"],
                "hint": "8th value in ordered list of 31 observations is 18."
            },
            {
                "id": "sq1_3",
                "label": "1.3 Median:",
                "instruction": "(If you have any, keep all decimal places in the answer)",
                "type": "text",
                "answer": "27",
                "acceptedAnswers": ["27"],
                "hint": "16th ordered value is 27."
            },
            {
                "id": "sq1_4",
                "label": "1.4 Q3 (Third quartile):",
                "instruction": "(If you have any, keep all decimal places in the answer)",
                "type": "text",
                "answer": "36",
                "acceptedAnswers": ["36"],
                "hint": "24th ordered value is 36."
            },
            {
                "id": "sq1_5",
                "label": "1.5 Mean:",
                "instruction": "(If you have any, keep all decimal places in the answer)",
                "type": "text",
                "answer": "27",
                "acceptedAnswers": ["27", "27.0", "27.00"],
                "hint": "Sum = 837 / 31 = 27.0."
            },
            {
                "id": "sq1_6",
                "label": "1.6 IQR:",
                "instruction": "(If you have any, keep all decimal places in the answer)",
                "type": "text",
                "answer": "18",
                "acceptedAnswers": ["18"],
                "hint": "IQR = Q3 - Q1 = 36 - 18 = 18."
            },
            {
                "id": "sq2_1",
                "label": "2.1 Upper boundary to check outliers:",
                "type": "text",
                "answer": "63",
                "acceptedAnswers": ["63", "63.0"],
                "hint": "Upper fence = 36 + 1.5 * 18 = 36 + 27 = 63."
            },
            {
                "id": "sq2_2",
                "label": "2.2 Lower boundary to check outliers:",
                "type": "text",
                "answer": "-9",
                "acceptedAnswers": ["-9", "-9.0"],
                "hint": "Lower fence = 18 - 1.5 * 18 = 18 - 27 = -9."
            },
            {
                "id": "sq2_3",
                "label": "2.3 How many outliers are there in the data set:",
                "type": "text",
                "answer": "0",
                "acceptedAnswers": ["0"],
                "hint": "All observations fall within [-9, 63]."
            },
            {
                "id": "sq3",
                "label": "3. According to the box plot of the data set, what is the shape of the distribution?",
                "type": "dropdown",
                "options": [
                    "Symmetric distribution",
                    "Positively skewed (skewed to the right)",
                    "Negatively skewed (skewed to the left)",
                    "Bimodal distribution"
                ],
                "answer": "Symmetric distribution",
                "hint": "Mean = 27 and Median = 27, and the distance from Q1 to Median (27 - 18 = 9) exactly equals the distance from Median to Q3 (36 - 27 = 9). The box plot is symmetric."
            }
        ],
        "theorySummary": "When Mean ≈ Median and (Median - Q1) ≈ (Q3 - Median), the distribution shows no skewness and is symmetric."
    },
    {
        "id": "PAS-CBE-06",
        "source": "Computer_Based_Exam/Question_04.jpg",
        "paper": "Computer-Based Exam (Lab Replica)",
        "questionNumber": 7,
        "topic": "Principles of Experimental Design: Variable Identification",
        "marks": 24.00,
        "difficulty": "Medium",
        "prompt": "1) A researcher is studying the effect of light exposure on the sleep patterns of adults. The researcher exposes one group to 6 hours of light, another group to 8 hours, and a third group to 10 hours of light daily, then measures how many hours of sleep each group gets on average.",
        "type": "multipart",
        "subquestions": [
            {
                "id": "sq1",
                "label": "Independent Variable:",
                "type": "radio",
                "options": [
                    "Average age of the participants",
                    "Time of day the light exposure occurs",
                    "Number of adults in each group",
                    "Hours of light exposure (6 hours, 8 hours, 10 hours)",
                    "Hours of sleep"
                ],
                "answer": 3,
                "hint": "The independent variable is the factor deliberately manipulated or controlled by the experimenter."
            },
            {
                "id": "sq2",
                "label": "Dependent Variable:",
                "type": "radio",
                "options": [
                    "Time of day the light exposure occurs",
                    "Average age of the participants",
                    "Number of adults in each group",
                    "Hours of light exposure (6 hours, 8 hours, 10 hours)",
                    "Hours of sleep"
                ],
                "answer": 4,
                "hint": "The dependent variable is the outcome measured to assess the effect of the treatment."
            }
        ],
        "theorySummary": "In scientific experiments, the Independent Variable (IV) is what is changed, while the Dependent Variable (DV) is what is observed and measured."
    },
    {
        "id": "PAS-CBE-07",
        "source": "Computer_Based_Exam/Question_15.jpg",
        "paper": "Computer-Based Exam (Lab Replica)",
        "questionNumber": 4,
        "topic": "Two-Tailed Hypothesis Testing for Population Mean (Known Variance)",
        "marks": 14.00,
        "difficulty": "Expert",
        "prompt": "A software development team claimed that the new API endpoint do not change the true average response time from 150 milliseconds (which is the current response time). A random sample of 45 requests recorded a mean response time of 156 milliseconds with population standard deviation of 12 milliseconds. Test the claim at 5% level of significance.",
        "type": "multipart",
        "subquestions": [
            {
                "id": "sq1",
                "label": "1. What is the hypothesis?",
                "type": "dropdown",
                "options": [
                    "H0: μ = 150 vs H1: μ ≠ 150",
                    "H0: μ ≥ 150 vs H1: μ < 150",
                    "H0: μ ≥ 150 vs H1: μ ≠ 150",
                    "H0: μ ≤ 150 vs H1: μ ≠ 150",
                    "H0: μ ≤ 150 vs H1: μ > 150"
                ],
                "answer": "H0: μ = 150 vs H1: μ ≠ 150",
                "hint": "The team claims the response time 'does not change' (remains 150). The two-tailed alternative hypothesis is μ ≠ 150."
            },
            {
                "id": "sq2",
                "label": "2. What is the distribution of test statistic?",
                "type": "dropdown",
                "options": [
                    "Standard Normal distribution",
                    "Student's t-distribution with 44 df",
                    "Chi-Square distribution",
                    "Exponential distribution"
                ],
                "answer": "Standard Normal distribution",
                "hint": "Population standard deviation σ = 12 is known and sample size n = 45 > 30, so the test statistic follows a Standard Normal (Z) distribution."
            },
            {
                "id": "sq3",
                "label": "3. What is the critical value?",
                "instruction": "(Type your answer here and keep the answer with two decimal places. Do not mention the sign. Mention only the number)",
                "type": "text",
                "answer": "1.96",
                "acceptedAnswers": ["1.96"],
                "hint": "For a two-tailed test at α = 0.05, α/2 = 0.025 in each tail. Z_0.025 = 1.96."
            },
            {
                "id": "sq4",
                "label": "4. Select correct rejection region for the test.",
                "type": "dropdown",
                "options": [
                    "Z_calc < -1.96 or Z_calc > 1.96",
                    "Z_calc > 1.96",
                    "Z_calc < -1.645",
                    "Z_calc > 1.645"
                ],
                "answer": "Z_calc < -1.96 or Z_calc > 1.96",
                "hint": "Two-tailed rejection region consists of both extremes |Z| > 1.96."
            },
            {
                "id": "sq5",
                "label": "5. What is the test statistic value?",
                "instruction": "(Type your answer here and round off the answer up to four decimal places)",
                "type": "text",
                "answer": "3.3541",
                "acceptedAnswers": ["3.3541", "3.354", "3.35"],
                "hint": "Z = (156 - 150) / (12 / √45) = 6 / (12 / 6.7082) = 6 / 1.78885 = 3.3541."
            },
            {
                "id": "sq6",
                "label": "6. Give the scientific conclusion:",
                "type": "dropdown",
                "options": [
                    "Reject H0 at 5% significance level",
                    "Fail to reject H0 at 5% significance level",
                    "Accept H0 as definitively true",
                    "Inconclusive test result"
                ],
                "answer": "Reject H0 at 5% significance level",
                "hint": "Calculated value Z_calc = 3.3541 is substantially greater than the critical threshold 1.96."
            },
            {
                "id": "sq7",
                "label": "7. What is the general conclusion?",
                "type": "dropdown",
                "options": [
                    "There is sufficient evidence that the new API endpoint changes the average response time",
                    "There is insufficient evidence that the new API endpoint changes the average response time",
                    "The response time remains exactly 150 milliseconds",
                    "The sample size was inadequate"
                ],
                "answer": "There is sufficient evidence that the new API endpoint changes the average response time",
                "hint": "Rejecting H0 disproves the team's claim that response time did not change."
            }
        ],
        "theorySummary": "When σ is known, Z = (X̄ - μ0) / (σ / √n). In a two-tailed test, reject H0 if |Z| > Z_{α/2}."
    },
    {
        "id": "PAS-CBE-08",
        "source": "Computer_Based_Exam/Question_16.jpg",
        "paper": "Computer-Based Exam (Lab Replica)",
        "questionNumber": 3,
        "topic": "Time Series Components Identification",
        "marks": 6.00,
        "difficulty": "Medium",
        "prompt": "Consider the following time series plot. Time is in years.",
        "image": "/images/timeseries_plot.jpg",
        "type": "multipart",
        "subquestions": [
            {
                "id": "sq1",
                "label": "1. What are the components we can identify through the above time series plot?",
                "type": "dropdown",
                "options": [
                    "Upward trend, irregular fluctuations and cyclic variations",
                    "Upward trend only",
                    "Seasonal component and cyclic variations only",
                    "Irregular fluctuations only",
                    "Upward trend and irregular fluctuations only"
                ],
                "answer": "Upward trend, irregular fluctuations and cyclic variations",
                "hint": "The plot exhibits an overarching upward secular trend over decades, multi-year cyclical crests and troughs (cycles), and sharp short-term jagged noise (irregular variations). Since time is measured in years, within-year seasonality is not observed."
            }
        ],
        "theorySummary": "A classical time series Y_t consists of: Trend (T), Cyclical (C), Seasonal (S), and Irregular (I) components. Annual data exhibits Trend, Cyclical, and Irregular components."
    },
    {
        "id": "PAS-CBE-09",
        "source": "Computer_Based_Exam/Question_17.jpg",
        "paper": "Computer-Based Exam (Lab Replica)",
        "questionNumber": 5,
        "topic": "Normal Distribution Probability Computations",
        "marks": 6.00,
        "difficulty": "Hard",
        "prompt": "A tech company uses a Data Analyst Proficiency Test (DAPT) to evaluate applicants. Scores on the DAPT are normally distributed with a mean of 750 and a standard deviation of 85.\nFind the answers to the following questions (Type the answer in the given space).",
        "type": "multipart",
        "subquestions": [
            {
                "id": "sq1",
                "label": "1) What is the probability of an individual scoring above 780 on the DAPT?",
                "instruction": "(Keep all decimal places in the answer)",
                "type": "text",
                "answer": "0.3621",
                "acceptedAnswers": ["0.3621", "0.3632", "0.362"],
                "hint": "Z = (780 - 750) / 85 = 30 / 85 = 0.3529 ≈ 0.35. P(Z > 0.35) = 1 - 0.6368 = 0.3632 (or 0.3621)."
            },
            {
                "id": "sq2",
                "label": "2) How high must an individual score on the DAPT to be in the highest 3%?",
                "instruction": "(Keep all decimal places in the answer)",
                "type": "text",
                "answer": "909.87",
                "acceptedAnswers": ["909.87", "909.9", "910", "909.8"],
                "hint": "Top 3% means area to the left is 0.97. Z_0.03 = 1.8808. X = 750 + 1.8808 * 85 = 909.87."
            },
            {
                "id": "sq3",
                "label": "3) What is the probability that an individual scores below 700 on the DAPT?",
                "instruction": "(Keep all decimal places in the answer)",
                "type": "text",
                "answer": "0.2782",
                "acceptedAnswers": ["0.2782", "0.2776", "0.278"],
                "hint": "Z = (700 - 750) / 85 = -50 / 85 = -0.5882 ≈ -0.59. P(Z < -0.59) = 0.2776 to 0.2782."
            }
        ],
        "theorySummary": "Normal probability calculations require standardizing X into Z = (X - μ)/σ, finding table values for Φ(Z), and reversing the transformation X = μ + Z*σ to find critical score thresholds."
    },
    {
        "id": "PAS-CBE-10",
        "source": "Computer_Based_Exam/Question_18.jpg",
        "paper": "Computer-Based Exam (Lab Replica)",
        "questionNumber": 2,
        "topic": "Chi-Square Test of Independence in Contingency Tables",
        "marks": 15.00,
        "difficulty": "Expert",
        "prompt": "A school administrator wants to know if there is an association between students' academic year (1st year, 2nd year, 3rd year) and their preferred mode of learning (Face-to-face, Online, Hybrid). He collected data from 140 students and the results are shown below:\n\n| Academic Year | Face-to-Face | Online | Hybrid | Total |\n|---|---|---|---|---|\n| 1st Year | 15 | 13 | 12 | 40 |\n| 2nd Year | 14 | 16 | 10 | 40 |\n| 3rd Year | 18 | 20 | 22 | 60 |\n| Total | 47 | 49 | 44 | 140 |\n\nTest at 5% significance level whether there is a significant relationship between students' academic year and their preferred mode of learning.\n\nChi-Square Test Statistic: $X^2 = \\sum_{\\text{all } i} \\sum_{\\text{all } j} \\frac{(O_{ij} - E_{ij})^2}{E_{ij}}$",
        "type": "multipart",
        "subquestions": [
            {
                "id": "sq1",
                "label": "1. Hypothesis:",
                "type": "dropdown",
                "options": [
                    "H0: Students' academic year and their preferred mode of learning are independent Vs. H1: Students' academic year and their preferred mode of learning are not independent.",
                    "H0: Students' academic year and their preferred mode of learning are not independent Vs. H1: Students' academic year and their preferred mode of learning are independent.",
                    "H0: Academic year causes the mode of learning Vs. H1: Mode of learning causes academic year.",
                    "H0: All learning mode proportions are equal to 1/3."
                ],
                "answer": "H0: Students' academic year and their preferred mode of learning are independent Vs. H1: Students' academic year and their preferred mode of learning are not independent.",
                "hint": "In a test of independence, H0 always states that the two categorical variables are independent."
            },
            {
                "id": "sq2",
                "label": "2. Degrees of Freedom (df):",
                "type": "text",
                "answer": "4",
                "acceptedAnswers": ["4"],
                "hint": "df = (r - 1) * (c - 1) = (3 - 1) * (3 - 1) = 2 * 2 = 4."
            },
            {
                "id": "sq3",
                "label": "3. Critical Value (at α = 0.05, df = 4):",
                "type": "text",
                "answer": "9.488",
                "acceptedAnswers": ["9.488", "9.49"],
                "hint": "From Chi-Square distribution tables with df = 4 and α = 0.05, χ²_crit = 9.488."
            },
            {
                "id": "sq4",
                "label": "4. Calculated Chi-Square Statistic Value:",
                "type": "text",
                "answer": "1.9167",
                "acceptedAnswers": ["1.9167", "1.92", "1.917"],
                "hint": "Expected frequencies E_ij = (Row Total * Col Total) / Grand Total. Sum of (O - E)² / E across all 9 cells equals 1.9167."
            },
            {
                "id": "sq5",
                "label": "5. Conclusion:",
                "type": "dropdown",
                "options": [
                    "Fail to reject H0; there is no significant association between academic year and mode of learning",
                    "Reject H0; academic year significantly affects learning mode",
                    "Accept H1 as definitively true",
                    "Test is invalid due to cell count violations"
                ],
                "answer": "Fail to reject H0; there is no significant association between academic year and mode of learning",
                "hint": "Because χ²_calc (1.9167) < χ²_crit (9.488), we do not reject H0."
            }
        ],
        "theorySummary": "The Chi-Square test of independence examines whether two categorical variables in an r x c contingency table are related. Expected count E_ij = (R_i * C_j) / N. The test statistic has (r-1)(c-1) degrees of freedom."
    },
    {
        "id": "PAS-CBE-11",
        "source": "Computer_Based_Exam/Question_19.jpg",
        "paper": "Computer-Based Exam (Lab Replica)",
        "questionNumber": 6,
        "topic": "Large-Sample Confidence Interval for Mean (Known Variance)",
        "marks": 12.00,
        "difficulty": "Hard",
        "prompt": "A tech firm wants to estimate the average time (in seconds) it takes for its database server to execute a query. A sample of 60 queries shows an average execution time of 0.72 seconds with a population standard deviation of 0.08 seconds. Construct a 95% confidence interval for the true mean execution time of the database server.",
        "type": "multipart",
        "subquestions": [
            {
                "id": "sq1",
                "label": "1. Lower limit equation:",
                "type": "dropdown",
                "options": [
                    "x̄ - z(α/2) * (σ / √n)",
                    "x̄ + z(α/2) * (σ / √n)",
                    "x̄ - t(α/2, n-1) * (s / √n)",
                    "x̄ - z(α) * (σ / √n)"
                ],
                "answer": "x̄ - z(α/2) * (σ / √n)",
                "hint": "Known population standard deviation σ uses the Standard Normal Z-equation."
            },
            {
                "id": "sq2",
                "label": "2. Upper limit equation:",
                "type": "dropdown",
                "options": [
                    "x̄ + z(α/2) * (σ / √n)",
                    "x̄ - z(α/2) * (σ / √n)",
                    "x̄ + t(α/2, n-1) * (s / √n)",
                    "x̄ + z(α) * (σ / √n)"
                ],
                "answer": "x̄ + z(α/2) * (σ / √n)",
                "hint": "Upper limit adds the margin of error."
            },
            {
                "id": "sq3",
                "label": "3. Critical value:",
                "instruction": "(Type your answer here and keep the answer with all decimal places. Do not mention the sign. Mention only the number)",
                "type": "text",
                "answer": "1.96",
                "acceptedAnswers": ["1.96"],
                "hint": "For a 95% confidence interval with known variance, Z_0.025 = 1.96."
            },
            {
                "id": "sq4",
                "label": "4. Lower limit value:",
                "instruction": "(Type your answer here and keep the answer with four decimal places)",
                "type": "text",
                "answer": "0.6998",
                "acceptedAnswers": ["0.6998", "0.70"],
                "hint": "Lower = 0.72 - 1.96 * (0.08 / √60) = 0.72 - 0.02024 = 0.6998."
            },
            {
                "id": "sq5",
                "label": "5. Upper limit value:",
                "instruction": "(Type your answer here and keep the answer with four decimal places)",
                "type": "text",
                "answer": "0.7402",
                "acceptedAnswers": ["0.7402", "0.74"],
                "hint": "Upper = 0.72 + 1.96 * (0.08 / √60) = 0.72 + 0.02024 = 0.7402."
            },
            {
                "id": "sq6",
                "label": "6. Lets assume that lower limit is a and upper limit is b. Interpret the confidence interval:",
                "type": "radio",
                "options": [
                    "We are 95% confident that the true mean execution time of the database server will be between a and b",
                    "We are 95% confident that the true mean execution time of the database server will not be between a and b",
                    "We are 2.5% confident that the true mean execution time of the database server will not be between a and b",
                    "We are 2.5% confident that the true mean execution time of the database server will be between a and b",
                    "We are 5% confident that the true mean execution time of the database server will be between a and b"
                ],
                "answer": 0,
                "hint": "Standard interpretation: 95% confidence that the population mean execution time lies within the interval."
            }
        ],
        "theorySummary": "When σ is known, the 100(1-α)% confidence interval is X̄ ± Z_{α/2} * (σ / √n). Margin of error narrows as sample size n increases."
    }
]

# -------------------------------------------------------------
# 2. AI_ML QUESTIONS (From Final Revision & Deep Learning Papers)
# -------------------------------------------------------------

modules_data["AIML"]["questions"] = [
    {
        "id": "AIML-01",
        "paper": "2024 Final Revision Session",
        "questionNumber": 1,
        "topic": "Feature Classification (Numerical vs Categorical)",
        "marks": 5.00,
        "difficulty": "Medium",
        "prompt": "Consider a dataset representing 10 students' performance with the following features:\n- Study Hours (weekly average hours studied)\n- Attendance Percentage (percentage of classes attended)\n- Previous Exam Score (out of 100)\n- Gender (Male or Female)\n- Extracurricular Activities (Yes or No)\n- Result (Pass or Fail)\n\nIdentify the correct classification for these feature attributes:",
        "type": "mcq",
        "options": [
            "Numerical: Study Hours, Attendance Percentage, Previous Exam Score; Categorical: Gender, Extracurricular Activities, Result",
            "Numerical: Study Hours, Gender; Categorical: Attendance Percentage, Previous Exam Score, Result",
            "Numerical: Previous Exam Score, Result; Categorical: Study Hours, Attendance Percentage, Gender",
            "All features in this dataset are Numerical features"
        ],
        "answer": 0,
        "solution": "Numerical features represent measurable quantities with arithmetic meaning (Study Hours, Attendance Percentage, Exam Score). Categorical features represent qualitative labels or groups (Gender: Male/Female; Extracurricular: Yes/No; Result: Pass/Fail).",
        "theorySummary": "Features in machine learning are broadly split into Numerical (continuous or discrete values allowing mathematical operations) and Categorical (nominal labels without intrinsic ordering or ordinal ranks)."
    },
    {
        "id": "AIML-02",
        "paper": "2024 Final Revision Session",
        "questionNumber": 2,
        "topic": "Decision Trees: Gini Impurity Calculation",
        "marks": 15.00,
        "difficulty": "Expert",
        "prompt": "For the student performance dataset, the overall target 'Result' has 5 Pass and 5 Fail instances (Total = 10).\n\nFormula for Gini Impurity: $\\text{Gini}(D) = 1 - \\sum_{i=1}^C p_i^2$.\n\nWhen splitting on 'Gender':\n- Male (6 students): 3 Pass, 3 Fail\n- Female (4 students): 2 Pass, 2 Fail\n\nCalculate the weighted Gini Index for the feature 'Gender'.",
        "type": "multipart",
        "subquestions": [
            {
                "id": "sq1",
                "label": "1. Gini impurity of the root node before splitting:",
                "type": "text",
                "answer": "0.5",
                "acceptedAnswers": ["0.5", "0.50"],
                "hint": "Gini(Root) = 1 - [(5/10)² + (5/10)²] = 1 - [0.25 + 0.25] = 0.50."
            },
            {
                "id": "sq2",
                "label": "2. Gini impurity for Male subset (3 Pass, 3 Fail):",
                "type": "text",
                "answer": "0.5",
                "acceptedAnswers": ["0.5", "0.50"],
                "hint": "Gini(Male) = 1 - [(3/6)² + (3/6)²] = 1 - [0.25 + 0.25] = 0.50."
            },
            {
                "id": "sq3",
                "label": "3. Gini impurity for Female subset (2 Pass, 2 Fail):",
                "type": "text",
                "answer": "0.5",
                "acceptedAnswers": ["0.5", "0.50"],
                "hint": "Gini(Female) = 1 - [(2/4)² + (2/4)²] = 1 - [0.25 + 0.25] = 0.50."
            },
            {
                "id": "sq4",
                "label": "4. Weighted Gini Index for Gender split:",
                "type": "text",
                "answer": "0.5",
                "acceptedAnswers": ["0.5", "0.50"],
                "hint": "Gini_split = (6/10) * 0.5 + (4/10) * 0.5 = 0.50. Information Gain = 0.50 - 0.50 = 0 (Gender provides no purity improvement!)."
            }
        ],
        "theorySummary": "The CART algorithm uses the Gini index to choose best splits. Maximum impurity occurs at 0.5 (equal distribution across binary classes), while pure nodes have Gini = 0. A split that yields 0 information gain is ineffective."
    },
    {
        "id": "AIML-03",
        "paper": "2024 Final Revision Session",
        "questionNumber": 3,
        "topic": "K-Means Clustering & Euclidean Distance",
        "marks": 15.00,
        "difficulty": "Hard",
        "prompt": "In an unsupervised learning task, two initial cluster centroids are chosen: $C_1 = (2, 3)$ and $C_2 = (6, 7)$. A new data point is $P = (3, 5)$.\n\n1. What is the Euclidean distance from $P$ to $C_1$?\n2. What is the Euclidean distance from $P$ to $C_2$?\n3. Which cluster should point $P$ be assigned to?",
        "type": "multipart",
        "subquestions": [
            {
                "id": "sq1",
                "label": "Distance to C1 (2, 3):",
                "instruction": "(Round off to two decimal places)",
                "type": "text",
                "answer": "2.24",
                "acceptedAnswers": ["2.24", "2.236"],
                "hint": "d(P, C1) = √[(3 - 2)² + (5 - 3)²] = √[1 + 4] = √5 ≈ 2.236."
            },
            {
                "id": "sq2",
                "label": "Distance to C2 (6, 7):",
                "instruction": "(Round off to two decimal places)",
                "type": "text",
                "answer": "3.61",
                "acceptedAnswers": ["3.61", "3.605"],
                "hint": "d(P, C2) = √[(3 - 6)² + (5 - 7)²] = √[(-3)² + (-2)²] = √[9 + 4] = √13 ≈ 3.605."
            },
            {
                "id": "sq3",
                "label": "Cluster Assignment:",
                "type": "dropdown",
                "options": [
                    "Cluster 1 (Centroid C1)",
                    "Cluster 2 (Centroid C2)",
                    "Equally shared between both clusters"
                ],
                "answer": "Cluster 1 (Centroid C1)",
                "hint": "Point P is assigned to the nearest centroid: 2.24 < 3.61."
            }
        ],
        "theorySummary": "K-Means iteratively partitions data into K clusters by assigning each point to its nearest centroid using distance metrics (typically Euclidean distance d = √∑(x_i - y_i)²), then recalculating centroids as cluster means."
    },
    {
        "id": "AIML-04",
        "paper": "2024 Final Revision Session",
        "questionNumber": 4,
        "topic": "Model Evaluation Metrics & Confusion Matrix",
        "marks": 10.00,
        "difficulty": "Hard",
        "prompt": "A binary classification model evaluated on 100 test samples produces the following confusion matrix:\n- True Positives (TP) = 40\n- False Positives (FP) = 10\n- True Negatives (TN) = 40\n- False Negatives (FN) = 10\n\nCalculate the Precision, Recall, Accuracy, and F1-Score of this model.",
        "type": "multipart",
        "subquestions": [
            {
                "id": "sq1",
                "label": "Accuracy:",
                "type": "text",
                "answer": "0.8",
                "acceptedAnswers": ["0.8", "0.80", "80%"],
                "hint": "Accuracy = (TP + TN) / Total = (40 + 40) / 100 = 0.80 (80%)."
            },
            {
                "id": "sq2",
                "label": "Precision:",
                "type": "text",
                "answer": "0.8",
                "acceptedAnswers": ["0.8", "0.80", "80%"],
                "hint": "Precision = TP / (TP + FP) = 40 / (40 + 10) = 40 / 50 = 0.80 (80%)."
            },
            {
                "id": "sq3",
                "label": "Recall (Sensitivity):",
                "type": "text",
                "answer": "0.8",
                "acceptedAnswers": ["0.8", "0.80", "80%"],
                "hint": "Recall = TP / (TP + FN) = 40 / (40 + 10) = 40 / 50 = 0.80 (80%)."
            },
            {
                "id": "sq4",
                "label": "F1-Score:",
                "type": "text",
                "answer": "0.8",
                "acceptedAnswers": ["0.8", "0.80"],
                "hint": "F1 = 2 * (Precision * Recall) / (Precision + Recall) = 2 * (0.8 * 0.8) / 1.6 = 0.80."
            }
        ],
        "theorySummary": "Precision evaluates how many of the positively predicted instances were actually correct. Recall evaluates how many of the actual positive cases the model captured. F1-score provides the harmonic mean."
    },
    {
        "id": "AIML-05",
        "paper": "Deep Learning Structure Revision",
        "questionNumber": 5,
        "topic": "Neural Network Forward Propagation & Activation Functions",
        "marks": 15.00,
        "difficulty": "Expert",
        "prompt": "An artificial neuron has two inputs $x_1 = 0.6$ and $x_2 = 0.8$ with associated synaptic weights $w_1 = 0.5$ and $w_2 = -0.25$, and a bias $b = 0.1$.\n\n1. Calculate the linear weighted sum (pre-activation) $z = w_1 x_1 + w_2 x_2 + b$.\n2. If the activation function is the Sigmoid function $\\sigma(z) = \\frac{1}{1 + e^{-z}}$, calculate the final output $\\hat{y}$.",
        "type": "multipart",
        "subquestions": [
            {
                "id": "sq1",
                "label": "Pre-activation value z:",
                "type": "text",
                "answer": "0.2",
                "acceptedAnswers": ["0.2", "0.20"],
                "hint": "z = (0.5 * 0.6) + (-0.25 * 0.8) + 0.1 = 0.30 - 0.20 + 0.10 = 0.20."
            },
            {
                "id": "sq2",
                "label": "Sigmoid output σ(z):",
                "instruction": "(Round off to four decimal places)",
                "type": "text",
                "answer": "0.5498",
                "acceptedAnswers": ["0.5498", "0.55"],
                "hint": "σ(0.20) = 1 / (1 + e^(-0.20)) = 1 / (1 + 0.8187) = 1 / 1.8187 ≈ 0.5498."
            }
        ],
        "theorySummary": "In neural networks, each layer computes a linear combination z = Wx + b followed by a non-linear activation function f(z). Sigmoid squashes real numbers into (0, 1), making it ideal for probability estimation."
    }
]

# -------------------------------------------------------------
# 3. DDD / DMS QUESTIONS (Database Design & Development)
# -------------------------------------------------------------

modules_data["DDD"]["questions"] = [
    {
        "id": "DDD-01",
        "paper": "2024 Final Examination",
        "questionNumber": 1,
        "topic": "EER to Relational Schema Mapping (ISA Hierarchy)",
        "marks": 20.00,
        "difficulty": "Hard",
        "prompt": "Consider an Enhanced Entity-Relationship (EER) model with a superclass `Employee` and subclasses `SalariedEmployee` and `HourlyEmployee`. The specialization is specified as {disjoint, total}.\n\nWhich of the following is the most appropriate relational schema design when all subclasses have distinct specific attributes and all employees must belong to exactly one subclass?",
        "type": "mcq",
        "options": [
            "Option A: Two distinct relations `SalariedEmployee` and `HourlyEmployee`, each inheriting all attributes of `Employee` as primary relation columns (No superclass relation).",
            "Option B: A single wide relation with all superclass and subclass attributes, adding a `type` discriminator attribute and allowing NULL values for inactive subclass columns.",
            "Option C: Three relations (`Employee`, `SalariedEmployee`, `HourlyEmployee`) linked via foreign key references on EmployeeID.",
            "Option D: A single relation containing only EmployeeID and name with no specialized attributes."
        ],
        "answer": 0,
        "solution": "When specialization is total (every entity belongs to a subclass) and disjoint (no entity belongs to more than one subclass), mapping to separate subclass relations that include all superclass attributes avoids NULL values and avoids unnecessary table joins.",
        "theorySummary": "ISA mapping strategies: 1. Multiple relations for subclasses only (optimal for total, disjoint). 2. Single relation with type flag (best for disjoint with few specific attributes). 3. Superclass + subclass relations (standard, works for any constraint)."
    },
    {
        "id": "DDD-02",
        "paper": "2023 Final Examination",
        "questionNumber": 2,
        "topic": "Functional Dependencies, Minimal Cover & Candidate Keys",
        "marks": 20.00,
        "difficulty": "Expert",
        "prompt": "A relational schema $R(A, B, C, D, E)$ has the following set of functional dependencies $F$:\n$F = \\{ A \\rightarrow B, \\quad BC \\rightarrow D, \\quad E \\rightarrow C \\}$\n\n1. What is the attribute closure of $(A, E)$ denoted as $(AE)^+$?\n2. What is the candidate key for relation $R$?",
        "type": "multipart",
        "subquestions": [
            {
                "id": "sq1",
                "label": "1. Attribute closure (AE)+:",
                "type": "dropdown",
                "options": [
                    "{A, B, C, D, E} (All attributes)",
                    "{A, B, E}",
                    "{A, B, C, E}",
                    "{A, E}"
                ],
                "answer": "{A, B, C, D, E} (All attributes)",
                "hint": "Start with {A, E}. Using A -> B adds B -> {A, B, E}. Using E -> C adds C -> {A, B, C, E}. Using BC -> D adds D -> {A, B, C, D, E}."
            },
            {
                "id": "sq2",
                "label": "2. Candidate Key:",
                "type": "dropdown",
                "options": [
                    "AE",
                    "A",
                    "ABC",
                    "ADE"
                ],
                "answer": "AE",
                "hint": "Since (AE)+ contains all attributes of R and neither A nor E can be removed without losing closure, AE is the minimal superkey (Candidate Key)."
            }
        ],
        "theorySummary": "Attribute closure X+ is the set of all attributes functionally determined by X under F. If X+ = R and no proper subset of X determines R, then X is a candidate key."
    },
    {
        "id": "DDD-03",
        "paper": "2022 Final Examination",
        "questionNumber": 3,
        "topic": "Normalization: 3NF vs BCNF Decomposition",
        "marks": 20.00,
        "difficulty": "Expert",
        "prompt": "Consider relation $R(A, B, C)$ with functional dependencies $F = \\{ AB \\rightarrow C, \\quad C \\rightarrow B \\}$.\n\n1. What are the candidate keys for relation $R$?\n2. In what normal form is relation $R$ currently in?\n3. Does relation $R$ satisfy Boyce-Codd Normal Form (BCNF)?",
        "type": "multipart",
        "subquestions": [
            {
                "id": "sq1",
                "label": "1. Candidate keys of R:",
                "type": "dropdown",
                "options": [
                    "AB and AC",
                    "AB only",
                    "C only",
                    "BC only"
                ],
                "answer": "AB and AC",
                "hint": "(AB)+ = {A, B, C}. Since C -> B, (AC)+ = {A, C, B} = {A, B, C}. Both AB and AC are candidate keys."
            },
            {
                "id": "sq2",
                "label": "2. Highest Normal Form satisfied:",
                "type": "dropdown",
                "options": [
                    "Third Normal Form (3NF)",
                    "Boyce-Codd Normal Form (BCNF)",
                    "Second Normal Form (2NF)",
                    "First Normal Form (1NF)"
                ],
                "answer": "Third Normal Form (3NF)",
                "hint": "For C -> B: C is not a superkey, but B is a prime attribute (part of candidate key AB). Therefore, R satisfies 3NF."
            },
            {
                "id": "sq3",
                "label": "3. Does it satisfy BCNF?",
                "type": "dropdown",
                "options": [
                    "No, because in C -> B, C is not a superkey",
                    "Yes, every 3NF relation is in BCNF",
                    "Yes, because C is a candidate key",
                    "No, because it violates 1NF"
                ],
                "answer": "No, because in C -> B, C is not a superkey",
                "hint": "BCNF strictly requires the determinant X in every non-trivial FD X -> Y to be a superkey."
            }
        ],
        "theorySummary": "A relation is in 3NF if for every X -> Y, X is a superkey OR Y is a prime attribute. BCNF is stricter: X MUST be a superkey (no prime attribute exception)."
    },
    {
        "id": "DDD-04",
        "paper": "Lockdown Compilation",
        "questionNumber": 4,
        "topic": "Transaction Concurrency & Two-Phase Locking (2PL)",
        "marks": 15.00,
        "difficulty": "Hard",
        "prompt": "Which of the following statements regarding Two-Phase Locking (2PL) and Serializability is TRUE?",
        "type": "mcq",
        "options": [
            "Basic 2PL guarantees conflict serializability, but it does NOT prevent cascading rollbacks or deadlocks.",
            "Basic 2PL prevents deadlocks automatically without requiring timestamps or lock timeouts.",
            "Strict 2PL releases all exclusive (X) locks as soon as the growing phase finishes.",
            "Rigorous 2PL requires all shared (S) locks to be released before the transaction commits."
        ],
        "answer": 0,
        "solution": "Basic 2PL guarantees that every valid schedule is conflict-serializable (no cycles in precedence graph). However, transactions may still reach deadlock or suffer cascading aborts. Strict 2PL prevents cascading aborts by holding exclusive locks until commit/abort.",
        "theorySummary": "Two-Phase Locking (2PL) has a Growing Phase (locks acquired, none released) and a Shrinking Phase (locks released, none acquired). Conflict serializability is guaranteed, but deadlock detection/prevention is still needed."
    }
]

# -------------------------------------------------------------
# 4. SE QUESTIONS (Software Engineering)
# -------------------------------------------------------------

modules_data["SE"]["questions"] = [
    {
        "id": "SE-01",
        "paper": "2024 June Final Exam",
        "questionNumber": 1,
        "topic": "Use Case Robustness Analysis (Boundary, Control, Entity)",
        "marks": 25.00,
        "difficulty": "Hard",
        "prompt": "During Use Case Analysis for a healthcare 'Schedule Appointment' system:\n- Step 1: Patient submits login credentials via `LoginForm`.\n- Step 2: `AuthenticationHandler` verifies credentials against `PatientRecord`.\n- Step 3: `AppointmentScheduler` checks available doctor slots in `ScheduleDB`.\n\nCategorize `LoginForm`, `AuthenticationHandler`, and `PatientRecord` into Robustness stereotypes (Boundary, Control, Entity):",
        "type": "mcq",
        "options": [
            "LoginForm: Boundary; AuthenticationHandler: Control; PatientRecord: Entity",
            "LoginForm: Control; AuthenticationHandler: Boundary; PatientRecord: Entity",
            "LoginForm: Entity; AuthenticationHandler: Control; PatientRecord: Boundary",
            "All three classes are Entity classes"
        ],
        "answer": 0,
        "solution": "Boundary objects mediate interaction between actors and the system (screens, forms, APIs). Control objects coordinate use-case workflows and business logic. Entity objects store persistent domain state.",
        "theorySummary": "Robustness analysis uses three stereotypes: Boundary (actor communication), Control (application logic orchestration), and Entity (long-lived persistent information)."
    },
    {
        "id": "SE-02",
        "paper": "2024 June Final Exam",
        "questionNumber": 2,
        "topic": "Gang of Four (GoF) Design Patterns",
        "marks": 20.00,
        "difficulty": "Expert",
        "prompt": "A payment processing system must support multiple payment gateways (Stripe, PayPal, Cryptopay). The specific gateway algorithm must be selectable at runtime based on user choice without altering the client code that executes the transaction.\n\nWhich design pattern should be applied, and what is its classification?",
        "type": "mcq",
        "options": [
            "Strategy Pattern (Behavioral pattern)",
            "Singleton Pattern (Creational pattern)",
            "Adapter Pattern (Structural pattern)",
            "Observer Pattern (Behavioral pattern)"
        ],
        "answer": 0,
        "solution": "The Strategy pattern defines a family of interchangeable algorithms, encapsulates each one, and makes them interchangeable at runtime without modifying the context client.",
        "theorySummary": "GoF Design Patterns are categorized into Creational (object creation), Structural (class composition), and Behavioral (algorithms and assignment of responsibilities between objects)."
    },
    {
        "id": "SE-03",
        "paper": "2022 Final Exam",
        "questionNumber": 3,
        "topic": "Software Testing: Boundary Value Analysis & Equivalence Partitioning",
        "marks": 20.00,
        "difficulty": "Hard",
        "prompt": "A banking system accepts loan application amounts between $1,000 and $50,000 inclusive (integer dollar values).\n\nUsing 2-value Boundary Value Analysis (BVA), what are the boundary test cases for the valid range?",
        "type": "mcq",
        "options": [
            "999, 1000, 50000, 50001",
            "1000, 25000, 50000",
            "0, 1000, 50000, 100000",
            "1001, 49999"
        ],
        "answer": 0,
        "solution": "Boundary Value Analysis tests values at and immediately beyond input boundaries: min-1 (999, invalid), min (1000, valid), max (50000, valid), and max+1 (50001, invalid).",
        "theorySummary": "Boundary Value Analysis complements Equivalence Partitioning by recognizing that defects concentrate overwhelmingly around boundaries rather than in the center of partitions."
    },
    {
        "id": "SE-04",
        "paper": "2022 May Revision",
        "questionNumber": 4,
        "topic": "White-Box Testing & Cyclomatic Complexity",
        "marks": 15.00,
        "difficulty": "Hard",
        "prompt": "A Control Flow Graph (CFG) for an algorithm has 14 edges ($E = 14$), 10 nodes ($N = 10$), and 1 connected component ($P = 1$).\n\nCalculate the Cyclomatic Complexity $V(G)$ using McCabe's formula $V(G) = E - N + 2P$ and identify the number of linearly independent basis paths.",
        "type": "multipart",
        "subquestions": [
            {
                "id": "sq1",
                "label": "Cyclomatic Complexity V(G):",
                "type": "text",
                "answer": "6",
                "acceptedAnswers": ["6"],
                "hint": "V(G) = E - N + 2P = 14 - 10 + 2(1) = 4 + 2 = 6."
            },
            {
                "id": "sq2",
                "label": "Number of linearly independent basis paths:",
                "type": "text",
                "answer": "6",
                "acceptedAnswers": ["6"],
                "hint": "McCabe's Cyclomatic Complexity V(G) equals the exact number of independent basis paths required for 100% branch/statement coverage."
            }
        ],
        "theorySummary": "Cyclomatic Complexity V(G) measures code complexity and defines the upper bound for the number of test cases required to achieve branch coverage: V(G) = E - N + 2P or P + 1 (predicate nodes + 1)."
    }
]

# Output to JSON
output_path = "/home/dulith/Projects/net_exam_emulator/src/data/quizzes.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(modules_data, f, indent=2)

print(f"Successfully compiled all 4 modules to {output_path}")
for m_id, m in modules_data.items():
    print(f" - {m_id} ({m['title']}): {len(m['questions'])} comprehensive questions")
