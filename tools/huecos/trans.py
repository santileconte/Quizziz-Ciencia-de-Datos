# Transcripción literal del texto de cada figura (leído de la imagen). Clave: índice de región (o "a+b" para unir).
# Prefijo "~": hueco de nivel 'extra'. Regiones no listadas: no se tapan.
T = {}
T['f15-01'] = {'0': '~Data engineering lifecycle', '1': 'Analytics', '2': 'Ingestion', '3': 'Transformation', '4': 'Serving',
  '5': 'Machine learning', '6': 'Generation', '7': 'Storage', '8': 'Reverse ETL', '9': '~Undercurrents:', '10': 'Security',
  '11': 'Data management', '12': 'DataOps', '13': 'Data architecture', '14': 'Orchestration', '15+16': 'Software engineering'}
T['f02-01'] = {'0': 'Source 1', '3': 'Source 2', '8': 'Source n', '5': 'Raw Data', '6': 'Features', '4.0': 'Modeling', '7': 'Insights',
  '10+12': 'Select and merge', '11': 'Clean and transform'}
T['f04-01'] = {'0': '~Step 1', '1': '~Step 2', '2': '~Step 3', '3': '~Step 4', '4': '~Step 5', '8+13': 'Define the problem domain',
  '5': 'Obtain data', '14': 'Exploratory analysis', '10+15': 'Feature engineering', '6+11': 'Model selection', '17': 'Training',
  '7+12.0': 'Model deployment', '18': 'Evaluation'}
T['f04-02'] = {'1': 'Model-centric', '18': 'Data-centric', '8': 'A potentially very complex problem', '3': 'Poorly extracted data',
  '4': 'A complex, slow ML model', '12+13': 'Data that has been properly engineered',
  '11': 'A simpler ML model that will likely perform faster and provide better metrics'}
T['f04-03'] = {'0': '~Feature engineering pipeline', '1': '2. Feature structuring', '3+6': 'Unstructured data (e.g., images and text)',
  '2+5+7': 'Feature extraction and learning', '4+8': 'Newly structured data', '9': 'Data union', '10+12': 'Final dataset', '11': 'Modeling',
  '14+17+18': 'Structured data (tabular)', '13+16': 'Feature improvement, construction, extraction, and selection',
  '15+19': 'Optimally structured data', '20+21': 'Data sources', '22+25+26': '1. Feature understanding', '23': '3. Feature optimization',
  '24': '4. Feature evaluation'}
T['f04-04'] = {'0+1': 'Use feature improvement/construction to enhance signals.', '2': 'Yes', '9': 'No', '3+6': 'Are our data structured?',
  '4+7': 'Structured data', '5+8': 'Evaluate ML model', '11+13': 'Structure them with feature construction, extraction, or learning',
  '10+14': 'Use feature extraction/learning to map features to a new feature space.',
  '12': 'If performance is not where we want it to be, continue to engineer features.',
  '15': 'Assign levels to features to know which feature engineering technique to use.'}
T['f04-05'] = {'20': 'Feature 1', '21': 'Feature 2', '22': 'Feature n', '23': '(e.g., has crown)',
  '24': '(e.g., is laying down)'}
T['f06-01'] = {'0': '~Types of data', '4': 'Nominal scale', '5': 'Ordinal scale',
  '6': 'Used to categorize data with no inherent order or quantitative value', '7': 'Used to impose a sense of order with no quantitative value',
  '8': 'Blood type', '9': 'Letter grades', '25': 'Interval scale', '26': 'Ratio scale',
  '27': 'These are quantitative values for which the difference between values has meaning.',
  '28': 'These are quantitative values with interpretable differences and for which a true zero exists, enabling complex mathematics.',
  '30': 'Temperature', '29': 'Height'}
T['f06-02'] = {'0': 'Neighborhood', '8': 'Financial district', '13': 'Outer Sunset', '18': 'Inner Richmond', '24': 'Financial district',
  '29': 'Soma', '1+5': 'Financial district', '2+6': 'Outer Sunset', '3+7': 'Inner Richmond', '4': 'Soma',
  '19': 'Create n features, where n is the number of distinct categories. This way the machine learning pipeline has a numerical value to learn from.'}
