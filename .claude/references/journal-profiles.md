# Journal Profiles

<!--
These profiles calibrate the domain-referee and methods-referee when reviewing
for a specific journal. Each profile describes the journal's review culture
in plain language — the LLM adapts its priorities accordingly.

Used by: domain-referee.md, methods-referee.md (via /review --peer [journal])
-->

## How This Works

When `/review --peer [journal]` is invoked:

1. **Editor reads the paper** → desk review (reject or send to referees)
2. **Editor selects referees** → draws dispositions and pet peeves from the journal's **Referee pool**
3. **Profile found below** → referees calibrate using the full profile
4. **Profile NOT found** → referees use the journal name + .claude/references/domain-profile.md to adapt (still better than generic)
5. **No journal specified** → generic top-field referee behavior

### Referee Pool Field

Each journal profile includes a **Referee pool** that weights which dispositions the editor draws from. The two referees always get DIFFERENT dispositions. Dispositions: STRUCTURAL, CREDIBILITY, MEASUREMENT, POLICY, THEORY, SKEPTIC (see editor.md for definitions).

### Table Format Convention

**Default:** All journals use standard economics table conventions — significance stars (`*` p<0.10, `**` p<0.05, `***` p<0.01), standard errors in parentheses, booktabs formatting. This default applies unless a journal profile below includes a **Table format** override.

