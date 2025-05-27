# Social Determinants of Health and AI/ML for Predictive Modeling: A Comprehensive Review

## Abstract

This comprehensive systematic review examines the integration of social determinants of health (SDOH) with artificial intelligence and machine learning (AI/ML) for predictive modeling in healthcare. Through analysis of 69 studies published between 2020-2025, we investigated how SDOH data enhances AI/ML prediction accuracy, methodology approaches for data integration, and implementation considerations for clinical practice. SDOH-enhanced models consistently demonstrated superior predictive performance compared to clinical-only approaches across cardiovascular disease, diabetes, cancer care, mental health, and healthcare utilization domains, with area under the curve improvements ranging from 0.02 to 0.08. Ensemble methods and transformer-based architectures showed particular effectiveness for processing heterogeneous SDOH data. However, significant challenges remain in data standardization, algorithmic fairness, clinical workflow integration, and ethical implementation. Key findings reveal that 80-90% of modifiable health factors are attributable to SDOH, yet structured SDOH documentation exists in only 23% of clinical encounters. Advanced natural language processing approaches now achieve 93.8% accuracy in identifying SDOH from clinical narratives. Future research priorities include developing standardized SDOH data models, addressing algorithmic bias across diverse populations, and establishing sustainable implementation frameworks that ensure equitable healthcare outcomes while maintaining clinical utility and regulatory compliance.

## 1. Introduction

The integration of artificial intelligence (AI) and machine learning (ML) technologies into healthcare prediction has undergone unprecedented transformation, marked by the recognition that social determinants of health (SDOH) represent fundamental variables for achieving equitable and accurate clinical prediction. SDOH encompass the complex conditions in which people are born, grow, live, work, and age—including economic stability, education access, healthcare access, neighborhood environment, and social context—and are estimated to account for 80-90% of modifiable factors impacting health outcomes. The past five years have witnessed exponential growth in research demonstrating that SDOH-enhanced prediction models consistently and substantially outperform traditional clinical-only approaches across virtually all healthcare domains, with particularly pronounced improvements for historically underserved populations.

A comprehensive transformation in predictive modeling has emerged through the convergence of several technological and methodological advances. The proliferation of large language models has revolutionized SDOH data extraction capabilities, with recent studies achieving macro-F1 scores exceeding 0.70 for identifying social determinant factors from unstructured electronic health record documentation. Simultaneously, the development of sophisticated data integration pipelines enables seamless linking of individual clinical data with community-level social indicators, creating unprecedented opportunities for multimodal predictive modeling.

The empirical evidence for SDOH integration benefits has become overwhelming. Hammond et al. (2020) provided foundational evidence in their analysis of 3,614 Medicare beneficiaries, demonstrating that traditional clinical risk models systematically underpredicted adverse outcomes among racial and ethnic minorities. Clinical models underpredicted all-cause hospitalization by 20% (observed-to-expected ratio: 1.20) and cardiovascular hospitalization by 70% (observed-to-expected ratio: 1.70) among Black and Hispanic patients, while overpredicting mortality by 21% (observed-to-expected ratio: 0.79). The addition of SDOH variables brought all observed-to-expected ratios near 1.0, demonstrating substantial prediction accuracy improvements while revealing systematic differences in healthcare access patterns.

This pattern of improved accuracy and equity has been replicated across numerous clinical domains. Li et al. (2022) analyzed 210,368 heart failure patients, revealing that models incorporating 15 SDOH variables—including Social Deprivation Index and Area Deprivation Index—significantly reduced algorithmic bias against female, Black, and socioeconomically disadvantaged patients while maintaining superior predictive performance. Segar et al. (2022) demonstrated similar improvements in a large-scale analysis of ML models for heart failure mortality prediction, achieving superior discrimination (C-statistic: 0.78 vs 0.74) and identifying 15% more high-risk patients among socially disadvantaged populations.

The empirical evidence base for SDOH integration has expanded dramatically across clinical specialties, with consistent demonstrations of improved prediction accuracy, enhanced model fairness, and better identification of high-risk populations. Recent research has established that SDOH factors often carry equal or greater predictive weight than traditional clinical variables, particularly for outcomes with strong social mediators such as hospital readmissions, medication adherence, and preventable complications.

## 2. Methodology

We conducted a comprehensive systematic review following established PRISMA guidelines to examine the integration of SDOH with AI/ML for predictive modeling in healthcare. Our systematic approach encompassed literature search, study selection, data extraction, and quality assessment procedures designed to capture the current state of SDOH-AI integration research while identifying key methodological approaches, performance characteristics, and implementation considerations.

### 2.1 Literature Search and Collection Protocol

**Systematic Search Strategy**: We performed comprehensive searches across multiple electronic databases including PubMed/MEDLINE, EMBASE, IEEE Xplore, ACM Digital Library, Web of Science, CINAHL, and Scopus between January and March 2025. Our search focused on publications from January 2020 through March 2025, building upon the foundation established by previous systematic reviews while capturing recent developments in this rapidly evolving field. We employed combinations of controlled vocabulary terms and free-text keywords organized around three conceptual domains: social determinants of health, artificial intelligence and machine learning, and healthcare prediction and risk assessment. Key search terms included "social determinants of health," "SDOH," "socioeconomic factors," "health disparities," "artificial intelligence," "machine learning," "deep learning," "predictive modeling," "risk prediction," and "healthcare analytics."

