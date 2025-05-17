## 2. Methodology

### 2.1 Literature Search and Collection Protocol

#### Systematic Review Approach

Our methodological approach for this comprehensive review of social determinants of health (SDOH) and AI/ML for predictive modeling followed established principles for systematic reviews. We adhered to the PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses) guidelines to ensure transparency, reproducibility, and methodological rigor throughout the review process [PRISMA guidelines reference with details on how they were implemented in this specific review]. The protocol for this review was registered with PROSPERO (International Prospective Register of Systematic Reviews) prior to the initiation of the search process to minimize bias and provide a public record of our intended methodology [PROSPERO registration number and details].

A team of reviewers with diverse expertise in medical informatics, data science, public health, and clinical care conducted the review. To ensure consistency and minimize individual biases, we established a standardized reviewer training process and conducted regular calibration exercises throughout the review timeline [Description of reviewer training and calibration process, potential reference to similar approaches in other systematic reviews].

#### Article Collection Process

Our search strategy was designed to comprehensively identify literature at the intersection of social determinants of health and artificial intelligence/machine learning approaches applied to healthcare prediction. We conducted systematic searches across multiple electronic databases between January and March 2025, focusing on publications from January 2020 through March 2025. This timeframe was selected to capture recent developments while building upon the foundation established by previous systematic reviews, particularly the work by Chen and colleagues (2020) [Chen et al., 2020 systematic review on social determinants in EHR and their impact on analysis and risk prediction].

The following electronic databases were systematically searched: PubMed/MEDLINE, EMBASE, IEEE Xplore, ACM Digital Library, Web of Science, CINAHL, and Scopus. Additionally, we performed targeted searches in specialized repositories including arXiv, medRxiv, and relevant AI/ML conference proceedings (including NeurIPS, AAAI, AMIA, and MLHC) to identify relevant preprints and conference papers not yet indexed in traditional biomedical databases [Specific search strategies for each database with exact search terms, boolean operators, and filters applied].

Our search strategy employed combinations of controlled vocabulary terms (MeSH, Emtree) and free-text keywords organized around three conceptual domains: (1) social determinants of health, (2) artificial intelligence and machine learning, and (3) healthcare prediction and risk assessment. Key search terms included but were not limited to: "social determinants of health," "SDOH," "socioeconomic factors," "health disparities," "social risk," "artificial intelligence," "machine learning," "deep learning," "natural language processing," "predictive modeling," "risk prediction," "clinical decision support," and "healthcare analytics" [Complete list of search terms and search strategies for each database provided in an appendix].

To ensure comprehensive coverage without excessive irrelevant results, we iteratively refined our search strategy through pilot searches and consultation with information specialists. All search results were imported into citation management software for deduplication and screening management [Description of citation management tools and deduplication process].

### 2.2 Paper Selection Criteria

#### Inclusion Criteria

Our review incorporated studies that met a comprehensive set of inclusion criteria designed to ensure relevance and quality. We included original research articles describing empirical studies, methodological developments, system implementations, or evaluations related to SDOH and AI/ML integration [Reference to similar inclusion criteria from established review methodologies]. Studies were required to explicitly incorporate at least one social determinant domain as defined by the Healthy People 2030 framework, which includes economic stability, education access and quality, healthcare access and quality, neighborhood and built environment, or social and community context [Reference to HP2030 SDOH framework and definitions]. Additionally, eligible studies needed to utilize artificial intelligence or machine learning approaches for prediction, classification, pattern recognition, or automated analysis [Reference to AI/ML taxonomy or classification framework].

We focused specifically on healthcare applications, including but not limited to clinical risk prediction, population health management, health service utilization forecasting, or health equity assessment [Reference to healthcare predictive modeling applications]. Publication requirements stipulated that studies must be published in peer-reviewed journals, conference proceedings, or established preprint repositories between January 2020 and March 2025, a timeframe selected to build upon the foundation established by Chen et al.'s 2020 review [Justification for date range, building on Chen et al. 2020]. We limited our analysis to studies with full text available in English, acknowledging the potential bias this introduces [Standard language limitation with acknowledgment of potential bias]. Finally, included studies needed to provide sufficient methodological detail to enable quality assessment and data extraction according to established reporting guidelines for AI/ML in healthcare [Reference to reporting guidelines for AI/ML in healthcare].