T['f06-03'] = {'0': 'Arithmetic mean', '1': 'Geometric mean', '2': 'Harmonic mean'}
T['f08-01'] = {'0': '~Raw Text', '1+2+3+4': '~Bag-of-words vector', '14+15+16+17+18+21+22': 'it is a puppy and it is extremely cute',
  '5': 'it', '7@0,0,60,20': 'they', '10': 'puppy', '12+13': 'and', '19': 'cat', '24@0,0,60,0': 'aardvark', '26': 'cute', '27+28': 'extremely'}
T['f09-01'] = {'0': 'Easy', '6': 'Medium', '12': 'Hard', '1': 'Spell Checking', '2': 'Keyword-Based Information Retrieval', '3': 'Topic Modeling',
  '4': 'Text Classification', '5': 'Information Extraction', '7': 'Closed Domain Conversational Agent', '8': 'Text Summarization',
  '9': 'Question Answering', '10': 'Machine Translation', '11': 'Open Domain Conversational Agent'}
T['f09-02'] = {'0': 'Context', '3': 'meaning', '4': 'Syntax', '7': 'phrases & sentences', '8': 'Morphemes & Lexemes', '12': 'words',
  '13': 'Phonemes', '16': 'speech & sounds', '17': '~Blocks of Language', '18': '~Applications', '1.0': 'Summarization',
  '1.1': 'Topic Modeling', '1.2': 'Sentiment Analysis', '5.0': 'Parsing', '5.1': 'Entity Extraction', '5.2': 'Relation Extraction',
  '9.0': 'Tokenization', '10+9.1': 'Word Embeddings', '9.2': 'POS Tagging', '14.0': 'Speech to Text', '14.1': 'Speaker Identification',
  '14.2': 'Text to Speech'}
T['f09-03'] = {'0': 'AI', '1': 'ML', '3': 'NLP', '4': 'DL', '2.0': 'Artificial intelligence', '2.1': 'Machine learning',
  '2.2': 'Natural Language Processing', '2.3': 'Deep learning'}
# f09-04 (SVM), f09-05 (RNN) y f09-06 (LSTM): sin palabras, solo símbolos y puntos. No se tapan.
T['f09-07'] = {'6': 'Core Tasks Covered in Chapters 3–7', '21': 'General Applications Covered in Chapters 4–7',
  '35+43': 'Industry Specific Covered in Chapters 8–10', '0.1+0.2': 'Text Classification', '1.3+1.4@25,0,0,0': 'Information Extraction',
  '12.1+12.2': 'Conversational Agent', '15@25,0,0,0': 'Information Retrieval', '16': 'Question Answering Systems',
  'R:365,428,553,508': 'Spam Classification', '27': 'Calendar Event Extraction', '28': 'Personal Assistants', '29': 'Search Engines',
  '30': 'Jeopardy!', '44': 'Social Media Analysis', '45': 'Retail Catalog Extraction', '46': 'Health Records Analysis',
  '47': 'Financial Analysis', '48@25,0,0,0': 'Legal Entity Extraction'}
T['f10-01'] = {'1': 'Data Acquisition', '2': 'Text Cleaning', '3': 'Pre-Processing', '0': 'Feature Engineering', '8': 'Modeling',
  '7': 'Evaluation', '6': 'Deployment', '5': 'Monitoring and Model Updating', '4': 'Improving the model'}
T['f10-02'] = {'R:185,58,585,140': 'Stemming', 'R:895,58,1480,135': 'Lemmatization', 'R:500,160,712,245': 'adjust',
  'R:445,262,735,340': 'formaliti', 'R:470,365,692,450': 'formal', 'R:455,470,630,550': 'airlin', 'R:1185,150,1420,240': '(to) be',
  'R:1250,262,1430,352': 'good', 'R:1235,370,1525,460': 'meeting'}
T['f10-03'] = {'1': 'Text', '0+3': 'Sentence Tokenization', '2': 'Sentences', '7': 'Sentence', '4': 'Lowercasing',
  '5+6': 'Removal of Punctuation', '8': 'Stemming', '9': 'Lemmatization', '10': 'Basic'}
T['f11-01'] = {'0': 'Training data (texts and their categories)', '2': 'Pre-processing, feature extraction from texts',
  '5+6+8': 'Train and evaluate classifiers to learn the features-category mapping', '10+13': 'Use the classifier to predict on new tasks',
  '9+11+14': 'New texts with unknown categories', '3': 'Training process'}