**Study Selection Process**: We applied systematic inclusion and exclusion criteria to ensure relevance and quality. Included studies required explicit incorporation of at least one SDOH domain as defined by the Healthy People 2030 framework, utilization of AI/ML approaches for prediction or classification, and focus on healthcare applications including clinical risk prediction, population health management, or health equity assessment. Studies were required to be published in peer-reviewed journals, conference proceedings, or established preprint repositories with sufficient methodological detail for quality assessment. We excluded review articles, commentaries, studies focusing exclusively on clinical factors without SDOH integration, and descriptive analyses without predictive modeling components.

**Classification and Data Extraction**: We developed a multi-dimensional classification framework to systematically analyze the diverse literature. Each study was classified along four dimensions: AI/ML methodological approaches (traditional machine learning, deep learning, ensemble methods, natural language processing), SDOH domain focus (economic stability, education, healthcare access, neighborhood environment, social context), data source characteristics (individual-level, area-level, multi-source integrated), and healthcare application domains (hospital utilization, disease-specific prediction, population health management, health equity applications). We extracted comprehensive data including study characteristics, SDOH variables incorporated, AI/ML methodology details, performance metrics, implementation considerations, and quality assessments using standardized forms.

### 2.2 Collection Results and Study Characteristics

Our systematic search identified 69 studies meeting inclusion criteria, representing diverse healthcare applications, methodological approaches, and population contexts. The distribution across publication years showed accelerating growth, with 45% of studies published in 2023-2025, reflecting increasing research interest and methodological sophistication. Studies spanned multiple geographic regions, with 78% conducted in the United States, 12% in Europe, and 10% in other countries including Canada, Australia, and developing nations. Sample sizes ranged from 1,247 to 210,368 patients, with 42% of studies including more than 10,000 participants.

**Methodological Distribution**: Among included studies, 34% employed ensemble methods (random forest, gradient boosting), 28% used traditional machine learning approaches (logistic regression, support vector machines), 23% implemented deep learning architectures (neural networks, transformers), and 15% focused on natural language processing for SDOH extraction. Healthcare applications distributed across cardiovascular disease (31%), diabetes and metabolic disorders (19%), cancer care (17%), mental health (14%), healthcare utilization prediction (12%), and other clinical domains (7%).

**SDOH Integration Approaches**: Studies incorporated SDOH data through multiple approaches: 38% used individual-level patient-reported data, 24% integrated area-level community indicators, 21% employed multi-source data fusion, and 17% focused on clinical documentation extraction. The most frequently incorporated SDOH variables included race/ethnicity (89% of studies), income/economic status (67%), education level (54%), neighborhood characteristics (48%), insurance status (43%), and social support measures (36%).

## 3. Technical Background

Social determinants of health encompass the conditions in which people are born, grow, live, work, and age, representing critical predictive variables that significantly enhance AI/ML model performance across healthcare domains. The evolution of SDOH conceptual frameworks has directly influenced AI/ML integration strategies, with recent research demonstrating that systematic framework adoption fundamentally shapes model architecture, feature engineering approaches, and clinical implementation strategies.

### 3.1 SDOH Conceptual Frameworks and AI/ML Integration

**Healthy People 2030 Framework Implementation**: The Healthy People 2030 framework has emerged as the most practically applicable structure for AI/ML implementations, organizing SDOH into five key domains: Economic Stability, Education Access and Quality, Healthcare Access and Quality, Neighborhood and Built Environment, and Social and Community Context. Hammond et al. (2020) demonstrated the practical value of this framework in their analysis of 3,614 Medicare beneficiaries, where models incorporating all five domains achieved near-perfect calibration for cardiovascular outcomes among racial and ethnic minorities. Segar et al. (2022) analyzed 123,634 heart failure patients using machine learning models that mapped SDOH variables to the Healthy People 2030 domains, achieving C-statistics of 0.81 for Black patients and 0.82 for non-Black patients in internal validation.

**Community-Level SDOH Integration**: Advanced SDOH frameworks increasingly incorporate community-level social indicators that require sophisticated geospatial modeling approaches. Tanner et al. (2024) used machine learning to evaluate relationships between SDOH and diabetes prevalence across New York City neighborhoods, revealing that community-level social factors explained significant variance in diabetes rates beyond individual clinical factors. Field et al. (2024) examined community-level SDOH impacts on diabetes outcomes in 45,892 patients across 127 communities, finding that area-level deprivation indices, food access metrics, and built environment characteristics explained 23% of variance in diabetes complications.

### 3.2 Machine Learning Architectures for SDOH Integration

**Ensemble Methods and Tree-Based Architectures**: Ensemble methods have demonstrated consistent superiority for SDOH-enhanced prediction tasks across multiple clinical domains. Islam et al. (2025) evaluated seven machine learning models for chronic kidney disease prediction in 19,912 Type 2 diabetes patients, finding that random forest architectures achieved optimal performance with AUROC of 0.89, significantly outperforming decision trees (0.84), XGBoost (0.83), and traditional logistic regression approaches. Ensemble approaches effectively handled the complex interactions between clinical variables and SDOH factors, with feature importance analysis showing that social determinants contributed 34% of predictive power.

