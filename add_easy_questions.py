#!/usr/bin/env python3
"""
Script to add easy questions to the quiz
"""

# Easy questions to insert (50 total: 10 per week)
easy_questions = """            // EASY QUESTIONS - Original simpler versions
            // Week 1: Global Imbalances - Easy (10 questions)
            {
                week: 1,
                difficulty: "easy",
                topic: "Balance of Payments Components",
                question: "The Balance of Payments consists of which main components?",
                options: [
                    "Current Account + Financial Account + Capital Account",
                    "Trade Balance + Income Balance only",
                    "Exports + Imports + Transfers",
                    "GDP + Net Exports + Government Spending"
                ],
                correct: 0,
                explanation: "The Balance of Payments = Current Account + Financial Account + Capital Account."
            },
            {
                week: 1,
                difficulty: "easy",
                topic: "Balance of Payments Components",
                question: "What does the Trade Balance measure?",
                options: [
                    "Total government spending on trade",
                    "Exports minus Imports of goods and services",
                    "Foreign investment flows",
                    "Net unilateral transfers"
                ],
                correct: 1,
                explanation: "Trade Balance = Exports - Imports (goods & services)."
            },
            {
                week: 1,
                difficulty: "easy",
                topic: "NIIP and Valuation",
                question: "Net International Investment Position (NIIP) is calculated as:",
                options: [
                    "Current Account - Trade Balance",
                    "Exports - Imports",
                    "Foreign Assets - Foreign Liabilities",
                    "GDP - National Debt"
                ],
                correct: 2,
                explanation: "NIIP = Foreign Assets - Foreign Liabilities. It represents accumulated wealth position."
            },
            {
                week: 1,
                difficulty: "easy",
                topic: "NIIP and Valuation",
                question: "What is the relationship between Current Account deficits and NIIP?",
                options: [
                    "Current Account Deficit causes NIIP to rise",
                    "Current Account Deficit causes NIIP to fall",
                    "They are unrelated",
                    "Current Account Deficit doubles the NIIP"
                ],
                correct: 1,
                explanation: "A Current Account Deficit leads to a fall in NIIP, while a Current Account Surplus causes NIIP to rise."
            },
            {
                week: 1,
                difficulty: "easy",
                topic: "Global Creditors and Debtors",
                question: "Which of the following is a major external creditor?",
                options: [
                    "United States",
                    "United Kingdom",
                    "Japan",
                    "Australia"
                ],
                correct: 2,
                explanation: "Japan, China, and Germany are major external creditors. The US is the world's largest debtor."
            },
            {
                week: 1,
                difficulty: "easy",
                topic: "NIIP and Valuation",
                question: "Why might NIIP not equal accumulated current accounts?",
                options: [
                    "Because of calculation errors",
                    "Because of valuation changes from market price movements",
                    "Because trade is measured incorrectly",
                    "They are always equal"
                ],
                correct: 1,
                explanation: "NIIP changes from two sources: (1) Current Account flows and (2) Valuation changes (stock/bond prices, exchange rates)."
            },
            {
                week: 1,
                difficulty: "easy",
                topic: "NIIP and Valuation",
                question: "During 2002-2007, the US ran $3.9 trillion in current account deficits but NIIP improved by $80 billion. What explains this?",
                options: [
                    "Measurement error",
                    "$4 trillion in positive valuation changes",
                    "Increased exports",
                    "Reduced imports"
                ],
                correct: 1,
                explanation: "The US benefited from $4 trillion in positive valuation changes, offsetting the current account deficits."
            },
            {
                week: 1,
                difficulty: "easy",
                topic: "Dark Matter and Return Differential",
                question: "The 'Dark Matter' hypothesis suggests:",
                options: [
                    "The US has hidden debt obligations",
                    "Unmeasured intangible assets mean true NIIP might be positive",
                    "Foreign countries hide their investments",
                    "Trade statistics are completely wrong"
                ],
                correct: 1,
                explanation: "The Dark Matter hypothesis suggests unmeasured intangible assets (brands, know-how) mean the true NIIP might actually be positive."
            },
            {
                week: 1,
                difficulty: "easy",
                topic: "Dark Matter and Return Differential",
                question: "The 'Return Differential' hypothesis explains the NIIP-NII paradox by:",
                options: [
                    "The US borrows at high rates and lends at low rates",
                    "The US invests in high-return assets (stocks/FDI) while foreigners invest in low-return US assets (Treasury bonds)",
                    "All countries earn the same return",
                    "Returns don't matter for investment income"
                ],
                correct: 1,
                explanation: "The Return Differential hypothesis: US invests in high-return foreign assets while foreigners invest in low-return US assets, related to 'exorbitant privilege'."
            },
            {
                week: 1,
                difficulty: "easy",
                topic: "Balance of Payments Components",
                question: "Which is included in the Income Balance component of the Current Account?",
                options: [
                    "Exports and imports of goods",
                    "Net Investment Income and Net Compensation to Employees",
                    "Government transfers only",
                    "Capital gains on stocks"
                ],
                correct: 1,
                explanation: "Income Balance = Net Investment Income + Net Compensation to Employees."
            },

            // Week 2: Sustainability - Easy (10 questions)
            {
                week: 2,
                difficulty: "easy",
                topic: "Finite vs Infinite Horizon",
                question: "In a two-period economy with terminal condition B₂ = 0, can a net debtor run perpetual trade balance deficits?",
                options: [
                    "Yes, always",
                    "No, must run surplus in at least one period",
                    "Yes, but only if interest rates are negative",
                    "It depends on GDP growth"
                ],
                correct: 1,
                explanation: "In finite horizon, a net debtor cannot run perpetual TB deficits - must run a surplus in at least one period to satisfy the sustainability condition."
            },
            {
                week: 2,
                difficulty: "easy",
                topic: "Transversality Condition",
                question: "What is the transversality condition in the infinite horizon model?",
                options: [
                    "Debt must equal zero",
                    "The present value of debt must vanish: lim(T→∞) Bₜ/(1+r)ᵀ = 0",
                    "Debt must grow faster than interest rate",
                    "Current account must always be positive"
                ],
                correct: 1,
                explanation: "The transversality (No-Ponzi-Game) condition: lim(T→∞) Bₜ/(1+r)ᵀ = 0. Present value of debt must vanish (not that debt goes to zero)."
            },
            {
                week: 2,
                difficulty: "easy",
                topic: "Perpetual Deficits",
                question: "In infinite horizon, can a net debtor run perpetual current account deficits?",
                options: [
                    "No, never",
                    "Yes, if paying fraction α ∈ (0,1) of interest via trade surplus",
                    "Only if GDP shrinks",
                    "Only for one period"
                ],
                correct: 1,
                explanation: "Yes! A net debtor CAN run perpetual CA deficits in infinite horizon if following a debt-servicing policy: TBₜ = -αrBₜ₋₁ where α ∈ (0,1)."
            },
            {
                week: 2,
                difficulty: "easy",
                topic: "Debt Growth and Sustainability",
                question: "For perpetual CA deficits to be sustainable, debt must grow at rate g where:",
                options: [
                    "g > r (faster than interest rate)",
                    "g = r (equal to interest rate)",
                    "g < r, specifically g = r(1-α) where α > 0",
                    "g can be anything"
                ],
                correct: 2,
                explanation: "Debt must grow slower than interest rate: g = r(1-α) < r. This ensures the transversality condition is satisfied."
            },
            {
                week: 2,
                difficulty: "easy",
                topic: "Finite vs Infinite Horizon",
                question: "What is the key difference between finite and infinite horizon sustainability?",
                options: [
                    "No difference",
                    "Finite: hard constraint (Bₜ=0), Infinite: soft constraint (PV→0)",
                    "Finite is easier",
                    "Infinite requires balanced budgets"
                ],
                correct: 1,
                explanation: "Finite horizon has hard constraint (must settle all debts), infinite has soft constraint (can 'grow out of debt' as long as PV→0)."
            },
            {
                week: 2,
                difficulty: "easy",
                topic: "Accounting Identities",
                question: "The accounting identity Bₜ = (1+r)Bₜ₋₁ + TBₜ shows:",
                options: [
                    "How current NIIP relates to previous NIIP plus current trade balance",
                    "How GDP grows over time",
                    "The inflation rate",
                    "Government budget constraint"
                ],
                correct: 0,
                explanation: "This identity shows NIIP evolves as: current NIIP = previous NIIP with interest plus current trade balance."
            },
            {
                week: 2,
                difficulty: "easy",
                topic: "Accounting Identities",
                question: "The relationship between Current Account and Trade Balance is:",
                options: [
                    "CA = TB (they are identical)",
                    "CA = TB + rBₜ₋₁ (trade balance plus net investment income)",
                    "CA = TB × 2",
                    "They are unrelated"
                ],
                correct: 1,
                explanation: "Current Account = Trade Balance + rBₜ₋₁ (where rBₜ₋₁ represents net investment income)."
            },
            {
                week: 2,
                difficulty: "easy",
                topic: "Perpetual Deficits",
                question: "In infinite horizon, a net debtor CANNOT run perpetual:",
                options: [
                    "Current account deficits",
                    "Trade balance deficits",
                    "Both CA and TB deficits",
                    "Either CA or TB deficits"
                ],
                correct: 1,
                explanation: "Even in infinite horizon, a net debtor CANNOT run perpetual TB deficits (must repay real resources at some point), but CAN run perpetual CA deficits."
            },
            {
                week: 2,
                difficulty: "easy",
                topic: "Debt Growth and Sustainability",
                question: "For sustainability with perpetual CA deficits, GDP growth must be:",
                options: [
                    "Negative",
                    "Zero",
                    "≥ r(1-α) to generate required TB surpluses",
                    "< interest rate"
                ],
                correct: 2,
                explanation: "Critical condition: GDP must grow ≥ r(1-α) to generate the required TB surpluses for sustainability."
            },
            {
                week: 2,
                difficulty: "easy",
                topic: "Finite vs Infinite Horizon",
                question: "In a two-period model, the sustainability condition with B₀ < 0 (net debtor) is:",
                options: [
                    "(1+r)B₀ = -TB₁ - TB₂/(1+r)",
                    "B₀ = TB₁ + TB₂",
                    "(1+r)B₀ = TB₁ + TB₂",
                    "B₀ = 0"
                ],
                correct: 0,
                explanation: "The sustainability condition is (1+r)B₀ = -TB₁ - TB₂/(1+r), which shows present value of trade balances must offset initial debt."
            },

            // Week 3: Theory of Current Account - Easy (10 questions)
            {
                week: 3,
                difficulty: "easy",
                topic: "Small Open Economy Model",
                question: "In the small open economy model, what does 'small' mean?",
                options: [
                    "The country has a small population",
                    "World prices and interest rates are independent of domestic conditions",
                    "The economy produces few goods",
                    "GDP is low"
                ],
                correct: 1,
                explanation: "Small means world prices and interest rates are independent of domestic conditions - the country is a price taker."
            },
            {
                week: 3,
                difficulty: "easy",
                topic: "Small Open Economy Model",
                question: "Free capital mobility in the model implies:",
                options: [
                    "No restrictions on trade",
                    "r₁ = r* (domestic interest rate equals world rate)",
                    "No taxes",
                    "Fixed exchange rate"
                ],
                correct: 1,
                explanation: "Free capital mobility implies interest rate parity: r₁ = r*."
            },
            {
                week: 3,
                difficulty: "easy",
                topic: "Euler Equation and Optimization",
                question: "The Euler equation in the model represents:",
                options: [
                    "Budget constraint",
                    "Optimal consumption choice: U'(C₁) = (1+r₁)βU'(C₂)",
                    "Production function",
                    "Trade balance identity"
                ],
                correct: 1,
                explanation: "The Euler equation U'(C₁) = (1+r₁)βU'(C₂) characterizes optimal intertemporal consumption choice."
            },
            {
                week: 3,
                difficulty: "easy",
                topic: "Temporary vs Permanent Shocks",
                question: "How does a TEMPORARY decline in Q₁ affect the current account?",
                options: [
                    "Large CA deterioration (households borrow to smooth consumption)",
                    "No effect",
                    "Large CA improvement",
                    "Small CA deterioration"
                ],
                correct: 0,
                explanation: "Temporary shocks lead to large CA movements - households borrow to smooth consumption, causing CA to deteriorate significantly."
            },
            {
                week: 3,
                difficulty: "easy",
                topic: "Temporary vs Permanent Shocks",
                question: "How does a PERMANENT decline in output (Q₁ and Q₂) affect consumption?",
                options: [
                    "No change in consumption",
                    "C₁ falls by less than the output decline",
                    "Both C₁ and C₂ adjust proportionally, little change in trade balance",
                    "Only C₂ changes"
                ],
                correct: 2,
                explanation: "With permanent shocks, economies adjust consumption in both periods. The trade balance changes little because households cannot smooth a permanent shock."
            },
            {
                week: 3,
                difficulty: "easy",
                topic: "Temporary vs Permanent Shocks",
                question: "The general principle comparing temporary vs permanent shocks is:",
                options: [
                    "Both have identical effects",
                    "Economies finance temporary shocks (borrow/lend) and adjust to permanent ones",
                    "Economies ignore temporary shocks",
                    "Only permanent shocks matter"
                ],
                correct: 1,
                explanation: "Economies tend to FINANCE temporary shocks through international borrowing/lending and ADJUST to permanent shocks by changing consumption."
            },
            {
                week: 3,
                difficulty: "easy",
                topic: "Anticipated Income Shocks",
                question: "If households learn in period 1 that Q₂ will be higher (anticipated income shock), what happens to CA₁?",
                options: [
                    "CA₁ improves",
                    "CA₁ deteriorates (households borrow against future income)",
                    "No change in CA₁",
                    "CA₁ becomes zero"
                ],
                correct: 1,
                explanation: "Good news about future income causes CA to deteriorate - households increase C₁ by borrowing, even though Q₁ is unchanged."
            },
            {
                week: 3,
                difficulty: "easy",
                topic: "Budget Constraint",
                question: "The intertemporal budget constraint in the two-period model is:",
                options: [
                    "C₁ + C₂ = Q₁ + Q₂",
                    "C₁ + C₂/(1+r₁) = (1+r₀)B₀ + Q₁ + Q₂/(1+r₁)",
                    "C₁ = Q₁ and C₂ = Q₂",
                    "C₁ + C₂ = 2Q₁"
                ],
                correct: 1,
                explanation: "The intertemporal budget constraint: C₁ + C₂/(1+r₁) = (1+r₀)B₀ + Q₁ + Q₂/(1+r₁) - present value of consumption equals present value of resources."
            },
            {
                week: 3,
                difficulty: "easy",
                topic: "Budget Constraint",
                question: "Trade balance in period 1 is defined as:",
                options: [
                    "TB₁ = C₁ - Q₁",
                    "TB₁ = Q₁ - C₁",
                    "TB₁ = Q₁ + C₁",
                    "TB₁ = (Q₁ - C₁) × r"
                ],
                correct: 1,
                explanation: "Trade Balance: TB₁ = Q₁ - C₁ (output minus consumption)."
            },
            {
                week: 3,
                difficulty: "easy",
                topic: "Consumption Smoothing",
                question: "What does consumption smoothing mean?",
                options: [
                    "Consuming the same goods every period",
                    "Households prefer stable consumption over time using international borrowing/lending",
                    "Consumption always equals income",
                    "Avoiding imported goods"
                ],
                correct: 1,
                explanation: "Consumption smoothing: households prefer stable consumption over time (due to concave utility) and use international borrowing/lending to achieve this."
            },

            // Week 4: Terms of Trade - Easy (10 questions)
            {
                week: 4,
                difficulty: "easy",
                topic: "Terms of Trade",
                question: "The terms of trade (TT) is defined as:",
                options: [
                    "TT = Imports / Exports",
                    "TT = Price of Exports / Price of Imports",
                    "TT = Trade Balance / GDP",
                    "TT = Current Account / Financial Account"
                ],
                correct: 1,
                explanation: "Terms of trade (TT) = P^X / P^M, the relative price of exports in terms of imports."
            },
            {
                week: 4,
                difficulty: "easy",
                topic: "Terms of Trade",
                question: "A temporary improvement in terms of trade (TT₁ ↑) affects the current account by:",
                options: [
                    "CA₁ improves as country saves windfall",
                    "CA₁ deteriorates",
                    "No effect on CA",
                    "CA₁ becomes zero"
                ],
                correct: 0,
                explanation: "Temporary TT improvement: country saves windfall to smooth consumption → CA₁ improves."
            },
            {
                week: 4,
                difficulty: "easy",
                topic: "Terms of Trade",
                question: "A permanent improvement in terms of trade (TT₁ and TT₂ both ↑) has what effect on CA?",
                options: [
                    "Large CA improvement",
                    "Little change in CA (consumption rises in both periods)",
                    "Large CA deterioration",
                    "CA₁ doubles"
                ],
                correct: 1,
                explanation: "Permanent TT improvement: consumption increases in both periods proportionally → little CA change. Same principle as endowment shocks."
            },
            {
                week: 4,
                difficulty: "easy",
                topic: "World Interest Rate Shocks",
                question: "An increase in world interest rate r* has two effects. What are they?",
                options: [
                    "Inflation effect and deflation effect",
                    "Substitution effect and income effect",
                    "Supply effect and demand effect",
                    "Export effect and import effect"
                ],
                correct: 1,
                explanation: "r* ↑ creates: (1) Substitution effect: bonds more attractive → save more. (2) Income effect: depends on borrower/lender position."
            },
            {
                week: 4,
                difficulty: "easy",
                topic: "World Interest Rate Shocks",
                question: "For a net borrower (B₀ < 0), an increase in r* causes:",
                options: [
                    "Income and substitution effects reinforce → CA₁ improves",
                    "Income and substitution effects oppose",
                    "No effect on CA",
                    "Only substitution effect matters"
                ],
                correct: 0,
                explanation: "Net borrower: both effects reduce C₁ (substitution: save more; income: poorer) → CA₁ improves."
            },
            {
                week: 4,
                difficulty: "easy",
                topic: "World Interest Rate Shocks",
                question: "For a net lender (B₀ > 0), which effect typically dominates when r* increases?",
                options: [
                    "Income effect (richer → consume more)",
                    "Substitution effect (save more → standard assumption)",
                    "Both cancel exactly",
                    "Neither effect applies"
                ],
                correct: 1,
                explanation: "For lenders: effects oppose, but substitution effect typically dominates under standard preferences—savings increase with interest rate."
            },
            {
                week: 4,
                difficulty: "easy",
                topic: "Import Tariffs",
                question: "The modified Euler equation with tariffs is:",
                options: [
                    "U'(C₁) = β(1+r)U'(C₂)",
                    "U'(C₁) = [(1+τ₁)/(1+τ₂)]β(1+r)U'(C₂)",
                    "U'(C₁) = τ₁U'(C₂)",
                    "U'(C₁) = U'(C₂)"
                ],
                correct: 1,
                explanation: "With tariffs, the Euler equation becomes: U'(C₁) = [(1+τ₁)/(1+τ₂)]β(1+r)U'(C₂), where τ represents import tariffs."
            },
            {
                week: 4,
                difficulty: "easy",
                topic: "Import Tariffs",
                question: "A temporary tariff (τ₁ > 0, τ₂ = 0) affects consumption by:",
                options: [
                    "Making current consumption relatively expensive → C₁ ↓, CA₁ ↑",
                    "Making current consumption cheaper → C₁ ↑",
                    "No effect on consumption",
                    "Doubling current consumption"
                ],
                correct: 0,
                explanation: "Temporary tariff: (1+τ₁)/(1+τ₂) > 1 makes current consumption expensive → households postpone consumption → CA₁ improves."
            },
            {
                week: 4,
                difficulty: "easy",
                topic: "Import Tariffs",
                question: "A permanent tariff (τ₁ = τ₂ > 0) has what effect on the current account?",
                options: [
                    "Large CA improvement",
                    "No effect on CA (ratio (1+τ₁)/(1+τ₂) = 1)",
                    "Large CA deterioration",
                    "CA doubles"
                ],
                correct: 1,
                explanation: "Permanent tariff: (1+τ₁)/(1+τ₂) = 1 in Euler equation → no intertemporal distortion → no CA effect."
            },
            {
                week: 4,
                difficulty: "easy",
                topic: "Import Tariffs",
                question: "Why do permanent tariffs not affect the CA in this model?",
                options: [
                    "Tariffs don't affect trade",
                    "Tariff revenues are rebated lump-sum, and no intertemporal substitution is created",
                    "The model ignores tariffs",
                    "CA is always zero"
                ],
                correct: 1,
                explanation: "Tariff revenues are rebated (L_t = τ_t C_t), so economy-wide resources unchanged. Permanent tariffs don't create intertemporal distortion → no CA effect."
            },

            // Week 5: Production Economy - Easy (10 questions)
            {
                week: 5,
                difficulty: "easy",
                topic: "Production Economy",
                question: "In the production economy, output is determined by:",
                options: [
                    "Q_t = A_t F(I_{t-1}), where I is investment and A is productivity",
                    "Q_t = C_t (consumption)",
                    "Q_t = exogenous endowment",
                    "Q_t = exports - imports"
                ],
                correct: 0,
                explanation: "Production economy: Q_t = A_t F(I_{t-1}). Output depends on investment I_{t-1} and productivity A_t."
            },
            {
                week: 5,
                difficulty: "easy",
                topic: "Production Economy",
                question: "The marginal product of capital (MPK) is:",
                options: [
                    "MPK = A_t F'(I_{t-1})",
                    "MPK = F(I)",
                    "MPK = I / Q",
                    "MPK = 1 + r"
                ],
                correct: 0,
                explanation: "MPK = A_t F'(I_{t-1}), the additional output from one more unit of investment."
            },
            {
                week: 5,
                difficulty: "easy",
                topic: "Production Economy",
                question: "The firm's profit maximization condition is:",
                options: [
                    "A₂F'(I₁) = 1 + r₁ (MPK equals opportunity cost)",
                    "I₁ = S₁",
                    "MPK = 0",
                    "Q = C"
                ],
                correct: 0,
                explanation: "Firms invest until A₂F'(I₁) = 1 + r₁: marginal benefit (MPK) equals marginal cost (opportunity cost of funds)."
            },
            {
                week: 5,
                difficulty: "easy",
                topic: "Investment Schedule",
                question: "The investment schedule I₁ = I(r₁⁻, A₂⁺) shows:",
                options: [
                    "Investment decreases with r₁ (higher cost) and increases with A₂ (higher MPK)",
                    "Investment increases with r₁",
                    "Investment is constant",
                    "Investment equals savings"
                ],
                correct: 0,
                explanation: "∂I/∂r₁ < 0 (higher interest rate → higher cost → less investment). ∂I/∂A₂ > 0 (higher productivity → higher MPK → more investment)."
            },
            {
                week: 5,
                difficulty: "easy",
                topic: "Saving Schedule",
                question: "The saving schedule S₁ = S(r₁⁺, A₁⁺, A₂⁻) indicates:",
                options: [
                    "Saving increases with r₁ and current productivity A₁, decreases with future productivity A₂",
                    "Saving is constant",
                    "Saving only depends on r₁",
                    "Saving equals investment"
                ],
                correct: 0,
                explanation: "∂S/∂r₁ > 0 (save more when return is higher). ∂S/∂A₁ > 0 (temporary income boost → save). ∂S/∂A₂ < 0 (good news → borrow)."
            },
            {
                week: 5,
                difficulty: "easy",
                topic: "Current Account Schedule",
                question: "The current account is defined as:",
                options: [
                    "CA₁ = S₁ - I₁ (saving minus investment)",
                    "CA₁ = I₁ - S₁",
                    "CA₁ = Q₁",
                    "CA₁ = C₁"
                ],
                correct: 0,
                explanation: "In production economy: CA₁ = S₁ - I₁. The current account equals saving minus investment."
            },
            {
                week: 5,
                difficulty: "easy",
                topic: "Current Account Schedule",
                question: "A positive productivity shock in period 2 (A₂ ↑) affects CA₁ by:",
                options: [
                    "CA₁ deteriorates (I₁ ↑ and S₁ ↓)",
                    "CA₁ improves",
                    "No effect on CA₁",
                    "CA₁ doubles"
                ],
                correct: 0,
                explanation: "A₂ ↑: firms invest more (I₁ ↑) and households borrow against future income (S₁ ↓) → CA₁ = S₁ - I₁ deteriorates."
            },
            {
                week: 5,
                difficulty: "easy",
                topic: "Metzler Diagram",
                question: "In the Metzler diagram, the investment schedule I(r₁) slopes:",
                options: [
                    "Downward (higher r₁ → less investment)",
                    "Upward (higher r₁ → more investment)",
                    "Vertical",
                    "Horizontal"
                ],
                correct: 0,
                explanation: "Investment schedule slopes downward: higher interest rates increase opportunity cost → less investment."
            },
            {
                week: 5,
                difficulty: "easy",
                topic: "Metzler Diagram",
                question: "In the Metzler diagram, the saving schedule S(r₁) slopes:",
                options: [
                    "Upward (higher r₁ → save more)",
                    "Downward",
                    "Vertical",
                    "Horizontal"
                ],
                correct: 0,
                explanation: "Saving schedule slopes upward: higher interest rates make saving more attractive (substitution effect dominates)."
            },
            {
                week: 5,
                difficulty: "easy",
                topic: "Giant Oil Discoveries",
                question: "The giant oil discoveries application shows that large future productivity shocks lead to:",
                options: [
                    "CA deterioration (heavy investment + borrowing against future oil)",
                    "CA improvement",
                    "No CA effect",
                    "Balanced trade"
                ],
                correct: 0,
                explanation: "Oil discoveries (A₂ ↑): countries invest in infrastructure (I₁ ↑) and borrow against future revenue (S₁ ↓) → CA₁ deteriorates."
            },

            // HARD QUESTIONS START HERE"""

# Read the file
with open('index.html', 'r') as f:
    content = f.read()

# Find the insertion point (after "const questions = [")
insertion_point = content.find('        const questions = [')
if insertion_point == -1:
    print("Error: Could not find insertion point")
    exit(1)

# Find the end of that line
line_end = content.find('\n', insertion_point)
insertion_point = line_end + 1

# Insert the easy questions
new_content = content[:insertion_point] + easy_questions + content[insertion_point:]

# Write back
with open('index.html', 'w') as f:
    f.write(new_content)

print("Successfully added 50 easy questions (10 per week) to the quiz!")