T['f13-01'] = {'0': '~Data viewpoint', '32': '~Technology viewpoint', '1': 'Data product', '2': 'Data product',
  **{str(i): 'Data element' for i in range(3, 10)}, **{str(i): 'Data attribute' for i in range(19, 29)},
  '29': 'Physical dataset 01', '30': 'Physical dataset 02', '31': 'Physical dataset 03'}
T['f13-02'] = {'R:570,35,1035,90': '~Application architecture', '1@20,0,0,0': 'Interface', '2': 'Commands', '3': 'Queries',
  'R:62,598,470,700': 'Command store (writes, updates, and deletes)', '8': 'Change feed', '10': 'Data', '13': 'Query model (reads)'}
T['f13-03'] = {'4': 'Source-oriented domains', '3': 'Consumer-oriented domains', '0': 'Data providers', '6': 'Data providers',
  '10': 'Data providers', '1': 'Data product', '7': 'Data product', '11': 'Data product', '2': 'Consumer-specific transformations',
  '8': 'Consumer-specific transformations', '12': 'Consumer-specific transformations', '5': 'Data consumers', '9': 'Data consumers',
  '13': 'Data consumers', '14': 'Supporting governance and domain-agnostic platform infrastructure'}
T['f13-04'] = {'2': 'Metadata layer: discover, observe, approve, secure, deploy', '10': 'Data product architecture',
  'R:520,335,735,385': 'Data pipeline', 'R:745,335,955,385': 'Enrichments', 'R:520,425,735,470': 'Observability', '17': 'Security',
  '21': 'Operational systems', '26': 'Input ports', '27': 'Output ports', '32': 'Layer 1', '29': 'Layer 2', '33': 'Layer 3',
  '24': 'Enforcement', '37': 'Infrastructure', '43': 'Data domain boundary'}
T['f14-01'] = {'R:0,22,888,155': '~THE DATA SCIENCE HIERARCHY OF NEEDS', '6': 'AI, DEEP LEARNING',
  '7': 'A/B TESTING, EXPERIMENTATION, SIMPLE ML ALGORITHMS', '10': 'ANALYTICS, METRICS, SEGMENTS, AGGREGATES, FEATURES, TRAINING DATA',
  'R:700,625,1380,668': 'CLEANING, ANOMALY DETECTION, PREP',
  '14': 'RELIABLE DATA FLOW, INFRASTRUCTURE, PIPELINES, ETL, STRUCTURED AND UNSTRUCTURED DATA STORAGE',
  '16': 'INSTRUMENTATION, LOGGING, SENSORS, EXTERNAL DATA, USER GENERATED CONTENT', '8': 'LEARN/OPTIMIZE', '11': 'AGGREGATE/LABEL',
  '12': 'EXPLORE/TRANSFORM', '15': 'MOVE/STORE', '17': 'COLLECT'}
T['f14-02'] = {'R:65,255,272,360': '1. Starting with data', '3': '2. Scaling with data', 'R:1325,20,1535,125': '3. Leading with data'}
T['f14-03'] = {'2+4': 'Software engineers', '5': 'Data architects', '9': 'DevOps and SREs', '11': 'Upstream data producers',
  '6+8': 'Data engineers', '3': 'Data analysts', '7': 'Data scientists', '10': 'Machine learning engineers', '12+13': 'Downstream data consumers'}
T['f15-02'] = {'R:470,400,1135,520': 'Data lifecycle', 'R:635,700,1485,960': 'Data engineering lifecycle'}
T['f15-03'] = {'0': 'Types of analytics', '2': 'Operational', '1@0,0,15,0': 'Business intelligence, ad hoc', '3': 'Embedded'}
T['f15-04'] = {'0': 'Data source', '1': 'Data source', '2': 'Data source', '6': 'Data source', '8': 'SaaS platform', '3': 'Ingestion',
  '4': 'Transformation', '5': 'Serving', '7': 'Storage'}
T['f15-05'] = {'4': 'Automation', '1': 'Observability and monitoring', '2+5': 'Incident response'}
T['f16-01'] = {'1': 'Enterprise architecture', '3': 'Business architecture', '4': 'Technical architecture', '5': 'Application architecture',
  '6': 'Data architecture'}