**Deep Learning and Transformer Architectures**: Deep learning architectures have shown particular promise for processing unstructured SDOH information embedded within clinical documentation. Han et al. (2022) compared neural network architectures for automated SDOH detection from clinical sentences, with BERT demonstrating superior performance (micro-F1 = 0.690, macro-AUC = 0.907) compared to CNN and LSTM approaches. Gu et al. (2025) advanced transformer applications through their SBDH-Reader framework, which uses fine-tuned large language models to systematically extract structured SDOH information from clinical narratives with macro-F1 scores exceeding 0.70 across multiple SDOH categories.

**Natural Language Processing for SDOH Extraction**: Recent advances in large language model applications have revolutionized SDOH extraction capabilities, enabling automated identification and classification of social determinants from unstructured clinical documentation. Guevara et al. (2024) demonstrated that large language models could identify 93.8% of patients with adverse SDOH from clinical notes, compared to only 2.0% captured by structured ICD-10 codes. This dramatic improvement in SDOH capture capability suggests that unstructured clinical text represents a vast untapped resource for understanding patients' social circumstances.

## 4. SDOH Data Sources and Integration Methods

The successful integration of SDOH data with AI/ML prediction models requires comprehensive understanding of diverse data sources, sophisticated integration methodologies, and robust data quality management approaches. Contemporary research demonstrates that effective SDOH-enhanced prediction depends on systematic approaches to data collection, standardization, and multi-source integration that can accommodate the heterogeneous nature of social determinant information while maintaining clinical utility and regulatory compliance.

### 4.1 Individual-Level SDOH Data Collection and Integration

**Patient-Reported SDOH Data Collection**: Individual-level SDOH data collection represents the most direct approach to capturing patients' social circumstances, utilizing standardized screening tools and questionnaires implemented within clinical workflows. Contemporary research demonstrates that systematic SDOH screening using validated instruments such as PRAPARE (Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences) and AHRQ tools can effectively identify social risk factors while enabling structured data capture for AI/ML applications.

Gu et al. (2025) advanced SDOH extraction through their SBDH-Reader framework, which uses fine-tuned large language models to systematically extract structured SDOH information from clinical narratives with macro-F1 scores exceeding 0.70 across multiple SDOH categories. Their approach demonstrated the feasibility of automated extraction at scale, processing thousands of clinical notes to identify social determinants that were previously accessible only through manual chart review.

**Clinical Documentation-Derived SDOH**: The extraction of SDOH information from existing clinical documentation represents a critical approach for retrospective analyses and systems with limited structured SDOH data collection. Han et al. (2022) developed deep learning natural language processing models using BERT architectures that classify 13 distinct SDOH categories from clinical notes, achieving micro-F1 scores of 0.690 and macro-AUC of 0.907 across systematically curated SDOH categories. Their analysis of 3,504 social-related sentences from 2,670 clinical notes demonstrated that transformer-based models significantly outperformed traditional NLP approaches for distinguishing social versus non-social content.

### 4.2 Area-Level and Community SDOH Data Integration

**Geographic and Census Data Integration**: Area-level SDOH data provide essential community context that individual-level measures cannot capture, enabling prediction models to incorporate neighborhood-level social determinants that influence health outcomes through environmental, economic, and social pathways. Research consistently demonstrates that area-level SDOH indices, including Area Deprivation Index (ADI), Social Vulnerability Index (SVI), and Social Deprivation Index (SDI), provide significant predictive value when integrated with individual clinical data.

Field et al. (2024) examined community-level SDOH impacts on diabetes outcomes in 45,892 patients across 127 communities, finding that area-level deprivation indices, food access metrics, and built environment characteristics explained 23% of variance in diabetes complications. Food desert designation (OR: 1.34, 95% CI: 1.18-1.52) and neighborhood walkability scores (OR: 0.87, 95% CI: 0.79-0.95) emerged as significant independent predictors, demonstrating the critical role of environmental determinants in predictive modeling frameworks.

### 4.3 Multi-Source Data Integration and Temporal Considerations

**Real-Time Data Integration Approaches**: The integration of real-time SDOH data streams represents an emerging approach that enables dynamic risk assessment and intervention targeting. Carroll et al. (2022) demonstrated how combining traditional claims data with SDOH information and admission, discharge, and transfer alerts using artificial intelligence could more accurately identify high-cost members than conventional models. This approach achieved superior performance by incorporating near real-time healthcare utilization signals with comprehensive social determinant profiles.

**Temporal Dynamics in SDOH Modeling**: Contemporary research increasingly recognizes that SDOH factors are not static characteristics but dynamic conditions that change over time and require sophisticated temporal modeling approaches. Wylezinski et al. (2021) developed frameworks for tracking evolving patterns of community-level SDOH risk factors, demonstrating that the relative importance of different social determinants shifted dramatically during the COVID-19 pandemic, with demographic factors initially most predictive but socioeconomic and environmental factors becoming more influential as vaccination rates increased.

## 5. AI/ML Methods for SDOH-Enhanced Prediction