#### Exclusion Criteria

We systematically excluded certain types of publications to maintain the focus and quality of our review. Review articles, commentaries, editorials, opinion pieces, or theoretical papers without original data or analysis were excluded, though these were cataloged separately for background context [Standard exclusion criteria for systematic reviews]. Studies focusing exclusively on clinical or biological factors without integration of social determinants were omitted as they did not address our core research questions regarding SDOH-AI integration [Justification for excluding clinical-only models]. Similarly, descriptive or exploratory analyses without a predictive modeling component were excluded to maintain our focus on predictive applications rather than descriptive analytics [Differentiation between predictive and descriptive analytics].

We limited our scope to healthcare applications, excluding AI/ML implementations in other domains such as education, criminal justice, or social services [Rationale for healthcare focus]. Studies where SDOH factors were analyzed only as outcomes rather than predictive variables were excluded as they did not align with our research questions about using SDOH to predict health outcomes [Clarification of directionality of interest]. Conference abstracts, posters, or proceedings with insufficient methodological detail for quality assessment were excluded due to limited information for rigorous evaluation [Quality threshold justification]. Finally, when multiple publications reported on the same study results, we included only the most comprehensive or recent publication to avoid duplicate representation [Approach to handling multiple publications from same study].

The title and abstract screening was conducted independently by two reviewers using a standardized screening form. Discrepancies were resolved through discussion, with a third reviewer consulted when consensus could not be reached. All potentially relevant articles then underwent full-text review by two independent reviewers to determine final inclusion based on the criteria above. The inter-reviewer agreement was calculated using Cohen's kappa, with values exceeding 0.80 considered indicative of strong agreement [Reference to standard measures of inter-reviewer reliability].

### 2.3 Classification Framework for Selected Articles

#### Classification Dimensions

To systematically analyze the diverse literature at the intersection of SDOH and AI/ML in healthcare, we developed a multi-dimensional classification framework. This framework enabled structured characterization of studies along key dimensions relevant to our research questions and facilitated identification of patterns and gaps in the literature [Reference to similar classification approaches in systematic reviews of complex healthcare technologies].

Our classification framework incorporated five primary dimensions. First, the SDOH Domain Focus dimension categorized studies according to the Healthy People 2030 framework domains (economic stability, education access and quality, healthcare access and quality, neighborhood and built environment, social and community context) [HP2030 reference]. This classification captured which social determinant domains were incorporated in each predictive model, with categories for both single-domain and multi-domain approaches. Second, in the AI/ML Methodological Approach dimension, studies were classified based on their primary computational techniques, including traditional machine learning (e.g., regression, decision trees, random forests, support vector machines), deep learning (e.g., neural networks, convolutional networks, transformers), natural language processing (rule-based, embedding methods, large language models), multi-modal approaches (combining multiple data types and algorithms), and causal inference methods (addressing confounding between clinical and social factors) [Reference to AI/ML taxonomy or classification framework].

The third dimension, Data Source Characteristics, categorized studies based on their primary SDOH data sources, including individual-level patient-reported data (surveys, screening tools), individual-level clinically documented data (structured EHR fields, clinical notes), area-level data (census, geographic indicators, community assessments), and multi-source integrated data (combinations of the above) [Reference to SDOH data source categorization frameworks]. Fourth, the Healthcare Application Domain dimension classified studies by their primary clinical or operational focus, such as hospital utilization prediction (readmissions, ED visits, length of stay), disease-specific risk prediction (by clinical condition), population health management (risk stratification, resource allocation), health equity applications (disparity identification, equity-focused interventions), and general methodology development [Reference to healthcare predictive analytics application taxonomy].

The fifth dimension, Implementation Maturity, categorized studies based on their stage in the translational pipeline, ranging from conceptual/developmental (initial algorithm development), retrospective validation (using historical data), prospective evaluation (real-world testing without clinical implementation), clinical implementation (integrated into workflows), to post-implementation evaluation (assessment of real-world impact) [Reference to implementation science frameworks for healthcare AI].

#### Classification Process

Each included study was independently classified by two reviewers using a standardized form with operational definitions for each category. Disagreements were resolved through discussion, with a third reviewer consulted when necessary. To ensure consistent application of the classification framework, we conducted initial calibration exercises with all reviewers using a sample of diverse articles, refining category definitions based on feedback.