T['f16-02'] = {'2': 'Data architecture', '3': 'Operational', '4': 'Technical', '5': 'What', '6': 'How'}
T['f17-01'] = {'0+1': 'Data source', '6+7': 'Data source', '3': 'ETL system', '4': 'Data warehouse', '2': 'Data mart', '5': 'Data mart'}
T['f17-02'] = {'1+3': 'Data source', '10': 'Data source', '0': 'ELT', '6': 'Staging', '5': 'Data warehouse',
  '2': 'Analysis, data science', '9': 'Reports'}
T['f17-03'] = {'2+3': 'Data source', '13': 'Data source', '1': 'ETL or ELT', '9': 'Staging', '8': 'Data warehouse', '5': 'Data marts',
  '11': 'Data marts', '6': 'Analysis, data science', '12': 'Reports'}
T['f17-04'] = {'0': 'Serving', '1+4': 'Stream processing', '9+11': 'Batch processing', '6+8': 'Source systems', '5': 'Stream query',
  '10': 'Batch query', '7': 'Queries'}
T['f17-05'] = {'0+4': 'Stream source', '1': 'Stream processing', '2': 'Serving layer', '3': 'Queries'}
T['f17-06'] = {'0': 'Typically implemented in the same database (RDBMS)', '1+3': 'Staging area', '7': 'File store', '8': 'Data warehouse',
  '10@15,0,0,0': 'Integration layer', '2': 'Data mart', '11.0': 'Data mart', '24': 'Data mart', '13': 'Reporting tools'}
T['f17-07'] = {'0+3': 'Staging area', '4': 'File store', '2': 'Typically implemented in the same database (RDBMS)', '5': 'Data warehouse',
  '7': 'Views', '10.0': 'Data mart', '11': 'Reporting tools'}
T['f17-08'] = {'0': 'Lakehouse architecture', '1': 'Compute', '2': 'Spark', '3': 'Cloud object storage', '5': 'Bronze', '6': 'Silver',
  '7': 'Gold', '4': 'Sources', '9': 'OLTP systems', '15': 'OLTP systems', '19': 'OLTP systems', '10': 'Operational data store',
  '8': 'Data science workloads', '14': 'Reporting workloads', '20': 'Sharing with others'}
T['f17-09'] = {'4': 'Data sources', '2': 'Cloud-based data connector and integration', '5': 'Cloud data warehouse', '3': 'BI and visualization'}
T['f17-10'] = {'0': 'Hadoop cluster', '1': 'HDFS/HIVE tables', '2': 'MapReduce/Spark', '3': 'Sources', '4': 'OLTP systems', '9': 'OLTP systems',
  '11': 'OLTP systems', '5': 'Operational data store', '8': 'Data science workloads', '12': 'Data warehouse'}
T['f18-01'] = {'R:652,219,962,269': 'Organizationally', 'R:666,638,947,688': 'Architecturally', '44': 'Technically', 'R:678,1484,936,1535': 'Operationally', '72': 'Principally',
  'R:655,2248,960,2299': 'Infrastructurally', '17': 'Centralized ownership', '18': 'Decentralized domain ownership', '37': 'Monolithic', '38': 'Distributed',
  '46': 'Data byproduct of code', 'R:1113,1165,1540,1208': 'Data and code as one unit', '64': 'Top-down governance',
  '65': 'Federated computational governance', '83': 'Data as an asset to collect', '81': 'Data as a product to share and connect',
  'R:76,2349,490,2434': 'Fragmented platform (analytical & operational)', 'R:1196,2349,1525,2394': 'Integrated platform'}
T['f18-02'] = {'13': 'Domain-oriented ownership', '14': 'Data as a product', '36': 'Federated computational governance',
  'R:1172,1779,1583,1845': 'Self-serve data platform', '11': '1) Prevent data siloing', '23': '(2) Empower domain teams',
  '21': '(3) Reduce the cost of ownership', '20': '(4) Increase engagement, reduce domain isolation',
  '22': '(5) Get higher-order value by interconnecting data products',
  'R:490,1833,1136,1958': '(6) Mesh-level consistent and reliable policy enforcement'}