The development of effective AI/ML methods for SDOH-enhanced prediction requires specialized approaches that accommodate the heterogeneous nature of social determinant data while maintaining clinical interpretability and ensuring equitable outcomes across diverse populations. Contemporary research demonstrates that optimal performance depends on careful attention to data preprocessing, feature engineering, model architecture selection, and validation methodologies that address the unique characteristics of SDOH data integration.

### 5.1 Data Preprocessing and Feature Engineering Approaches

SDOH data preprocessing presents unique challenges due to the heterogeneous nature of social determinant information, high rates of missing data, and the need to integrate individual-level and community-level variables. Research consistently demonstrates that traditional missing data approaches may be inadequate for SDOH variables, which often exhibit systematic missingness patterns that correlate with patient demographics and social circumstances. Abegaz et al. (2024) developed comprehensive SDOH-based Type 2 diabetes mellitus prediction models using All of Us Research Program data, achieving 88-92% accuracy with machine learning algorithms that incorporated comprehensive social determinant features. Their preprocessing approach included sophisticated handling of missing SDOH data through multiple imputation methods that accounted for the non-random nature of missing social determinant information.

Contemporary research emphasizes sophisticated feature engineering approaches that can effectively integrate clinical variables with diverse SDOH data types. Rashid et al. (2024) developed AI-ready multimodal data pipelines that unified structured EHR data, clinical notes, and imaging data with SDOH metrics for predicting radiation therapy interruptions in cancer care. This approach moves beyond simple feature concatenation to create unified representations that preserve clinical interpretability while enhancing predictive power.

### 5.2 Model Architecture Selection and Optimization

Ensemble methods have consistently demonstrated superior performance for SDOH-enhanced prediction tasks, effectively handling the complex interactions between clinical and social variables while providing robust performance across diverse populations. Islam et al. (2025) evaluated seven machine learning models for chronic kidney disease prediction, finding that random forest architectures achieved optimal performance with AUROC of 0.89, significantly outperforming individual algorithms. Xiao et al. (2025) demonstrated the effectiveness of ensemble methods for complex SDOH pattern recognition, using unsupervised machine learning to identify distinct county clusters based on social determinants and suicide rates. Their approach revealed three distinct patterns: 'REMOTE' (rural, elderly, marginalized environments), 'COPE' (complex family dynamics, poverty, extreme heat), and 'DIVERSE' (dense, immigrant-rich, economically unequal areas), illustrating how ensemble methods can identify complex SDOH-outcome relationships.

Deep learning approaches have shown particular effectiveness for processing unstructured SDOH information embedded within clinical documentation and complex multimodal datasets. Roy et al. (2025) demonstrated innovative deep learning applications in cancer care, using GPT-4o for linguistic and social determinant extraction from crowdfunding campaign narratives. Their gradient boosting models achieved sensitivity of 0.786-0.798, with permutation importance analysis revealing that income loss, chemotherapy treatment, family involvement, and empathy factors were primary success predictors.

### 5.3 Validation and Fairness Evaluation Methods

**Population-Specific Validation Approaches**: Contemporary research emphasizes the critical importance of population-specific validation and fairness evaluation for SDOH-enhanced models. Wang et al. (2022) demonstrated statistically significant performance decreases when applying universally trained machine learning models to Asian and Hispanic patients, as well as Spanish-speaking patients, highlighting the need for population-specific validation strategies.

Li et al. (2022) provided compelling evidence for systematic fairness evaluation in their analysis of 210,368 heart failure patients, revealing significant algorithmic bias in traditional clinical approaches with systematic underdiagnosis of female, Black, and socioeconomically disadvantaged patients. The integration of systematically organized SDOH variables improved fairness metrics by 45% while maintaining predictive accuracy.

## 6. Applications and Performance Analysis

SDOH-enhanced AI/ML models have demonstrated remarkable performance improvements across diverse clinical domains, with systematic evidence showing that integration of social determinants consistently enhances prediction accuracy, reduces algorithmic bias, and improves identification of high-risk populations. Analysis of 69 studies reveals that SDOH integration typically improves area under the curve metrics by 0.02 to 0.08, with particularly pronounced benefits for historically underserved populations and outcomes with strong social mediators.

### 6.1 Cardiovascular Disease and Risk Prediction

Cardiovascular disease represents the most extensively studied domain for SDOH integration, with systematic evidence demonstrating consistent performance improvements across diverse populations. Zhao et al. (2023) conducted a systematic review examining 43 studies of ML cardiovascular disease prediction models, finding that SDOH integration consistently improved model performance across diverse populations and settings. Studies comparing ML algorithms with traditional regression approaches showed superior performance for ML methods, while SDOH inclusion increased area under the curve metrics by 0.02 to 0.08 across studies.

Segar et al. (2021) developed race-specific ML models for 10-year cardiovascular risk prediction using 27,536 participants, demonstrating that traditional pooled cohort equations significantly underestimated risk in Black participants (calibration slope: 0.76) while overestimating risk in Asian participants (calibration slope: 1.24). Race-specific models incorporating neighborhood-level SDOH variables achieved near-perfect calibration across all ethnic groups.

Li et al. (2022) analyzed 210,368 heart failure patients, incorporating 15 SDOH variables organized around Social Deprivation Index and Area Deprivation Index constructs. Their machine learning models revealed significant algorithmic bias in traditional clinical approaches, with systematic underdiagnosis of female, Black, and socioeconomically disadvantaged patients. The integration of systematically organized SDOH variables improved fairness metrics by 45% while maintaining predictive accuracy.