**Exception — AEA journals** (AER, AEJ:Applied, AEJ:Policy, AER:Insights): No significance stars. Report standard errors in parentheses; use exact p-values or confidence intervals for key results. See the [AEA Style Guide](https://www.aeaweb.org/journals/aeri/style-guide) and content-standards.md for implementation details.

---

## Economics

**Top-5 General Interest**

### American Economic Review (AER)
**Focus:** All fields of economics — the broadest audience
**Bar:** Must interest economists outside your subfield. Big question, clean execution, clear contribution.
**Domain referee adjusts:** "Would a labor economist care about this health paper?" Contribution must be broad. Literature positioning against the *general* frontier, not just subfield. Policy implications welcome but not required — insight is enough.
**Methods referee adjusts:** Identification must be convincing to non-specialists. Clean, transparent design preferred over technically complex one. Standard errors and robustness should be thorough but not excessive.
**Typical concerns:** "Why should economists outside this field care?" "Is the contribution big enough for AER?" "Is this too narrow/specialized?"
**Referee pool:** CREDIBILITY (high), POLICY (medium), STRUCTURAL (medium), MEASUREMENT (low), THEORY (low), SKEPTIC (low)
**Table format:** No significance stars. Standard errors in parentheses. Exact p-values or confidence intervals for key results (AEA style).

### Econometrica (ECMA)
**Focus:** Theoretical and empirical economics with formal rigor
**Bar:** Methodological innovation or empirical work with exceptional identification and formal results.
**Domain referee adjusts:** Theoretical contribution valued highly. If empirical, the design must be near-airtight. Formal welfare analysis expected. Less emphasis on policy narrative, more on economic theory and mechanisms.
**Methods referee adjusts:** Formal proofs or near-formal arguments expected for key results. Asymptotic properties discussed. Novel estimators should have theoretical justification. Simulation evidence for finite-sample properties.
**Typical concerns:** "Where's the formal result?" "What are the asymptotic properties?" "Is this a methods contribution or an applied contribution?"
**Referee pool:** THEORY (high), STRUCTURAL (high), SKEPTIC (medium), CREDIBILITY (low), MEASUREMENT (low), POLICY (low)

### Journal of Political Economy (JPE)
**Focus:** All fields — strong emphasis on economic mechanisms and structural thinking
**Bar:** Deep economic insight. JPE values understanding *why* something happens, not just *that* it happens.
**Domain referee adjusts:** Mechanism is king. Reduced-form results alone insufficient — need to explain the economics. Structural models or mechanism tests expected. Theoretical framework (even informal) valued.
**Methods referee adjusts:** Identification strong, but mechanism evidence equally important. Heterogeneity that illuminates the mechanism. Willing to accept some identification imperfection if the economic insight is deep enough.
**Typical concerns:** "What's the mechanism?" "Can you decompose the effect?" "What does this tell us about economic behavior?"
**Referee pool:** STRUCTURAL (high), THEORY (high), CREDIBILITY (medium), SKEPTIC (medium), POLICY (low), MEASUREMENT (low)

### Quarterly Journal of Economics (QJE)
**Focus:** All fields — prizes compelling narrative and important questions
**Bar:** The question must be important and the answer must surprise. QJE loves papers that change how you think about something.
**Domain referee adjusts:** Narrative matters enormously. The paper should read like a story with a punchline. Broad implications. Creative use of data or setting. "Clever" identification valued.
**Methods referee adjusts:** Identification must be clean and intuitive — not just technically correct, but easy to explain. Transparency and simplicity over complexity. Visual evidence (event studies, RD plots) highly valued.
**Typical concerns:** "Is this surprising?" "Does this change how we think about X?" "Can you explain the identification in one sentence?"
**Referee pool:** CREDIBILITY (high), POLICY (high), SKEPTIC (medium), STRUCTURAL (low), THEORY (low), MEASUREMENT (low)

### Review of Economic Studies (REStud)
**Focus:** All fields — technically excellent empirical and theoretical work
**Bar:** Technical quality must be top-tier. Values precision and completeness over narrative.
**Domain referee adjusts:** Thoroughness expected — address every possible objection. Complete set of robustness checks. Careful literature review. Less emphasis on storytelling than QJE, more on completeness.
**Methods referee adjusts:** Every specification must be justified. Full battery of robustness checks expected. Sensitivity analysis (Oster bounds, etc.). Careful treatment of inference. Multiple testing corrections if applicable.
**Typical concerns:** "Have you checked robustness to X?" "What about specification Y?" "The inference needs more care."
**Referee pool:** SKEPTIC (high), MEASUREMENT (high), CREDIBILITY (medium), THEORY (medium), STRUCTURAL (low), POLICY (low)

---

**Top Field Journals**

### American Economic Journal: Applied Economics (AEJ:Applied)
**Focus:** Empirical microeconomics — labor, health, education, development, public
**Bar:** Clean applied micro paper with credible identification and clear results. Slightly below top-5 bar but same rigor expectations.
**Domain referee adjusts:** Contribution should be meaningful to the subfield. Practical policy relevance appreciated. Literature positioning within the subfield, not the general field.
**Methods referee adjusts:** Same identification standards as top-5. Modern estimators expected (no naive TWFE for staggered). Replication package expected.
**Typical concerns:** "Is this incremental relative to [closely related paper]?" "Would this be better in a field journal?"
**Referee pool:** CREDIBILITY (high), POLICY (medium), MEASUREMENT (medium), SKEPTIC (low), STRUCTURAL (low), THEORY (low)
**Table format:** No significance stars. Standard errors in parentheses. Exact p-values or confidence intervals for key results (AEA style).

### American Economic Journal: Economic Policy (AEJ:Policy)
**Focus:** Policy evaluation and design — how policies affect outcomes
**Bar:** Must have direct policy relevance. Natural experiments from actual policy changes preferred.
**Domain referee adjusts:** Policy implications front and center — not an afterthought. Cost-benefit or welfare discussion expected. Institutional details of the policy must be well-documented. Generalizability to other policy contexts.
**Methods referee adjusts:** Identification from actual policy variation (not cross-sectional). Pre-trends must be clean. Heterogeneity by policy-relevant subgroups expected. Back-of-envelope welfare calculations.
**Typical concerns:** "What should policymakers do with this?" "Does this generalize to other states/countries?" "What's the cost-benefit?"
**Referee pool:** POLICY (high), CREDIBILITY (high), MEASUREMENT (medium), STRUCTURAL (low), THEORY (low), SKEPTIC (low)
**Table format:** No significance stars. Standard errors in parentheses. Exact p-values or confidence intervals for key results (AEA style).

### Journal of Human Resources (JHR)
**Focus:** Labor economics, education, health, demography
**Bar:** Strong empirical contribution with clear policy relevance and careful identification.
**Domain referee adjusts:** Policy relevance matters more than theoretical novelty. External validity — can results inform actual policy? Sample representativeness. Heterogeneity analysis by policy-relevant subgroups expected. Institutional knowledge of labor markets/education systems/health care valued.
**Methods referee adjusts:** Clean identification is non-negotiable. Modern staggered DiD estimators required if applicable. Robustness to functional form. Pre-trends must be clean and shown. Replication package expected at acceptance.
**Typical concerns:** "What's the policy implication?" "Does this generalize beyond your sample?" "Have you considered heterogeneity by [race/gender/income]?"
**Referee pool:** CREDIBILITY (high), POLICY (high), MEASUREMENT (medium), SKEPTIC (low), STRUCTURAL (low), THEORY (low)

### Journal of Health Economics (JHE)
**Focus:** Health economics — insurance, utilization, provider behavior, public health
**Bar:** Sound health economics with credible identification. Institutional knowledge of health care systems expected.
**Domain referee adjusts:** Must demonstrate deep understanding of health care institutions. Moral hazard vs. adverse selection distinction matters. Welfare implications expected. Connection to health policy debates. Knowledge of CMS data, insurance markets, provider incentives.
**Methods referee adjusts:** Health-specific threats: selection into insurance, Ashenfelter dip in health utilization, moral hazard confounding. IV exclusion restrictions scrutinized heavily in health contexts. GLM for cost outcomes expected alongside OLS.
**Typical concerns:** "Is this moral hazard or adverse selection?" "Have you addressed selection into treatment?" "What about the Medicaid population specifically?"
**Referee pool:** STRUCTURAL (high), MEASUREMENT (high), POLICY (medium), CREDIBILITY (medium), THEORY (low), SKEPTIC (low)

### RAND Journal of Economics (RAND)
**Focus:** Industrial organization, regulation, antitrust, health care markets
**Bar:** IO-flavored analysis with market structure or firm behavior component. Structural or quasi-experimental.
**Domain referee adjusts:** Market structure and competition implications. Firm behavior and strategic incentives. Regulatory implications. Welfare analysis (consumer surplus, total surplus) expected.
**Methods referee adjusts:** Structural models valued alongside reduced-form. Demand estimation methods (BLP, discrete choice). Entry/exit models. Merger simulation if relevant. Reduced-form papers need very clean identification.
**Typical concerns:** "What does this imply for market structure?" "Consumer welfare impact?" "Can you do a structural analysis?"
**Referee pool:** STRUCTURAL (high), THEORY (high), SKEPTIC (medium), POLICY (medium), CREDIBILITY (low), MEASUREMENT (low)

### Journal of Public Economics (JPubE)
**Focus:** Tax policy, public goods, redistribution, government programs
**Bar:** Public finance question with clean identification. Understanding of tax/transfer system mechanics.
**Domain referee adjusts:** Tax incidence, deadweight loss, behavioral responses to taxation. Program evaluation of government interventions. Fiscal federalism. Redistribution and inequality. Knowledge of tax code and transfer programs.
**Methods referee adjusts:** Bunching estimators for tax kinks/notches. RDD at eligibility thresholds. DiD around policy changes. Structural models of labor supply response. Extensive vs. intensive margin effects.
**Typical concerns:** "What's the elasticity?" "Extensive or intensive margin?" "Welfare implications of the tax/transfer change?"
**Referee pool:** STRUCTURAL (high), POLICY (high), CREDIBILITY (medium), THEORY (medium), MEASUREMENT (low), SKEPTIC (low)

### Journal of Labor Economics (JLE)
**Focus:** Labor markets — wages, employment, human capital, discrimination, immigration
**Bar:** Clean labor economics with careful identification. Understanding of labor market institutions.
**Domain referee adjusts:** Wage determination, employment effects, human capital returns, discrimination, unions, immigration. Mincer equations and labor supply models. Firm-worker matched data valued. Monopsony and market power in labor markets.
**Methods referee adjusts:** Selection correction (Heckman, Lee bounds) when relevant. Decomposition methods for wage gaps. Clean identification of causal effects on wages/employment. Event study designs around job transitions or policy changes.
**Typical concerns:** "Is this a supply or demand effect?" "Selection into employment?" "What about general equilibrium effects?"
**Referee pool:** CREDIBILITY (high), STRUCTURAL (medium), MEASUREMENT (medium), THEORY (medium), POLICY (low), SKEPTIC (low)

### Journal of Development Economics (JDE)
**Focus:** Development economics — poverty, institutions, agriculture, trade in developing countries
**Bar:** Credible empirical evidence on development questions. RCTs or strong quasi-experimental designs. Field knowledge.
**Domain referee adjusts:** Context matters enormously — deep knowledge of the country/region expected. External validity to other developing country settings. Implementation details for interventions. Cost-effectiveness. Sustainability of effects. Gender and equity dimensions.
**Methods referee adjusts:** RCTs: randomization checks, attrition, compliance, spillovers, pre-analysis plan. Quasi-experimental: strong first stage for IV, clean RD, credible parallel trends. Power calculations. Clustered standard errors at appropriate level.
**Typical concerns:** "Does this generalize beyond this specific context?" "What about attrition?" "Cost-effectiveness?" "Long-run effects?"
**Referee pool:** CREDIBILITY (high), POLICY (high), MEASUREMENT (high), SKEPTIC (medium), STRUCTURAL (low), THEORY (low)

---

**Short Format**

### AER: Insights
**Focus:** Same breadth as AER but shorter format — important results that can be communicated concisely
**Bar:** AER-quality insight in a shorter paper. Must be self-contained and punchy.
**Domain referee adjusts:** Brevity is a feature, not a limitation. One clean result is enough. No need for 15 robustness checks — the core result must be compelling on its own. Well-suited for striking findings or clever identification.
**Methods referee adjusts:** Core identification must be clean. Fewer robustness checks acceptable given format, but the main result must be robust. Transparency and visual evidence valued.
**Typical concerns:** "Can this be communicated in 10 pages?" "Is the single result compelling enough?" "Does this need a longer format to be convincing?"
**Referee pool:** CREDIBILITY (high), POLICY (medium), SKEPTIC (medium), STRUCTURAL (low), THEORY (low), MEASUREMENT (low)
**Table format:** No significance stars. Standard errors in parentheses. Exact p-values or confidence intervals for key results (AEA style).

### Economics Letters
**Focus:** Short papers across all fields of economics — theoretical and empirical
**Bar:** One clear result that can be communicated in 5-8 pages. Speed of publication valued. No room for extensive robustness or literature review — the result must stand on its own.
**Domain referee adjusts:** Contribution must be stated in the first paragraph. No space for extensive institutional background. One key finding, cleanly presented. Incremental extensions of existing work acceptable if the result is sharp.
**Methods referee adjusts:** Identification must be clean but extensive robustness not expected given format. One well-executed specification is enough. Standard errors must be correct. No space for 10-table robustness sections.
**Typical concerns:** "Can this be said in 5 pages?" "Is the single result robust?" "Is this novel enough for a standalone paper?"
**Referee pool:** CREDIBILITY (high), SKEPTIC (medium), THEORY (medium), MEASUREMENT (low), STRUCTURAL (low), POLICY (low)

---

**Econometrics**

### Journal of Econometrics
**Focus:** Econometric theory and methods — estimation, inference, testing, computational methods, machine learning for causal inference
**Bar:** Methodological contribution with formal results. Empirical applications welcome but the method must be the contribution, not the application.
**Domain referee adjusts:** Theoretical novelty is paramount. Must clearly state what existing methods cannot do that yours can. Monte Carlo simulations expected to demonstrate finite-sample properties. Empirical illustration should showcase the method, not the substantive finding.
**Methods referee adjusts:** Formal proofs required for key results (consistency, asymptotic normality, convergence rates). Regularity conditions must be stated and discussed. Comparison with existing estimators — analytically and via simulation. Power analysis. Computational feasibility discussed. Code availability expected.
**Typical concerns:** "What are the asymptotic properties?" "How does this compare to [existing method]?" "What happens in finite samples?" "Are the regularity conditions plausible in practice?"
**Referee pool:** THEORY (high), SKEPTIC (high), MEASUREMENT (high), STRUCTURAL (medium), CREDIBILITY (low), POLICY (low)

### Review of Economics and Statistics (RESTAT)
**Focus:** Empirical economics — all fields, emphasis on careful measurement and methods
**Bar:** Technically excellent empirical work. Values careful econometrics and measurement.
**Domain referee adjusts:** Measurement quality is paramount. Novel data or measurement approaches valued. Less emphasis on big-picture narrative than QJE, more on getting the econometrics exactly right. Replication studies welcome.
**Methods referee adjusts:** Highest econometric standards short of Econometrica. Every assumption must be tested or bounded. Sensitivity analysis expected. Careful treatment of standard errors. Pre-registration or pre-analysis plans viewed favorably.
**Typical concerns:** "Is the measurement precise enough?" "Have you tested every assumption?" "What about measurement error in [variable]?"
**Referee pool:** MEASUREMENT (high), SKEPTIC (high), CREDIBILITY (high), THEORY (medium), STRUCTURAL (low), POLICY (low)

---

**Health Economics**

### Health Economics
**Focus:** Health economics with emphasis on empirical applications — health care demand, insurance, provider behavior, public health interventions, pharmaceutical markets
**Bar:** Sound empirical health economics. Slightly below JHE bar but same methodological expectations. Good outlet for well-executed applied work in health.
**Domain referee adjusts:** Same institutional knowledge as JHE expected — insurance markets, provider incentives, moral hazard, adverse selection. Health policy relevance valued. Understanding of health care data (claims, EHR, surveys). Behavioral health economics increasingly accepted.
**Methods referee adjusts:** Clean identification expected. Health-specific threats addressed (selection into insurance, Ashenfelter dip, moral hazard confounding). Both OLS and GLM for cost outcomes. Subgroup analysis by insurance type, age, income expected.
**Typical concerns:** "Have you addressed selection?" "What about moral hazard?" "Does this replicate across payer types?" "Policy implications?"
**Referee pool:** CREDIBILITY (high), MEASUREMENT (high), POLICY (medium), STRUCTURAL (medium), THEORY (low), SKEPTIC (low)

---

**Urban and Spatial Economics**

### Journal of Urban Economics (JUE)
**Focus:** Urban and regional economics — housing, transportation, local public goods, agglomeration, spatial equilibrium, neighborhood effects
**Bar:** Clean empirical work on urban questions with credible identification. Understanding of spatial economics and local policy variation.
**Domain referee adjusts:** Spatial equilibrium thinking expected — people and firms move, so partial equilibrium results need justification. Housing markets, land use regulation, sorting, commuting. Knowledge of Census/ACS geography, LODES, HMDA. Hedonic models and spatial instruments common. General equilibrium concerns about migration and capitalization.
**Methods referee adjusts:** Spatial identification challenges: selection into neighborhoods, Tiebout sorting, MAUP. Boundary discontinuity designs valued. DiD around local policy changes. IV with Bartik-style shift-share instruments scrutinized. Spatial autocorrelation in standard errors. Conley standard errors when appropriate.
**Typical concerns:** "What about sorting?" "Is this capitalized into housing prices?" "General equilibrium effects?" "Have you addressed spatial autocorrelation?"
**Referee pool:** STRUCTURAL (high), CREDIBILITY (high), MEASUREMENT (medium), POLICY (medium), THEORY (medium), SKEPTIC (low)

### Journal of Economic Geography
**Focus:** Economic geography — agglomeration, trade costs, spatial inequality, regional development, clusters, migration, urban systems
**Bar:** Contribution to understanding the spatial dimension of economic activity. Both theoretical and empirical work accepted. Interdisciplinary with geography and regional science.
**Domain referee adjusts:** Spatial thinking required — distance, borders, market access, gravity models. New Economic Geography tradition (Krugman, Fujita, Venables). Understanding of agglomeration economies, congestion costs, and spatial sorting. European and international evidence valued alongside US.
**Methods referee adjusts:** Spatial econometrics expected when appropriate (spatial lag, spatial error models). Gravity equation estimation (PPML, multilateral resistance). Handling of spatial autocorrelation. Market access instruments. Shift-share designs for local labor market shocks.
**Typical concerns:** "What about spatial sorting?" "Have you accounted for market access?" "Is this agglomeration or selection?" "Spatial autocorrelation in errors?"
**Referee pool:** STRUCTURAL (high), MEASUREMENT (high), THEORY (medium), CREDIBILITY (medium), POLICY (medium), SKEPTIC (low)

---

## Finance

### The Journal of Finance (JF)
**Focus:** All areas of finance — asset pricing, corporate finance, market microstructure, behavioral finance, household finance
**Bar:** Must advance our understanding of financial markets or financial decision-making. Big question, clean execution. The finance equivalent of AER in breadth and ambition.
**Domain referee adjusts:** Contribution must matter to finance broadly, not just one niche. Theoretical motivation expected — even empirical papers need a clear economic framework. Equilibrium implications considered. Risk adjustment must be thorough for asset pricing papers.
**Methods referee adjusts:** For corporate/household finance: clean causal identification expected (DiD, IV, RDD). For asset pricing: factor model tests, Fama-MacBeth, portfolio sorts with proper standard errors. Endogeneity concerns taken very seriously. Instrument validity scrutinized.
**Typical concerns:** "What's the economic mechanism?" "Is this priced risk or mispricing?" "Have you addressed endogeneity?" "Does this survive controlling for known factors?"
**Referee pool:** THEORY (high), STRUCTURAL (high), CREDIBILITY (medium), SKEPTIC (medium), MEASUREMENT (low), POLICY (low)

### Journal of Financial Economics (JFE)
**Focus:** Corporate finance, asset pricing, banking, governance, financial intermediation
**Bar:** Rigorous empirical or theoretical work. Strong emphasis on economic significance, not just statistical significance. Slightly more empirical focus than JF.
**Domain referee adjusts:** Corporate finance and governance papers especially valued. Institutional knowledge of financial markets expected. Firm-level analysis with careful treatment of endogeneity. Understanding of agency problems, contracting, and incentive alignment.
**Methods referee adjusts:** Natural experiments and quasi-experimental designs valued in corporate finance. Event studies must follow modern best practices (short window, proper benchmarking). Diff-in-diff around regulatory changes common. IV exclusion restrictions scrutinized heavily.
**Typical concerns:** "Is this economically significant or just statistically significant?" "What about reverse causality?" "Have you controlled for firm fixed effects?" "Is your instrument truly exogenous?"
**Referee pool:** CREDIBILITY (high), STRUCTURAL (high), THEORY (medium), SKEPTIC (medium), MEASUREMENT (low), POLICY (low)

### The Review of Financial Studies (RFS)
**Focus:** Theoretical and empirical finance — broad coverage, values technical sophistication
**Bar:** Technically excellent finance research. Tolerates longer papers with thorough analysis. Values completeness and rigor over narrative.
**Domain referee adjusts:** Thoroughness valued — complete robustness section expected. Both theoretical and empirical contributions accepted. International finance and emerging markets welcome. Novel datasets or measurement approaches valued.
**Methods referee adjusts:** Full battery of robustness checks expected. Multiple identification strategies appreciated. Structural estimation alongside reduced-form welcome. Careful inference — clustered standard errors, bootstrap, wild cluster bootstrap when appropriate.
**Typical concerns:** "Have you checked robustness to alternative specifications?" "What about clustering at the firm vs. industry level?" "Can you provide a structural interpretation?"
**Referee pool:** SKEPTIC (high), MEASUREMENT (high), STRUCTURAL (medium), THEORY (medium), CREDIBILITY (low), POLICY (low)

### Journal of Financial and Quantitative Analysis (JFQA)
**Focus:** Empirical and theoretical finance with quantitative rigor — corporate finance, investments, banking, capital markets
**Bar:** Sound empirical finance with clear contribution. Below top-3 finance bar but same rigor expectations. Good outlet for careful empirical work.
**Domain referee adjusts:** Solid contribution to the subfield sufficient — doesn't need to reshape the whole field. International and comparative studies welcome. Clear economic intuition expected.
**Methods referee adjusts:** Standard modern finance econometrics expected. Fixed effects, clustering, instrumental variables. Event study methodology must be current. Robustness to alternative specifications.
**Typical concerns:** "Is this incremental relative to existing work?" "Have you considered international evidence?" "Is the sample period long enough?"
**Referee pool:** CREDIBILITY (high), MEASUREMENT (medium), SKEPTIC (medium), THEORY (medium), STRUCTURAL (low), POLICY (low)

---

## Accounting

### Journal of Accounting Research (JAR)
**Focus:** Financial reporting, auditing, disclosure, capital markets — the most empirically rigorous accounting journal
**Bar:** Archival empirical work with strong identification, or analytical models with clear predictions. JAR is the most "economics-adjacent" accounting journal.
**Domain referee adjusts:** Must understand GAAP/IFRS reporting incentives. Earnings management, accruals quality, and disclosure theory. Capital markets consequences of accounting choices. Audit quality and auditor incentives.
**Methods referee adjusts:** Identification strategy must be clean — JAR holds to economics standards. DiD around accounting standard changes common. Selection models for auditor choice. Heckman corrections when appropriate. Pre-trends and parallel trends for policy changes.
**Typical concerns:** "Is this an accounting paper or a finance paper?" "Have you controlled for accruals quality?" "What about the selection into treatment?" "Does this survive the Hribar-Collins adjustment?"
**Referee pool:** CREDIBILITY (high), MEASUREMENT (high), STRUCTURAL (medium), THEORY (medium), SKEPTIC (low), POLICY (low)

### Journal of Accounting and Economics (JAE)
**Focus:** Economic analysis of accounting — contracting, regulation, capital markets, disclosure
**Bar:** Must have a clear economic framework. JAE values theory-motivated empirical work. The most economics-flavored accounting journal.
**Domain referee adjusts:** Agency theory and contracting framework expected. Understanding of SEC regulation, SOX, Dodd-Frank implications. CEO compensation and governance. Tax avoidance and tax planning. Positive accounting theory tradition.
**Methods referee adjusts:** Theory-driven hypotheses expected — not data-mining. Structural approaches valued alongside reduced-form. Large-sample archival methods with careful endogeneity treatment. Instrument validity in governance studies especially scrutinized.
**Typical concerns:** "What's the economic theory behind this prediction?" "Is this a contracting or valuation story?" "Have you addressed the Leamer critique?" "What about omitted variable bias?"
**Referee pool:** THEORY (high), STRUCTURAL (high), CREDIBILITY (medium), MEASUREMENT (medium), SKEPTIC (low), POLICY (low)

### The Accounting Review (TAR)
**Focus:** Broadest accounting journal — financial, managerial, auditing, tax, systems
**Bar:** Significant contribution to accounting knowledge. More methodologically diverse than JAR/JAE — accepts experiments, surveys, and analytical work alongside archival.
**Domain referee adjusts:** Broader scope than JAR/JAE — managerial accounting, cost accounting, and accounting education also considered. Practical implications for accounting profession valued. Standard-setting relevance appreciated.
**Methods referee adjusts:** Archival papers: similar identification standards to JAR. Experiments: proper randomization, demand effects, external validity. Surveys: response rates, non-response bias. Tax papers: knowledge of IRC provisions expected.
**Typical concerns:** "What are the implications for standard-setters?" "Does this generalize beyond your sample?" "Have you addressed self-selection?" "What about the tax implications?"
**Referee pool:** CREDIBILITY (medium), MEASUREMENT (high), POLICY (medium), STRUCTURAL (medium), THEORY (medium), SKEPTIC (low)

### Contemporary Accounting Research (CAR)
**Focus:** All areas of accounting — international perspective, methodological innovation
**Bar:** Solid accounting research with clear contribution. More international scope than US-centric TAR/JAR. Good outlet for methodological contributions to accounting.
**Domain referee adjusts:** International accounting standards (IFRS adoption, cross-country comparisons) valued. Canadian and international evidence welcome alongside US. Innovative measurement approaches.
**Methods referee adjusts:** Same rigor as TAR for archival work. Novel econometric approaches to accounting problems valued. Textual analysis and machine learning applications increasingly accepted. Careful treatment of measurement error in accounting variables.
**Typical concerns:** "Does this apply outside the US?" "How sensitive are results to the accrual measure used?" "Have you considered IFRS vs. GAAP differences?"
**Referee pool:** MEASUREMENT (high), CREDIBILITY (high), SKEPTIC (medium), POLICY (low), STRUCTURAL (low), THEORY (low)

---

## Marketing

### Journal of Marketing Research (JMR)
**Focus:** Marketing research methods and substantive findings — consumer behavior, pricing, advertising, digital marketing
**Bar:** Methodological rigor with marketing substance. Values causal identification and experimental design. The most empirically rigorous marketing journal.
**Domain referee adjusts:** Must speak to marketing managers and academics. Consumer welfare and firm implications. Understanding of marketing mix (price, promotion, distribution, product). Digital marketing and platform economics increasingly important.
**Methods referee adjusts:** Experiments (lab and field) held to high standards — randomization checks, demand effects, external validity. Structural demand models (BLP-style) valued. Causal inference from observational data must be convincing. Machine learning for prediction vs. causal inference distinction expected.
**Typical concerns:** "What's the managerial implication?" "Can you run a field experiment to validate?" "Have you addressed endogeneity of price/advertising?" "What about demand-side vs. supply-side effects?"
**Referee pool:** CREDIBILITY (high), STRUCTURAL (high), MEASUREMENT (medium), POLICY (medium), THEORY (low), SKEPTIC (low)

### Marketing Science
**Focus:** Quantitative marketing — structural models, field experiments, econometric analysis of marketing phenomena
**Bar:** Technical sophistication expected. The most methods-intensive marketing journal. Structural estimation and formal models highly valued.
**Domain referee adjusts:** Quantitative marketing models — demand estimation, pricing optimization, advertising response, customer lifetime value. Platform economics and two-sided markets. Competitive strategy implications. Welfare analysis of marketing practices.
**Methods referee adjusts:** Structural models expected for many topics (demand estimation, dynamic pricing, entry/exit). BLP, nested logit, mixed logit standard vocabulary. Field experiments and A/B testing with proper inference. Bayesian methods accepted. Counterfactual simulations expected alongside reduced-form.
**Typical concerns:** "Can you estimate a structural model?" "What's the counterfactual policy simulation?" "Have you estimated price elasticities?" "What about consumer heterogeneity?"
**Referee pool:** STRUCTURAL (high), THEORY (high), MEASUREMENT (medium), CREDIBILITY (medium), SKEPTIC (low), POLICY (low)

### Journal of Consumer Research (JCR)
**Focus:** Consumer behavior — psychology of consumption, decision-making, identity, culture
**Bar:** Theoretical contribution to understanding consumer behavior. Values conceptual novelty and experimental rigor. More behavioral/psychological than JMR or Marketing Science.
**Domain referee adjusts:** Psychological theory of consumer behavior expected. Process evidence (mediation, moderation) valued. Identity, motivation, judgment and decision-making frameworks. Cultural and sociological perspectives also accepted. Less emphasis on managerial implications than JMR.
**Methods referee adjusts:** Experimental designs dominant — proper controls, manipulation checks, attention checks. Multiple studies showing robustness and boundary conditions expected. Effect sizes and confidence intervals. Replication of core finding across studies. Pre-registration viewed favorably.
**Typical concerns:** "What's the underlying psychological process?" "Can you show mediation?" "What are the boundary conditions?" "Have you replicated across different contexts?"
**Referee pool:** THEORY (high), MEASUREMENT (high), SKEPTIC (medium), CREDIBILITY (medium), STRUCTURAL (low), POLICY (low)

---

## Management and Strategy

### Management Science
**Focus:** Interdisciplinary — operations, finance, marketing, strategy, economics, behavioral science, organizations, information systems
**Bar:** Technically rigorous work that spans business disciplines. Values formal models AND clean empirical work. Extremely broad scope — the most interdisciplinary top business journal.
**Domain referee adjusts:** Paper must fit one of the departments (operations, finance, marketing, etc.) but speak to a broader audience. Practical implications valued. Model-driven empirical work appreciated. Accepts papers that wouldn't fit neatly into a single field journal.
**Methods referee adjusts:** Standards match the relevant field (finance papers judged by finance methods standards, etc.). Structural estimation, causal inference, and field experiments all welcome. Simulation and computational methods accepted. Optimization and analytical models alongside empirical work.
**Typical concerns:** "Which department does this fit?" "Is this a Management Science paper or a field journal paper?" "What's the practical implication?" "Does the model match the empirics?"
**Referee pool:** STRUCTURAL (high), CREDIBILITY (high), THEORY (medium), MEASUREMENT (medium), POLICY (low), SKEPTIC (low)

### Strategic Management Journal (SMJ)
**Focus:** Strategy — competitive advantage, diversification, alliances, innovation, governance, entrepreneurship
**Bar:** Significant contribution to strategic management theory and practice. Empirical papers need strong identification. Theory papers need testable implications.
**Domain referee adjusts:** Resource-based view, dynamic capabilities, competitive dynamics, industry analysis. Understanding of firm heterogeneity and sustained competitive advantage. Alliance formation, M&A, and diversification. Innovation strategy and technology competition.
**Methods referee adjusts:** Endogeneity is the central concern — firm strategy is endogenous by nature. Instrumental variables, DiD around exogenous shocks, matching methods. Panel data with firm fixed effects expected. Selection models for entry/exit decisions. Heckman corrections common.
**Typical concerns:** "Is strategy endogenous here?" "What about unobserved firm heterogeneity?" "Can you identify the causal effect of this strategic choice?" "What's the theory of competitive advantage?"
**Referee pool:** THEORY (high), CREDIBILITY (high), STRUCTURAL (medium), SKEPTIC (medium), MEASUREMENT (low), POLICY (low)

### Administrative Science Quarterly (ASQ)
**Focus:** Organization theory and behavior — institutions, networks, culture, power, status, organizational design
**Bar:** Deep theoretical contribution with rigorous evidence. ASQ values papers that change how you think about organizations. Accepts qualitative, quantitative, and mixed methods.
**Domain referee adjusts:** Institutional theory, organizational ecology, network theory, social categorization. Status and legitimacy in markets. Organizational identity and culture. Power and politics in organizations. Historical and comparative analysis valued.
**Methods referee adjusts:** Quantitative papers: panel data, fixed effects, causal identification expected. Qualitative papers: systematic data collection, coding protocols, theoretical sampling. Mixed methods: integration of qualitative and quantitative evidence. Ethnographic work accepted if theoretically motivated.
**Typical concerns:** "What's the theoretical mechanism?" "How does this advance organization theory?" "Is this generalizable beyond your empirical context?" "Have you considered alternative theoretical explanations?"
**Referee pool:** THEORY (high), MEASUREMENT (high), STRUCTURAL (medium), CREDIBILITY (medium), POLICY (low), SKEPTIC (low)

---

## Engineering and Materials Science

> In engineering journals the referee dispositions map as follows:
> **STRUCTURAL** → experimental design & methodology rigor · **CREDIBILITY** → validation & reproducibility · **MEASUREMENT** → instrumentation, uncertainty, data quality · **POLICY** → industrial applicability & sustainability · **THEORY** → governing equations, modelling, analytical framework · **SKEPTIC** → adversarial, questions every assumption

---

**Heat Transfer & Thermal Engineering — Top Field**

### International Journal of Heat and Mass Transfer (IJHMT)
**Focus:** Fundamental and applied heat and mass transfer — convection, conduction, radiation, phase change, mass transfer, heat exchangers
**Bar:** The reference journal for heat transfer. Rigorous experimental or numerical work with clear novelty over existing correlations and models. Incremental improvements to geometry or operating conditions are insufficient unless the mechanism is new.
**Domain referee adjusts:** Governing dimensionless groups must be correctly defined and justified. Comparison against established correlations (Dittus-Boelter, Gnielinski, etc.) required. Boundary conditions must be fully specified. Thermophysical properties evaluated at the correct reference temperature. Heat balance closure must be demonstrated.
**Methods referee adjusts:** Experimental: uncertainty analysis mandatory (Kline & McClintock or GUM). Grid independence study required for numerical work. Validation against benchmark data or analytical solutions before novel predictions. Mesh and time-step convergence documented. Turbulence model selection justified.
**Typical concerns:** "What's the novelty over existing correlations?" "Where is the uncertainty analysis?" "Have you validated the model against independent data?" "Are the thermophysical properties correctly evaluated?" "Does the heat balance close?"
**Referee pool:** THEORY (high), MEASUREMENT (high), CREDIBILITY (high), STRUCTURAL (medium), SKEPTIC (medium), POLICY (low)

### Applied Thermal Engineering (ATE)
**Focus:** Applied heat transfer and thermodynamics — industrial systems, heat exchangers, HVAC, energy conversion, thermal management
**Bar:** Strong applied focus. Must demonstrate engineering relevance beyond the laboratory. Performance improvement over current technology must be quantified.
**Domain referee adjusts:** System-level performance metrics required (COP, effectiveness, efficiency). Comparison against commercial or benchmark systems. Energy and exergy analysis valued. Operating conditions must reflect realistic industrial scenarios, not just laboratory optima.
**Methods referee adjusts:** Experimental validation of numerical models required if both are presented. Uncertainty propagation through derived quantities (effectiveness, COP). Parametric studies showing sensitivity to key variables. Economic or environmental impact analysis strengthens the paper.
**Typical concerns:** "How does this compare to current commercial solutions?" "What are the realistic operating conditions?" "Where is the exergy analysis?" "Have you quantified the uncertainty in the derived efficiency metrics?"
**Referee pool:** POLICY (high), MEASUREMENT (high), CREDIBILITY (medium), STRUCTURAL (medium), THEORY (low), SKEPTIC (medium)

---

**Heat Transfer & Thermal Engineering — Strong Field**

### Experimental Thermal and Fluid Science (ETFS)
**Focus:** Experimental investigation of thermal and fluid phenomena — measurement techniques, flow visualization, heat transfer coefficients
**Bar:** Experimental rigor is the primary criterion. Novel measurement methodology or systematic characterization of a phenomenon not previously measured. Instrumentation and uncertainty must be impeccable.
**Domain referee adjusts:** Measurement technique must be described in sufficient detail for replication. Sensor calibration documented. Repeatability demonstrated (replicate runs). Flow conditions fully characterized (Re, boundary conditions). Comparison with theory or correlations required.
**Methods referee adjusts:** Expanded uncertainty (k=2, 95% confidence) mandatory for all reported quantities. Propagation from raw measurements to derived quantities shown explicitly. Systematic and random errors separated. Number of replicate experiments sufficient to estimate repeatability.
**Typical concerns:** "How were the sensors calibrated?" "What is the uncertainty in the reported heat transfer coefficient?" "How many replicates were run?" "Is the flow fully developed at the measurement location?"
**Referee pool:** MEASUREMENT (high), CREDIBILITY (high), STRUCTURAL (medium), SKEPTIC (medium), THEORY (low), POLICY (low)

### International Communications in Heat and Mass Transfer (ICHMT)
**Focus:** Short communications — rapid publication of significant new results in heat and mass transfer
**Bar:** Single focused result, letter format. Novel finding that warrants rapid communication; not a full study. 4,000–6,000 words maximum.
**Domain referee adjusts:** One clear, novel result. No room for comprehensive parametric studies — save those for IJHMT. The finding must stand on its own without extensive context.
**Methods referee adjusts:** Shorter but rigorous. Uncertainty still required. Validation concise but present. Reproducibility must be apparent from the description even if details are condensed.
**Typical concerns:** "Is this a full IJHMT paper in disguise?" "What is the single key finding?" "Is the novelty sufficient for a rapid communication?"
**Referee pool:** SKEPTIC (high), MEASUREMENT (medium), CREDIBILITY (medium), THEORY (medium), STRUCTURAL (low), POLICY (low)

### Journal of Heat Transfer (JHT — ASME Transactions)
**Focus:** Fundamental heat transfer, thermodynamics, and fluid mechanics — ASME audience (mechanical engineering)
**Bar:** Fundamental contribution, often with analytical or theoretical basis. ASME values rigorous derivations alongside experiments.
**Domain referee adjusts:** ASME nomenclature conventions. SI units mandatory. Analytical or theoretical framework expected even for experimental papers. Dimensional analysis before experiments.
**Methods referee adjusts:** ASME format for uncertainty (ASME PTC 19.1). Grid independence mandatory for CFD. Turbulence model selection with justification. Comparison to analytical solutions where available.
**Typical concerns:** "Where is the analytical framework?" "Are the SI units used consistently?" "Have you followed ASME uncertainty standards?"
**Referee pool:** THEORY (high), MEASUREMENT (high), CREDIBILITY (medium), STRUCTURAL (medium), SKEPTIC (low), POLICY (low)

---

**Energy & Buildings**

### Energy and Buildings (E&B)
**Focus:** Energy use in buildings — HVAC, passive cooling, thermal comfort, building envelopes, renewable integration
**Bar:** Demonstrated energy savings or comfort improvement. Real building or validated simulation. Climate context required.
**Domain referee adjusts:** Climate zone must be specified. Comparison against baseline building code or conventional system. Comfort metrics (PMV, PPD, operative temperature) alongside energy metrics. Life cycle perspective valued.
**Methods referee adjusts:** Building simulation (EnergyPlus, TRNSYS, IDA ICE) must be validated against measured data. Uncertainty in simulation inputs acknowledged. Annual energy performance, not just peak conditions.
**Typical concerns:** "What climate zone?" "What is the baseline for comparison?" "Is the simulation validated?" "What are the thermal comfort implications?"
**Referee pool:** POLICY (high), CREDIBILITY (medium), MEASUREMENT (medium), STRUCTURAL (medium), THEORY (low), SKEPTIC (medium)

### Applied Energy
**Focus:** Energy conversion, storage, and efficiency — renewable energy systems, energy policy, smart grids, decarbonization
**Bar:** Quantified energy/emissions impact. System-level analysis. High engineering and policy relevance.
**Domain referee adjusts:** Life cycle assessment or techno-economic analysis strengthens the paper significantly. Scalability discussion required. Comparison against current energy mix or alternative solutions.
**Methods referee adjusts:** Energy balance closure. Simulation validated against real plant data. Sensitivity and uncertainty analysis on key economic/environmental parameters. Monte Carlo for uncertainty propagation in TEA/LCA.
**Typical concerns:** "What is the levelized cost?" "Have you done an LCA?" "How does this scale to real-world deployment?" "What are the CO₂ savings?"
**Referee pool:** POLICY (high), STRUCTURAL (medium), CREDIBILITY (medium), MEASUREMENT (medium), THEORY (low), SKEPTIC (medium)

---

**Additive Manufacturing & Manufacturing Processes**

### Additive Manufacturing (AM — Elsevier)
**Focus:** All additive manufacturing processes and materials — process–structure–property relationships, design for AM, post-processing, characterization
**Bar:** The top journal for AM research. Must advance understanding of process–structure–property relationships or introduce a genuinely new capability. Process parameter studies without microstructural or property linkage are insufficient.
**Domain referee adjusts:** AM process fully described: machine, parameters (layer thickness, exposure time, power, scan strategy), atmosphere, post-processing. Material characterization beyond density — microstructure, phases, defects. Property comparison against wrought or conventionally manufactured equivalent.
**Methods referee adjusts:** Statistical design (DOE) expected for parameter studies. Characterization techniques validated (XRD, SEM/EDS, TEM if needed). Mechanical testing following standard (ASTM, ISO). Defect analysis (porosity, cracking, delamination) quantified.
**Typical concerns:** "What is the process–structure–property linkage?" "How does this compare to conventional manufacturing?" "Is the DOE statistically valid?" "Have you characterized the microstructure, not just the density?"
**Referee pool:** STRUCTURAL (high), MEASUREMENT (high), CREDIBILITY (high), THEORY (medium), SKEPTIC (medium), POLICY (low)

### Journal of Manufacturing Processes (JMP)
**Focus:** Manufacturing processes — machining, forming, joining, AM, surface engineering, process monitoring
**Bar:** Process innovation or systematic characterization with engineering application. Practical manufacturing relevance required.
**Domain referee adjusts:** Process parameters and their ranges must be industrially realistic. Comparison with conventional process. Surface quality, dimensional accuracy, or part properties must be quantified. Economic feasibility discussed.
**Methods referee adjusts:** DOE (Taguchi, RSM, Box-Behnken) expected for parameter optimization. ANOVA for factor significance. Regression models validated. Measurement system analysis (Gage R&R) for key responses.
**Typical concerns:** "Are the process parameters industrially relevant?" "What is the Gage R&R for your measurement system?" "Have you validated the regression model?"
**Referee pool:** STRUCTURAL (high), MEASUREMENT (high), POLICY (medium), CREDIBILITY (medium), THEORY (low), SKEPTIC (low)

### Journal of Materials Processing Technology (JMPT)
**Focus:** Materials processing — forming, casting, welding, heat treatment, surface modification, AM, machining
**Bar:** Rigorous experimental study linking processing parameters to material structure and properties. High impact factor for manufacturing — novelty threshold is significant.
**Domain referee adjusts:** Process–microstructure–property chain must be closed. Characterization at multiple scales (macro, micro, nano if relevant). Failure analysis for negative results also valued. Industrial process conditions.
**Methods referee adjusts:** Full factorial or response surface DOE for parameter studies. Microstructural characterization (SEM, EBSD, XRD) to support property claims. Mechanical testing per standard. FEM simulation validated against experiments if included.
**Typical concerns:** "The process–property link is missing." "What does the microstructure look like?" "Are the mechanical tests following a standard?" "Where is the FEM validation?"
**Referee pool:** MEASUREMENT (high), STRUCTURAL (high), CREDIBILITY (high), THEORY (medium), POLICY (low), SKEPTIC (medium)

### Virtual and Physical Prototyping (VPP)
**Focus:** AM processes, design for AM, 4D printing, multi-material AM, process simulation, in-situ monitoring
**Bar:** Strong AM focus. Process innovation, novel material–process combinations, or in-situ characterization. Design for AM (DfAM) with demonstrated performance improvement.
**Domain referee adjusts:** Process parameters fully reported. In-situ or ex-situ characterization linked to process conditions. DfAM papers must quantify performance gain (weight, topology, thermal) vs. conventional design.
**Methods referee adjusts:** In-situ monitoring data (melt pool, layer imaging) must be correlated to part quality metrics. Statistical evaluation of dimensional accuracy and surface roughness. Post-processing effects on final properties must be separated from as-built effects.
**Typical concerns:** "How do the process parameters affect the in-situ signatures?" "What is the dimensional accuracy vs. CAD?" "Have you separated as-built from post-processed properties?"
**Referee pool:** STRUCTURAL (high), MEASUREMENT (high), CREDIBILITY (medium), THEORY (medium), SKEPTIC (medium), POLICY (low)

### Rapid Prototyping Journal (RPJ)
**Focus:** Rapid prototyping, AM, tooling, reverse engineering, product development — broad AM scope including polymer, metal, ceramic
**Bar:** Applied AM with clear product or process benefit. Less fundamental than Additive Manufacturing journal — engineering application and practical novelty sufficient.
**Domain referee adjusts:** Application context must be clear and realistic. Dimensional accuracy and surface finish are primary quality metrics. Material properties in context of the intended application. Cost or lead-time comparison vs. alternative manufacturing valued.
**Methods referee adjusts:** Dimensional metrology (CMM, 3D scanning) with GD&T interpretation. Surface roughness measurement (Ra, Rz). Mechanical testing per standard. Process time and cost analysis.
**Typical concerns:** "How does dimensional accuracy compare to the tolerance required by the application?" "What is the surface finish relative to the function?" "Have you compared cost and lead time vs. conventional manufacturing?"
**Referee pool:** POLICY (high), MEASUREMENT (high), STRUCTURAL (medium), CREDIBILITY (medium), THEORY (low), SKEPTIC (low)

### Progress in Additive Manufacturing (PIAM)
**Focus:** Reviews, perspectives, and original research on AM — all processes, all materials, simulation, standardization, sustainability
**Bar:** Review papers: comprehensive, systematic, with clear gaps identified. Original research: novel contribution to AM science or technology with broader implications for the field.
**Domain referee adjusts:** Reviews must be systematic (search strategy documented). Original papers must contextualize within the AM technology landscape. Sustainability and circular economy perspective valued.
**Methods referee adjusts:** Reviews: PRISMA protocol or equivalent for systematic literature reviews. Original research: standard characterization and testing with statistical rigor.
**Typical concerns:** "Is the review systematic?" "What are the research gaps identified?" "How does this contribute to AM standardization or sustainability?"
**Referee pool:** STRUCTURAL (high), POLICY (high), CREDIBILITY (medium), MEASUREMENT (medium), THEORY (low), SKEPTIC (medium)

### Journal of Manufacturing Science and Engineering (JMSE — ASME)
**Focus:** Manufacturing processes, systems, and automation — machining, forming, AM, metrology, process control (ASME audience)
**Bar:** Rigorous engineering science. Analytical model validated by experiment is the ideal ASME paper. Pure experimental or pure simulation acceptable if contribution is significant.
**Domain referee adjusts:** ASME notation and SI units. Governing equations of the process must be presented. Manufacturing system perspective (process → quality → cost) expected.
**Methods referee adjusts:** Analytical or semi-analytical model preferred alongside experiments. FEM for process simulation must include validation. Statistical analysis of experimental results (ANOVA, regression). Uncertainty per ASME PTC 19.1.
**Typical concerns:** "Where is the analytical model?" "Have you validated the simulation against experiments?" "What is the process physics underlying the observation?"
**Referee pool:** THEORY (high), MEASUREMENT (high), STRUCTURAL (high), CREDIBILITY (medium), SKEPTIC (medium), POLICY (low)

---

**Materials Science**

### Acta Materialia
**Focus:** Physical and mechanical metallurgy, materials science — microstructure, mechanical properties, phase transformations, defects
**Bar:** Top materials science journal. Fundamental materials science insight, not just characterization. Must advance understanding of structure–property relationships at a mechanistic level.
**Domain referee adjusts:** Deep mechanistic understanding required — not just "material X has property Y" but "why." Phase diagrams, thermodynamic arguments, dislocation theory, fracture mechanics as appropriate. First-principles or CALPHAD supporting experimental findings valued.
**Methods referee adjusts:** Multi-scale characterization expected: SEM/EBSD for texture, TEM for defect structure, APT for compositional analysis where relevant. Mechanical testing statistically sound (n ≥ 5 per condition). DIC for strain field analysis valued. Modeling (MD, DFT, phase field) alongside experiments for mechanism elucidation.
**Typical concerns:** "What is the mechanism?" "Can you support this with TEM or APT?" "Where is the thermodynamic justification?" "The microstructural evidence is insufficient to support the claim."
**Referee pool:** THEORY (high), MEASUREMENT (high), CREDIBILITY (high), STRUCTURAL (medium), SKEPTIC (high), POLICY (low)

### Materials & Design
**Focus:** Materials selection, design, and characterization — functional materials, composites, coatings, biomaterials, AM materials
**Bar:** Applied materials science with clear design relevance. Novelty in material composition, processing route, or application. Less fundamental than Acta Materialia — application-driven.
**Domain referee adjusts:** Design motivation must be clear. Comparison against current material alternatives. Multi-functional properties valued (mechanical + thermal + corrosion, etc.). Sustainability and recyclability increasingly weighted.
**Methods referee adjusts:** Full characterization suite expected. Statistical analysis of mechanical data. Failure analysis (fractography) for mechanical property claims. Aging or degradation study if the application involves environmental exposure.
**Typical concerns:** "Why is this better than existing materials?" "Have you characterized degradation under service conditions?" "Is the sample size sufficient for statistical conclusions?"
**Referee pool:** POLICY (high), MEASUREMENT (high), STRUCTURAL (medium), CREDIBILITY (medium), THEORY (low), SKEPTIC (medium)

### Journal of the European Ceramic Society (JECS)
**Focus:** Ceramics and glass — processing, microstructure, mechanical and functional properties, ceramic composites
**Bar:** Significant advance in ceramic science or technology. Processing–microstructure–property relationships. Functional ceramics (dielectrics, piezoelectrics, bioceramics) alongside structural ceramics.
**Domain referee adjusts:** Sintering conditions fully specified. Phase identification by XRD mandatory. Microstructural characterization (SEM, density by Archimedes). Mechanical testing following EN/ISO standards. Thermal stability for high-temperature applications.
**Methods referee adjusts:** Relative density must be reported. XRD with Rietveld refinement for quantitative phase analysis. Weibull statistics for brittle fracture data. Thermal analysis (TGA/DSC) for processing studies.
**Typical concerns:** "What is the sintering mechanism?" "Where is the Weibull analysis?" "Have you identified all phases by XRD?" "Is the relative density sufficient for the claimed properties?"
**Referee pool:** MEASUREMENT (high), STRUCTURAL (high), CREDIBILITY (medium), THEORY (medium), SKEPTIC (medium), POLICY (low)

---

**Specialty / Open Access**

### Case Studies in Thermal Engineering
**Focus:** Applied thermal engineering case studies — real systems, industry-relevant conditions, engineering solutions
**Bar:** Lower novelty threshold than top journals. Must present a complete, well-documented engineering case with transferable lessons. Rigorous within its scope.
**Domain referee adjusts:** Real or realistic system. Engineering conclusions transferable to similar applications. No need for fundamental novelty — thorough documentation of a well-executed applied study is sufficient.
**Methods referee adjusts:** Uncertainty analysis still required. Validation against real system data preferred. Clear presentation of operating conditions and boundary conditions.
**Typical concerns:** "What are the transferable lessons?" "Is the case documented in sufficient detail for replication?" "Where is the uncertainty analysis?"
**Referee pool:** POLICY (high), MEASUREMENT (medium), CREDIBILITY (medium), STRUCTURAL (medium), THEORY (low), SKEPTIC (low)

### Thermal Science and Engineering Progress (TSEP)
**Focus:** Thermal engineering progress — heat transfer, energy systems, thermal management, emerging technologies
**Bar:** Sound engineering work with practical relevance. More accessible than IJHMT but rigour expected.
**Domain referee adjusts:** Clear motivation and application context. Parametric results must be presented systematically. Correlations or design guidelines from the results valued.
**Methods referee adjusts:** Uncertainty analysis required. Validation against literature data acceptable when experiments not feasible. Mesh independence for CFD.
**Typical concerns:** "Have you compared against existing correlations?" "Where is the uncertainty?" "Can you derive a design correlation from these results?"
**Referee pool:** MEASUREMENT (medium), CREDIBILITY (medium), POLICY (medium), STRUCTURAL (medium), THEORY (low), SKEPTIC (low)

### Results in Engineering
**Focus:** Broad engineering — preliminary results, negative results, replication studies, short communications
**Bar:** Sound methodology and honest reporting. Values completeness and reproducibility over impact. Accepts negative and confirmatory results.
**Domain referee adjusts:** Scope is very broad — any engineering discipline. The key criterion is methodological soundness, not novelty. Replication studies explicitly welcomed.
**Methods referee adjusts:** Reproducibility and transparency are primary. Data must be available (open data encouraged). Methods described in sufficient detail for replication.
**Typical concerns:** "Is the methodology sound?" "Are the data available?" "Is the description sufficient for replication?"
**Referee pool:** CREDIBILITY (high), MEASUREMENT (medium), STRUCTURAL (medium), POLICY (low), THEORY (low), SKEPTIC (low)

---

## Add Your Own Journal

Copy this template and add it above this section:

```markdown
### [Journal Name] ([Abbreviation])
**Focus:** [fields and topics covered]
**Bar:** [what it takes to publish here]
**Domain referee adjusts:** [what matters most to domain reviewers at this journal]
**Methods referee adjusts:** [rigor expectations, preferred methods, required checks]
**Typical concerns:** [common referee questions at this journal]
**Referee pool:** [disposition] (high/medium/low) for each: STRUCTURAL, CREDIBILITY, MEASUREMENT, POLICY, THEORY, SKEPTIC
**Table format:** [optional — only include if journal deviates from default (stars OK). E.g., "No significance stars (AEA style)."]
```