T['f18-03'] = {'0': 'Federated computational governance', '7': 'Global policies automated by platform',
  '5': 'Federated team of domain representatives', '10': 'Policies applied to data products', '16': 'Data product',
  'R:393,1095,497,1172': 'Apps', '25': 'Business domain', '30': 'Data sharing APIs', '36': 'Platform services used by data products',
  '38': 'Cross-functional domain team: business, technology, and data', '39': 'Data platform service interfaces',
  '43': 'Self-serve data platform', '48': 'Platform team'}
T['f18-04'] = {'0': 'Federated computational governance', '5': 'Global policies automated by platform',
  '4': 'Federated team of domain representatives', '8': 'Policies applied to data products', 'R:183,480,340,595': 'Data product',
  'R:390,605,500,665': 'Apps', '30': 'Business domain', '36': 'Data sharing APIs', '42': 'Platform services used by data products',
  '44': 'Cross-functional domain team: business, technology, and data', '45': 'Data platform service interfaces',
  '49': 'Self-serve data platform', 'R:48,1295,256,1332': 'Platform team'}
T['f19-01'] = {'0.0': 'Bronze layer', '0.1': '(raw copies)', '1.0': 'Silver layer', '1.1+1.2': '(filtered, clean, augmented)',
  '2.0': 'Gold layer', '2.1+2.2': '(modeled for consumption)', '5': 'Sources', '4': 'Landing zone', '7': 'OLTP systems',
  '11': 'ERP system', '13': 'CRM system', '8': 'Blob file store', '14': 'Kafka',
  '10+12': 'Initial landing zone for raw data collected from various sources',
  '6': 'Transitional stage where data is still source system-aligned and granular but has been processed to ensure quality and consistency',
  '9': 'Focus on performance and scalability, providing fast access to business insights'}
T['f19-02'] = {'0': 'Metadata and governance layer', '1': 'Medallion architecture', '4': 'Bronze', '5': 'Silver', '6': 'Gold',
  '3': 'Data sources', '2': 'Intelligent and consuming data services'}
T['f19-03'] = {'2': 'Metadata and governance layer', '3': '1. Data providers', '7+8': '2. Distribution layer', '5+6+9': '3. Data consumers'}
T['f22-01'] = {'6': 'User', '4': 'Orchestration', '1': 'Model', '2': 'Tools', '5': 'Memory', '7': 'Knowledge base'}
T['f23-01'] = {'0': 'The prompt with the user question is augmented with the retrieved information.',
  '1': 'The LLM responds with a contextual answer.', '2+3@0,0,15,0': 'User asks a question.', '12': 'User', '10': 'Question',
  '13': 'Retriever', '11': '{Question + Information}', '14': 'LLM', '9.1': 'Response', '16': 'Parametric memory',
  '20+22@0,0,15,0': 'The system searches for relevant information.', '18': 'Search', 'R:580,330,640,478': 'Fetch information',
  '21': 'The information relevant to the input question is fetched, or retrieved.',
  'R:1120,376,1428,406': 'Generation pipeline:', 'R:1118,408,1487,520': 'Uses the knowledge base to generate context-aware responses',
  'R:24,590,292,620': 'Indexing pipeline:', 'R:22,622,340,698': 'Facilitates the creation of the knowledge base',
  'R:430,632,676,668': 'Knowledge base', 'R:495,676,595,705': 'Storage', 'R:445,706,640,770': 'Non-parametric memory',
  '30': 'Converter', '31@0,0,15,0': 'Converts these small pieces into a suitable format.',
  '32': 'Extract documents and parse text from documents.', '33@0,0,15,0': 'Breaks down long pieces of text into smaller manageable pieces.',
  '34@0,0,15,0': 'Connects to external sources.', '39': 'Source', '40': 'Connector', '41+43': 'Extracter and parser', '42': 'Splitter'}
T['f23-02'] = {'1': 'User query or prompt', '2': 'Answer relevance', '5+6': 'Is the answer relevant to the user query?',
  '3': 'Context relevance', '4+7': 'Is the retrieved information or context relevant to the user query or prompt?',
  '10': 'Groundedness', '11+16': 'Is the response or answer faithful to the retrieved context?', '12+14': 'Response or answer',
  '13+15': 'Retrieved information or context'}