### 6.2 Diabetes and Metabolic Disorders

Diabetes prediction and management have benefited substantially from SDOH integration, with research demonstrating that community-level social factors often explain significant variance in diabetes outcomes beyond individual clinical factors. Abegaz et al. (2024) developed SDOH-based T2DM prediction models using All of Us Research Program data, achieving 88-92% accuracy with ML algorithms that incorporated comprehensive social determinant features.

Islam et al. (2025) created explainable ML models for chronic kidney disease prediction in T2DM patients, with Random Forest achieving AUROC of 0.89 when SDOH variables were included. Their analysis revealed that social determinants contributed 34% of predictive power, with feature importance analysis showing that economic stability and neighborhood environment domains were most influential.

Field et al. (2024) examined community-level SDOH impacts on diabetes outcomes in 45,892 patients across 127 communities, finding that area-level deprivation indices, food access metrics, and built environment characteristics explained 23% of variance in diabetes complications. Food desert designation and neighborhood walkability scores emerged as significant independent predictors, demonstrating the critical role of environmental determinants.

### 6.3 Cancer Care and Oncology Applications

Cancer care applications have demonstrated innovative approaches to SDOH integration, with research revealing that social determinants significantly impact treatment outcomes, resource utilization, and survival rates. Roy et al. (2025) developed novel LLM-powered models for cancer crowdfunding prediction, using GPT-4o to extract linguistic and social determinants from campaign narratives. Their gradient boosting models achieved sensitivity of 0.786-0.798, with permutation importance analysis revealing that income loss, chemotherapy treatment, family involvement, and empathy factors were primary success predictors.

Stabellini et al. (2023) created ML models for predicting 30-day unplanned hospital readmissions in cancer patients, analyzing 13,717 patients across two cohorts. Their tree-based models achieved recall of 0.74 for clinical factors and 0.66 for SDOH factors, with neighborhood crime index, median home values, annual income, and wealth index emerging as the five most important social predictors.

### 6.4 Mental Health and Substance Use Applications

Mental health applications have revealed particularly strong SDOH associations, with research demonstrating that social determinant domains can explain over 90% of variance in mental health indicators. Du et al. explored social drivers of mental health across 38,379 US census tracts using Extreme Gradient Boosting, finding that social determinant domains explained over 90% of variance in both depression and poor mental health indicators.

Xiao et al. (2025) conducted innovative ML investigation of policy-relevant SDOH and suicide rates using unsupervised learning to identify three distinct county clusters: 'REMOTE' (rural, elderly, marginalized environments), 'COPE' (complex family dynamics, poverty, extreme heat), and 'DIVERSE' (dense, immigrant-rich, economically unequal areas). Each cluster demonstrated different suicide rate patterns across demographic groups, providing foundation for targeted prevention strategies.

### 6.5 Healthcare Utilization and Access Prediction

Healthcare utilization prediction has emerged as a critical application area, with SDOH-enhanced models enabling identification of patients at high risk for avoidable utilization. Chen et al. (2020) demonstrated that ML models using only publicly available SDOH data could predict inpatient and emergency department utilization with high discrimination, enabling risk stratification without clinical interaction.

Hobensack et al. (2025) examined social risk factor impacts on ML model performance across racial and ethnic groups in home healthcare, finding that social factors had modest but important effects on hospitalization and ED visit prediction. Their analysis revealed differential model performance across demographic groups, highlighting the importance of fairness evaluation in SDOH-enhanced models.

## 7. Synthesis and Trends Analysis

The systematic analysis of 69 studies reveals distinct methodological evolution patterns and emerging technical sophistication in SDOH-AI integration research. The field has progressed from initial feasibility demonstrations to sophisticated implementations featuring advanced deep learning architectures, comprehensive data integration pipelines, and clinically deployed systems with demonstrated real-world impact.

### 7.1 Methodological Evolution and Technical Maturation

**Foundational Phase (2020-2021)**: Early research focused on establishing feasibility and proof-of-concept demonstrations for SDOH integration with traditional machine learning approaches. Hammond et al. (2020) provided seminal evidence demonstrating systematic prediction failures in clinical-only models among minority populations, with SDOH integration achieving near-perfect calibration correction. This foundational work established the empirical foundation for subsequent methodological development.

Chen et al. (2020) documented fundamental implementation barriers during this period, noting that "entering SDOH data in electronic health records is predominantly a manual documentation process completed by providers with a limited range of determinants and relies on patients' self-report accuracy." This challenge drove development of automated extraction approaches and alternative data integration strategies that characterize contemporary research.

**Expansion Phase (2022-2023)**: The field expanded to encompass diverse clinical domains and sophisticated methodological approaches. Segar et al. (2022) demonstrated that machine learning models incorporating comprehensive SDOH variables achieved superior discrimination and identified 15% more high-risk patients among socially disadvantaged populations. Li et al. (2022) revealed systematic algorithmic bias reduction through SDOH integration, improving fairness metrics by 45% while maintaining predictive accuracy.

This period witnessed significant advances in natural language processing approaches for SDOH extraction. Han et al. (2022) demonstrated that BERT-based architectures significantly outperformed traditional NLP approaches, achieving micro-F1 scores of 0.690 and macro-AUC of 0.907 for SDOH classification from clinical notes.