For studies that spanned multiple categories within a dimension (e.g., addressing multiple SDOH domains or employing several AI/ML techniques), we recorded all applicable categories while identifying the primary focus for summary analyses. This approach allowed both focused categorization and recognition of studies with broader scope. Inter-reviewer agreement for classification was assessed using Cohen's kappa, with values exceeding 0.75 considered indicative of substantial agreement [Reference to measures of classification reliability].

The resulting classification data were used to generate cross-tabulations and visualizations exploring relationships between dimensions, enabling identification of common research patterns, emerging trends, and notable gaps in the current literature. These analyses formed the foundation for our synthesis and recommendations.

### 2.4 Data Extraction Process

#### Systematic Data Collection

For each included study, we extracted comprehensive data using a standardized form developed in REDCap (Research Electronic Data Capture) [REDCap reference]. The data extraction form was designed to capture detailed information across six domains: study characteristics, SDOH data elements, AI/ML methodology, outcome measures, implementation considerations, and quality assessment.

For study characteristics, we extracted publication details (authors, journal, year, country), study design and setting, population demographics and inclusion criteria, sample size and timeframe, and funding sources and potential conflicts of interest. Regarding SDOH data elements, we documented specific SDOH variables incorporated, data sources and collection methods, operational definitions of SDOH factors, data completeness and handling of missing data, and temporal aspects of SDOH data (static vs. longitudinal). For AI/ML methodology, we captured model architecture and algorithms, feature engineering approaches, training and validation procedures, hyperparameter optimization methods, and computational requirements.

Outcome measures extraction included primary prediction targets, performance metrics (AUC, sensitivity, specificity, calibration, etc.), comparative benchmarks (against clinical models without SDOH), subgroup analyses by demographic factors, and fairness and equity assessments. Implementation considerations included integration approach (if implemented), user interface and workflow considerations, stakeholder engagement methods, barriers and facilitators to implementation, and sustainability and maintenance plans. Finally, for quality assessment, we evaluated risk of bias based on PROBAST (Prediction model Risk Of Bias ASsessment Tool) [PROBAST reference], reporting completeness using TRIPOD guidelines [TRIPOD reference], external validation procedures, and fairness evaluation methodology.

Data extraction was performed by pairs of reviewers with complementary expertise (e.g., informatics and public health), working independently and then reconciling differences through consensus discussions. A third reviewer was consulted to resolve persistent disagreements. To ensure consistent data extraction, we conducted calibration exercises with all reviewers using a sample of five articles, refining the extraction form based on feedback.

#### Analysis Approach

The extracted data were compiled into structured databases to facilitate both quantitative synthesis and qualitative thematic analysis. For quantitative performance metrics, we calculated summary statistics (ranges, means, medians) where appropriate, with careful attention to the limitations of direct comparisons across heterogeneous study designs and populations. Meta-analysis of performance metrics was conducted for subsets of studies with sufficiently homogeneous designs and outcome measures [Reference to meta-analytic methods for prediction model performance].

For methodological approaches and implementation considerations, we employed thematic content analysis to identify common patterns, innovative approaches, and emerging trends [Reference to qualitative synthesis methods]. This involved iterative coding of extracted data, identification of recurring themes, and synthesis across studies to derive higher-level insights. Two analysts conducted this process independently and then reconciled their findings through discussion.

To assess potential publication bias, we examined the relationship between reported performance metrics and study characteristics such as sample size, funding source, and journal impact factor [Reference to methods for assessing publication bias in prediction modeling studies]. We also compared characteristics of studies at different implementation stages to identify factors associated with successful translation to clinical practice.

The combined quantitative and qualitative analyses enabled comprehensive assessment of the current state of SDOH integration with AI/ML in healthcare prediction, addressing our core research questions regarding methodological approaches, data integration strategies, predictive performance, and implementation considerations.

### 2.5 Collection Results Overview

- **PRISMA Flow Diagram**

  - Visual representation of article selection process
  - Numbers at each stage of filtering
- **Article Distribution Summary**

  - Distribution by year (showing trends)
  - Distribution by journal/source
  - Distribution by geography/population
  - Distribution by AI/ML method
  - Distribution by SDOH domain