T['f23-03'] = {'1': 'Data-splitting component: Chunking', '2': 'Storage component: Vector DBs', '5': 'Data-loading component',
  '3+6': 'Conversion component: Embeddings', '0+4+7': '“Offline” data indexing components for knowledge base creation',
  '10': 'Prompt management', '18': 'Retrievers', '21': 'LLMs setup',
  '11+16+19': '“Real-time” interaction components for contextual responses', '13@10,0,0,0': 'Input/Output', '15': 'Orchestrator',
  '22': 'Application component', '24': 'Caching', '25': 'Evaluation', '28': 'Guardrails', '29': 'Monitoring', '31': 'LLM security',
  '32': 'Privacy', '26': '“Supporting” components for usability, efficiency, experience, etc.', '34': 'Service Infrastructure'}
T['f24-01'] = {'0.0': 'External memory', '0.1+0.2': 'Documents, tables, chat history, etc.', '1': 'Prompt', '4': 'Retriever',
  '6': 'Context relevant to query', '7': 'Generative model', '8': 'Response'}
T['f24-02'] = {'2': 'Index', '4.0': 'External memory', '4.1+4.2': 'Documents, tables, chat history, etc.', '6': 'Splitter',
  '9': 'Embedding model', '10': 'VectorDB', '13': 'External data embeddings', '20': 'Query', '22': 'Query embedding',
  'R:1320,775,1497,820': 'Retriever', '24': 'Generative model', '26': 'Context relevant to query', '27': 'Response'}
T['f25-01'] = {'R:598,26,920,64': '(1) Hotspot QA', '4': 'Question', 'R:506,338,1122,380': '(1d) ReAct (Reason + Act)',
  'R:36,424,264,464': 'Thought 1', 'R:36,524,162,562': 'Act 1', 'R:36,574,166,612': 'Obs 1',
  'R:36,774,264,814': 'Thought 2', 'R:36,924,162,962': 'Act 2', 'R:36,974,166,1012': 'Obs 2',
  'R:36,1174,264,1214': 'Thought 3', 'R:36,1274,162,1312': 'Act 3', 'R:36,1324,166,1362': 'Obs 3',
  'R:36,1424,264,1464': 'Thought 4', 'R:36,1574,162,1612': 'Act 4',
  'R:214,526,364,564': '~Search', 'R:214,926,364,964': '~Search', 'R:214,1276,364,1314': '~Search', 'R:214,1574,366,1614': '~Finish'}
T['f25-02'] = {'0': 'Info less frequently used', '1+4': 'External memory', '2': 'Long-term memory', '8': 'Retriever', '10+13': 'Short-term memory',
  '11': 'Context', '12': 'Model', '16': 'Training data', '18@8,0,0,0': 'Internal knowledge', '19': 'Info essential for multiple tasks'}
T['f25-03'] = {'0': 'Tools', '1': 'Tool outputs', '2': 'Executor', '3': 'Query', '4': 'Planner', '5': 'Generated plan', '6': 'Evaluator',
  'R:1418,476,1540,522': 'Finish'}
T['f26-01'] = {'R:14,22,768,288': '~THE LANDSCAPE OF AI AND ITS USE CASES', '4': 'ASI Artificial Superintelligence',
  '10': 'AGI Artificial General Intelligence', '15': 'Traditional AI', 'R:468,545,682,638': '(Multimodal) GenAI',
  '5': 'Art/Books that understand human emotion', '12': 'Solving Global Challenges', '13': 'Agentic AI',
  '14': 'Perform Specific Tasks', '16': 'Medical Diagnosis/ Treatment', '17': 'Healthcare Revolution', '18': 'NLP',
  '20+22': 'Addressing Climate Change', '21': 'Environment Management', '24': 'Face Detection', '25': 'Image Recognition',
  '26': 'Space Exploration', '27@0,0,10,0': 'Content Generation: (Image, video, text, audio)', '28': 'Accelerate Scientific Research',
  '29+30': 'Speech Recognition, TTS', '31': 'Personalized Education', '32': 'Data Mining', '33+34': 'Pattern Recognition',
  '35': 'Autonomous Systems', '37': 'Physical AI / Robotics', '38+39+41': 'Can behave in a humanlike way',
  '40': 'Smarter than Humans (hypothetical)'}
T['f26-02'] = {'2': 'Core product management craft and practices', '3': 'Engineering foundations for PMs',
  '4': 'Essential leadership and collaboration skills', '5': 'AI lifecycle and operational awareness'}