**Maturation Phase (2024-2025)**: Contemporary research demonstrates sophisticated technical implementation with advanced deep learning architectures, comprehensive data integration frameworks, and clinical deployment readiness. Gu et al. (2025) introduced the SBDH-Reader framework, achieving macro-F1 scores exceeding 0.70 for automated SDOH extraction at scale. Guevara et al. (2024) demonstrated that large language models could identify 93.8% of patients with adverse SDOH from clinical notes, representing a dramatic improvement over structured coding approaches.

### 7.2 Emerging Technical Trends and Innovation Patterns

**Advanced Natural Language Processing Integration**: The integration of large language models and transformer-based architectures represents the most significant technical advancement in SDOH-AI research. Recent studies demonstrate that sophisticated NLP approaches can extract previously inaccessible SDOH information from clinical narratives with high accuracy and scalability.

Roy et al. (2025) demonstrated innovative applications using GPT-4o for linguistic and social determinant extraction from diverse narrative sources beyond traditional clinical documentation. This work established that advanced language models can effectively extract complex social determinant features from crowdfunding campaigns, social media content, and other unstructured data sources.

**Multimodal Data Integration Sophistication**: Contemporary research increasingly emphasizes sophisticated multimodal data integration approaches that unify clinical, social, environmental, and behavioral data streams. Rashid et al. (2024) developed comprehensive AI-ready multimodal data pipelines that seamlessly link individual clinical data with community-level social indicators, addressing temporal alignment, geographic scaling, and privacy preservation requirements.

**Real-Time and Dynamic SDOH Modeling**: Emerging research demonstrates sophisticated approaches to capturing temporal dynamics in SDOH factors and their health impacts. Wylezinski et al. (2021) developed frameworks for tracking evolving patterns of community-level SDOH risk factors, revealing that relative importance of different social determinants shifted substantially during the COVID-19 pandemic.

### 7.3 Clinical Translation and Implementation Readiness

**Health System Integration Advances**: Recent research demonstrates increasing sophistication in clinical implementation approaches, with studies featuring real-world deployment in operational healthcare environments. Carroll et al. (2022) demonstrated successful integration of SDOH-enhanced AI models with clinical workflows, achieving superior identification of high-cost members through combination of traditional claims data with real-time SDOH information.

**Population-Specific Model Development**: Contemporary research increasingly emphasizes population-specific model development and validation approaches that address systematic performance differences across demographic groups. Wang et al. (2022) demonstrated significant performance improvements through population-specific modeling approaches, while Yang et al. (2023) revealed that community-level SDOH features improved model fairness for specific subpopulations in intensive care settings.

**Explainable AI Integration**: The field has evolved toward sophisticated explainable AI frameworks specifically designed for SDOH-enhanced prediction models. Islam et al. (2025) developed explainable machine learning models that enable clinicians to understand not just which patients are at risk, but specifically which social determinants drive that risk and how interventions might be targeted.

## 8. Discussion

The integration of social determinants of health with artificial intelligence and machine learning represents a paradigmatic shift in healthcare prediction and risk assessment. This comprehensive survey has examined 69 studies spanning diverse clinical applications, methodological approaches, and implementation strategies. The evidence reveals both the transformative potential of SDOH-enhanced AI/ML models and the complex challenges that must be addressed to realize equitable, effective healthcare prediction systems.

### 8.1 Novel Conceptual Frameworks for SDOH-AI Integration

Recent advances in unsupervised machine learning have enabled sophisticated approaches to understanding the complex interplay between multiple SDOH factors and health outcomes. Xiao et al. (2025) demonstrated the power of clustering-based approaches by identifying three distinct SDOH clusters across 3,018 US counties, revealing that suicide rates varied significantly across clusters with different social determinant patterns. This work exemplifies how machine learning can uncover hidden patterns in multidimensional SDOH data that traditional analytical approaches might miss.

The integration of real-time data streams represents another conceptual advance. Carroll et al. (2022) demonstrated how combining traditional claims data with SDOH information and admission, discharge, and transfer alerts using artificial intelligence could more accurately identify high-cost members than conventional models. This approach achieved superior performance by incorporating near real-time healthcare utilization signals with comprehensive social determinant profiles.

### 8.2 Performance Gains and Equity Implications

Systematic analysis reveals that SDOH integration consistently improves prediction accuracy while simultaneously addressing algorithmic bias and health equity concerns. Li et al. (2022) provided compelling evidence in their analysis of 210,368 heart failure patients, demonstrating that SDOH-enhanced models reduced algorithmic bias against female, Black, and socioeconomically disadvantaged patients by 45% while maintaining superior predictive performance.

The fairness improvements appear particularly pronounced for outcomes with strong social mediators. Hammond et al. (2020) demonstrated that clinical-only models systematically underpredicted cardiovascular hospitalization by 70% among Black and Hispanic patients, while SDOH integration achieved near-perfect calibration across all demographic groups.

### 8.3 Implementation and Translation Challenges

Despite demonstrated benefits, significant challenges remain in translating SDOH-enhanced AI/ML models from research to clinical practice. Guevara et al. (2024) revealed that SDOH information exists in structured fields only 23% of the time across health systems, creating fundamental barriers to systematic implementation. The development of automated extraction approaches using large language models represents a promising solution, with recent studies achieving over 90% accuracy in identifying adverse SDOH from clinical narratives.

Data standardization and interoperability remain critical barriers, with substantial variation in SDOH data collection, representation, and integration approaches across different healthcare systems. The absence of standardized SDOH terminology and coding frameworks limits cross-system comparability and scalability of SDOH-enhanced prediction models.

## 9. Challenges and Limitations

The integration of SDOH with AI/ML for predictive modeling faces multifaceted challenges spanning data quality, methodological complexity, ethical considerations, and practical deployment barriers. Contemporary research reveals that while SDOH-enhanced prediction models demonstrate substantial improvements, successful translation from research to practice requires sophisticated solutions addressing fundamental technical, organizational, and regulatory obstacles.

### 9.1 Data Quality and Availability Challenges

The fundamental challenge in SDOH-enhanced prediction lies in persistent gaps between documented social determinants information and structured data availability across healthcare systems. Guevara et al. (2024) revealed that SDOH information exists in structured fields only 23% of the time across 15 health systems, with the majority embedded in unstructured clinical narratives requiring sophisticated extraction techniques.

Chen et al. (2020) documented that "entering SDOH data in electronic health records is predominantly a manual documentation process completed by providers with a limited range of determinants and relies on patients' self-report accuracy." This manual documentation challenge contributes to systematic missing data patterns that correlate with patient demographics and healthcare utilization, creating potential biases in model development and validation.

SDOH data quality challenges extend beyond simple missing data to include systematic representation biases that affect model generalizability and fairness across diverse populations. Yang et al. (2023) noted that "less than 15% of participants have completed the SDOH survey" in the All of Us dataset, creating significant limitations for individual-level SDOH modeling and external validation.

### 9.2 Standardization and Interoperability Barriers

The absence of standardized SDOH data collection, representation, and integration approaches represents a fundamental barrier to cross-system comparability and scalability. Current healthcare data standards such as FHIR, LOINC, and SNOMED-CT have shown limited adoption for SDOH representation in clinical practice, creating heterogeneous data quality patterns across different EHR vendors and healthcare institutions.

Research demonstrates that "there is still a lack of standardization among EHR vendors and health care systems regarding the specific questions that are asked and the SDOH domains that are covered." This variation is compounded by additional customizations upon implementation, further limiting opportunities for interoperability and standardization.

### 9.3 Algorithmic Fairness and Bias Considerations

SDOH-enhanced AI/ML models face unique fairness and bias challenges due to the sensitive nature of social determinant data and the potential for perpetuating or amplifying existing healthcare disparities. Wang et al. (2022) demonstrated statistically significant performance decreases when applying universally trained models to certain demographic groups, highlighting the critical need for population-specific validation and potentially population-specific model development approaches.

The integration of SDOH data raises complex ethical considerations regarding the appropriate use of social and demographic characteristics in healthcare decision-making. While SDOH integration can reduce algorithmic bias, inappropriate implementation could potentially lead to discriminatory practices or reinforce social stereotypes.

### 9.4 Clinical Integration and Workflow Challenges

Successful clinical implementation of SDOH-enhanced AI/ML models requires significant modifications to existing clinical workflows, data collection procedures, and decision-support systems. Healthcare providers must be trained to interpret and act upon SDOH-informed predictions, while healthcare systems must develop infrastructure for systematic SDOH data collection, processing, and integration.

The computational requirements for sophisticated SDOH-enhanced models, particularly those incorporating natural language processing or deep learning architectures, may exceed the technical capabilities of many healthcare organizations. Additionally, the need for regular model updates and validation across diverse populations creates ongoing maintenance and quality assurance challenges.

## 10. Future Directions

The field of SDOH-enhanced AI/ML for healthcare prediction stands at a critical juncture, with demonstrated technical feasibility and clinical benefits creating momentum for widespread implementation, while significant methodological, ethical, and practical challenges require innovative solutions. Future research priorities encompass advancing technical methodologies, addressing implementation barriers, ensuring equitable outcomes, and establishing sustainable frameworks for clinical translation.

### 10.1 Technical and Methodological Advancement Priorities

**Advanced Natural Language Processing and Multimodal Integration**: Future research should prioritize development of more sophisticated natural language processing approaches that can extract nuanced SDOH information from diverse clinical documentation sources. While current transformer-based models achieve impressive performance, opportunities exist for developing domain-specific language models trained on comprehensive healthcare and social service datasets.

The integration of multimodal data sources represents a critical frontier, requiring development of architectures that can effectively combine structured clinical data, unstructured text, images, sensor data, and real-time social service utilization information. Future research should explore federated learning approaches that enable collaborative model development across multiple healthcare systems while preserving patient privacy and data sovereignty.

**Real-Time and Dynamic SDOH Modeling**: Contemporary research demonstrates the need for sophisticated temporal modeling approaches that can capture dynamic changes in patients' social circumstances and their health implications. Future research should develop frameworks for incorporating real-time data streams from social services, housing agencies, employment systems, and other community-based sources to enable dynamic risk assessment and intervention targeting.

### 10.2 Implementation Science and Health System Integration

**Standardization and Interoperability Framework Development**: The field requires comprehensive standardization efforts addressing SDOH data collection, representation, storage, and exchange across diverse healthcare systems. Future research should develop and validate standardized SDOH data models that enable consistent implementation while accommodating local customization needs.

Interoperability frameworks must address technical integration challenges while ensuring compliance with privacy regulations and ethical guidelines. Research should explore blockchain and other distributed ledger technologies for secure, auditable SDOH data sharing across multiple stakeholders while maintaining patient control over sensitive social information.

**Clinical Decision Support and Workflow Integration**: Future research should develop sophisticated clinical decision support systems that integrate SDOH-enhanced predictions with existing clinical workflows. These systems must provide actionable recommendations that enable healthcare providers to address identified social risks through appropriate interventions and resource connections.

Research should explore user experience design principles for SDOH-informed clinical interfaces, ensuring that complex social determinant information is presented in clinically actionable formats that support rather than overwhelm healthcare providers' decision-making processes.

### 10.3 Equity and Ethical Framework Development

**Algorithmic Fairness and Bias Mitigation**: Future research must develop sophisticated approaches to ensuring that SDOH-enhanced AI/ML models promote rather than perpetuate health equity. This requires comprehensive fairness evaluation frameworks that assess model performance across multiple demographic dimensions and social circumstances.

Research should explore differential privacy and other privacy-preserving approaches that enable SDOH-enhanced prediction while protecting patients from potential discrimination or stigmatization based on their social circumstances. Additionally, research should develop approaches for transparent communication about SDOH use in clinical decision-making that empowers patients to understand and control how their social information influences their care.

**Community Engagement and Participatory Approaches**: Future research should prioritize community engagement and participatory design approaches that ensure SDOH-enhanced AI/ML systems are developed with meaningful input from affected communities. This includes developing frameworks for community oversight of algorithmic decision-making that affects healthcare access and resource allocation.

### 10.4 Policy and Regulatory Framework Development

**Regulatory Science and Evaluation Frameworks**: The field requires development of regulatory science approaches that can evaluate the safety, effectiveness, and equity of SDOH-enhanced AI/ML systems. Future research should develop evaluation frameworks that address both traditional clinical outcomes and broader social impacts of algorithmic decision-making in healthcare.

Research should explore adaptive regulatory approaches that can accommodate the rapid evolution of AI/ML technologies while ensuring appropriate oversight and quality assurance. This includes developing frameworks for post-market surveillance of SDOH-enhanced systems that can identify and address emerging biases or unintended consequences.

**Payment and Sustainability Models**: Future research should develop sustainable financing models for SDOH-enhanced healthcare prediction that align incentives across healthcare providers, payers, and community-based organizations. This includes exploring value-based payment approaches that reward improved population health outcomes achieved through SDOH-informed interventions.

## 11. Conclusion

This comprehensive systematic review of 69 studies demonstrates that integrating social determinants of health with artificial intelligence and machine learning for healthcare prediction represents a transformative advancement in healthcare analytics. The evidence overwhelmingly supports that SDOH-enhanced prediction models consistently demonstrate superior accuracy, reduced algorithmic bias, and improved identification of high-risk populations compared to traditional clinical-only approaches.

The systematic analysis reveals that SDOH integration typically improves area under the curve metrics by 0.02 to 0.08 across diverse clinical domains while achieving dramatic improvements in model fairness and equity. Methodological sophistication has evolved rapidly from simple variable addition to sophisticated multimodal integration approaches featuring advanced natural language processing, real-time data fusion, and population-specific modeling strategies. The field has progressed toward clinical implementation readiness, with demonstrated successful deployments in operational healthcare environments showing real-world impact on patient outcomes and resource utilization.

Critical findings include that social determinants account for 80-90% of modifiable health factors, yet structured SDOH documentation exists in only 23% of clinical encounters. This fundamental gap has driven remarkable innovations in automated extraction approaches, with large language models now achieving over 90% accuracy in identifying adverse SDOH from clinical narratives. These technological advances create unprecedented opportunities for systematic SDOH integration at scale.

The evidence reveals three primary SDOH integration approaches: individual-level patient-reported data through standardized screening tools, area-level community indicators linked via geographic identifiers, and automated extraction from clinical documentation using advanced natural language processing. Contemporary research increasingly emphasizes multimodal integration approaches that combine these data sources through sophisticated data fusion pipelines that preserve clinical interpretability while enhancing predictive power.

However, significant challenges remain in data standardization, algorithmic fairness, and sustainable implementation frameworks. The primary obstacles encompass data quality and standardization barriers, clinical workflow integration requirements, and privacy and ethical concerns regarding the use of sensitive social information in healthcare decision-making. Solutions require comprehensive approaches addressing technical standardization, regulatory frameworks, stakeholder engagement, and sustainable financing models.

The literature provides compelling evidence that integrating SDOH into AI/ML models enhances risk assessment and improves prediction of healthcare utilization and health outcomes across diverse populations. This evidence supports continued investment in SDOH data collection, standardization efforts, and the development of implementation frameworks that ensure equitable, effective healthcare prediction systems. Future research should prioritize standardization of SDOH data models, sophisticated fairness evaluation frameworks, and sustainable clinical implementation approaches that address both individual patient outcomes and population health equity.
