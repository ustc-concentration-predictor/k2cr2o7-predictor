# Potassium Dichromate Solutions: From Chemical Equilibrium to Color Prediction

## 1　Review of Fundamental Concepts

Many chemical reactions are **reversible**. For a reversible reaction under given conditions, when the forward and reverse reaction rates are equal and the concentrations of all components in the reaction mixture remain constant, the system is in a state of **chemical equilibrium**.

For a general reversible reaction:

$$
mA+nB \rightleftharpoons pC+qD
$$

The **reaction quotient** at any moment is:

$$
Q=\frac{c(\mathrm{C})^p\,c(\mathrm{D})^q}
        {c(\mathrm{A})^m\,c(\mathrm{B})^n}
$$

When the reaction reaches equilibrium at a given temperature, the quotient becomes a constant, $K$. This constant is the **chemical equilibrium constant**, and its value depends on temperature. If a factor affecting equilibrium is changed, the equilibrium shifts in the direction that tends to counteract that change. This is **Le Châtelier's principle**.

<p class="transition-note"><em>How can we perceive an equilibrium shift intuitively? How can we uncover the qualitative physicochemical mechanism behind Le Châtelier's principle? We will use potassium dichromate solution as our main example and explore chemical equilibrium through changes in color.</em></p>

## 2　Color-Change Reactions of Potassium Dichromate Solution

Two major reversible reactions coexist in potassium dichromate solution:

1. the dimerization equilibrium between hydrogen chromate and dichromate ions; and
2. <a class="annotation-term" href="#note-en-s2">the ionization equilibrium of hydrogen chromate ions</a>.

Their chemical equations are:

$$
\mathrm{Cr_2O_7^{2-}\ (orange)+H_2O
\rightleftharpoons 2HCrO_4^-}
$$

$$
\mathrm{HCrO_4^- \rightleftharpoons H^+ + CrO_4^{2-}\ (yellow)}
$$

Because dichromate is orange and chromate is yellow, changes in solution color reveal changes in the relative concentrations of these species and help us analyze equilibrium shifts.

<p class="transition-note"><em>We now know that two key equilibria exist in potassium dichromate solution and that quantitative analysis requires equilibrium constants. Yet even under isothermal conditions, concentration-based equilibrium constants can vary with solution composition. Why?</em></p>

## 3　The Concept of Activity

The concentration of a substance B is the amount of B per unit volume of the mixture. An equilibrium constant defined using concentrations is an **empirical equilibrium constant**. Its magnitude can be affected not only by temperature but also by ionic concentration. The familiar statement that “an equilibrium constant depends only on temperature” implicitly assumes an ideal dilute solution.

In real electrolyte solutions, complex electrostatic interactions occur between ions and between ions and solvent molecules. These interactions cause the <a class="annotation-term" href="#note-en-s3">thermodynamic</a> behavior of species to deviate from the ideal state. The higher the ionic concentration and charge, the larger this deviation can become. Activity corrects the concentration:

$$
a_\mathrm{B}=\gamma_\mathrm{B}\frac{c_\mathrm{B}}{c^\circ}
$$

Here, $a_\mathrm{B}$ is the **activity** of B (dimensionless), which can be understood as a corrected concentration; $\gamma_\mathrm{B}$ is the activity coefficient of B and is commonly less than 1; and $c^\circ$ is the standard concentration, usually $1\ \mathrm{mol\,L^{-1}}$.

The thermodynamic equilibrium constant obtained from activities is called the **activity constant**, or the **standard equilibrium constant** of the solution system. For

$$
mA+nB \rightleftharpoons pC+qD
$$

the activity constant is:

$$
K^\circ=\frac{a_\mathrm{C}^{p}a_\mathrm{D}^{q}}
{a_\mathrm{A}^{m}a_\mathrm{B}^{n}}
$$

This has the same form as the concentration constant $K$. Accurate calculations should use activities and the activity constant, but the calculation is more complicated. For dilute solutions, activity coefficients approach 1 and concentration-based calculations often have acceptable error, so they remain widely used.

<p class="transition-note"><em>The standard equilibrium constant derived from activity is an important tool for describing equilibrium. But if a reversible reaction has not yet reached equilibrium—for example, if it has just started or if a condition change has disturbed an existing equilibrium—how can we determine its direction and the extent required to reach equilibrium?</em></p>

## 4　Direction and Extent of Chemical Reactions

Comparing the reaction quotient $Q$ with the equilibrium constant $K$ determines the direction of a reaction. Furthermore, <a class="annotation-term" href="#note-en-s4">under given conditions</a>, comparing the Gibbs free-energy change per mole of reaction with zero tells us whether a reaction can proceed spontaneously. These perspectives are linked by the **reaction isotherm**:

$$
\Delta_\mathrm{r}G_\mathrm{m}
=\Delta_\mathrm{r}G_\mathrm{m}^{\circ}+RT\ln Q
$$

The subscript $\mathrm r$ denotes a chemical reaction, $\mathrm m$ means per mole of reaction, and $\Delta_\mathrm{r}G_\mathrm{m}^{\circ}$ is the standard molar Gibbs free-energy change, which serves as a thermodynamic reference point.

At equilibrium, $\Delta_\mathrm{r}G_\mathrm{m}=0$ and $Q=K^\circ$. Therefore:

$$
\Delta_\mathrm{r}G_\mathrm{m}
=RT\ln\!\left(\frac{Q}{K^\circ}\right)
$$

The comparison between $Q$ and $K^\circ$ is thus equivalent to the comparison between $\Delta_\mathrm{r}G_\mathrm{m}$ and zero:

- $Q<K^\circ,\ \Delta_\mathrm{r}G_\mathrm{m}<0$: the forward reaction is spontaneous;
- $Q=K^\circ,\ \Delta_\mathrm{r}G_\mathrm{m}=0$: the system is at equilibrium;
- $Q>K^\circ,\ \Delta_\mathrm{r}G_\mathrm{m}>0$: the reverse reaction is spontaneous.

<div class="thought-card">
  <div class="thought-title">Think 1</div>
  <p>If sufficient sodium hydroxide is added to an orange potassium dichromate solution, what color will the solution become?</p>
  <details>
    <summary>Show answer</summary>
    <div class="thought-answer">
      Sodium hydroxide lowers the H<sup>+</sup> concentration. The reaction quotient for HCrO<sub>4</sub><sup>−</sup> ⇌ H<sup>+</sup> + CrO<sub>4</sub><sup>2−</sup> decreases, shifting the equilibrium right and increasing yellow CrO<sub>4</sub><sup>2−</sup>. The decrease in HCrO<sub>4</sub><sup>−</sup> also shifts Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup> + H<sub>2</sub>O ⇌ 2HCrO<sub>4</sub><sup>−</sup> to the right, decreasing orange Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup>. The solution therefore shifts toward yellow.
    </div>
  </details>
</div>

<p class="transition-note"><em>As its name suggests, a reaction isotherm applies only at constant temperature. How, then, does temperature itself affect chemical equilibrium?</em></p>

## 5　Effect of Temperature on Chemical Equilibrium

According to Le Châtelier's principle, heating shifts an equilibrium toward the endothermic reaction, whereas cooling favors the exothermic direction. This qualitative relationship has a rigorous thermodynamic basis.

At constant pressure, the relationship between the standard equilibrium constant and temperature is:

$$
\frac{\mathrm{d}\ln K^\circ}{\mathrm{d}T}
=\frac{\Delta_\mathrm{r}H_\mathrm{m}^{\circ}}{RT^2}
$$

This is the <a class="annotation-term" href="#note-en-s5">differential form</a> of the van ’t Hoff equation. Here, $\Delta_\mathrm{r}H_\mathrm{m}^{\circ}$ is the standard molar reaction enthalpy change.

For an endothermic reaction, $\Delta_\mathrm{r}H_\mathrm{m}^{\circ}>0$, so $\mathrm{d}\ln K^\circ/\mathrm{d}T>0$: $K^\circ$ increases with temperature and heating favors the forward reaction. For an exothermic reaction, $\Delta_\mathrm{r}H_\mathrm{m}^{\circ}<0$, so the equilibrium constant decreases as temperature increases.

<div class="thought-card">
  <div class="thought-title">Think 2</div>
  <p>Both Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup> + H<sub>2</sub>O ⇌ 2HCrO<sub>4</sub><sup>−</sup> and HCrO<sub>4</sub><sup>−</sup> ⇌ H<sup>+</sup> + CrO<sub>4</sub><sup>2−</sup> are endothermic. How will cooling or heating a suitably concentrated potassium dichromate solution affect its color?</p>
  <details>
    <summary>Show answer</summary>
    <div class="thought-answer">
      Heating increases the equilibrium constants of both endothermic reactions and shifts them forward. Orange Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup> decreases while yellow CrO<sub>4</sub><sup>2−</sup> increases, so the solution becomes more yellow. Cooling has the opposite effect and deepens the orange color.
    </div>
  </details>
</div>

<p class="transition-note"><em>We have now reviewed equilibrium, the factors that affect it, and equilibrium shifts. Before applying these ideas to color-change experiments with potassium dichromate, we need to clarify the physical relationship between solution color and ionic composition.</em></p>

## 6　Solution Color and Ionic Composition

Different ions exhibit different colors: dichromate is orange, chromate is yellow, and hydrogen chromate is nearly colorless. Their electronic energy-level structures differ. When white light illuminates a solution, electrons absorb specific wavelengths and move from their ground state to excited states. The wavelength at which a substance absorbs most strongly is its **characteristic absorption wavelength**.

Dichromate primarily absorbs blue-violet light, leaving red and yellow components that appear orange. Chromate primarily absorbs blue-green light, leaving light that appears yellow. Hydrogen chromate absorbs mainly in the ultraviolet and contributes little visible absorption. Therefore, the observed color—or, more rigorously, the characteristic absorption wavelengths—can reveal the composition of colored ions.

Color depth also depends on the concentration of colored ions. Absorbance is defined as:

$$
A=\log_{10}\!\left(\frac{I_0}{I}\right)
$$

where $I_0$ is incident-light intensity and $I$ is transmitted-light intensity. According to the **Beer-Lambert law**:

$$
A=\varepsilon bc
$$

Here, $\varepsilon$ is molar absorptivity, $b$ is the optical path length, and $c$ is the concentration of the absorbing species. Absorbance is proportional to the concentration of a single absorbing species. When several absorbing species are present, total absorbance is the sum of their individual contributions.

For fixed incident light, the concentrations of chromium-containing ions in potassium dichromate solution directly determine its color. In simple cases, ion concentration and solution color can be mapped one-to-one, providing a basis for concentration prediction.

<div class="thought-card">
  <div class="thought-title">Think 3</div>
  <p>A potassium dichromate solution with a Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup> concentration of <em>c</em> has absorbance <em>A</em>. If it is diluted twofold and measured under the same conditions, must its absorbance equal <em>A</em>/2?</p>
  <details>
    <summary>Show answer</summary>
    <div class="thought-answer">
      Not necessarily. In the Beer-Lambert law, “concentration” means the actual equilibrium concentration of a single absorbing species, not the prepared total concentration. Dilution shifts Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup> + H<sub>2</sub>O ⇌ 2HCrO<sub>4</sub><sup>−</sup> toward the side with more ions, while HCrO<sub>4</sub><sup>−</sup> ⇌ H<sup>+</sup> + CrO<sub>4</sub><sup>2−</sup> also shifts. Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup> falls below the simple <em>c</em>/2 value, and the newly formed species contribute differently to absorbance. Total absorbance is therefore not linearly related to total chromium concentration; it is <a class="annotation-term" href="#note-en-s6">governed by the interplay of the two coupled equilibria</a>.
    </div>
  </details>
</div>

<p class="transition-note"><em>We have explained the microscopic origin of color and established the quantitative relationship between color depth and concentration. In principle, knowing a solution's color lets us infer component concentrations—provided that the color-to-concentration relationship can be established accurately.</em></p>

<p class="transition-note"><em>Traditionally, a spectrophotometer performs this task. It is precise, but expensive and relatively complex to operate, which limits rapid or on-site testing. In a system with several colored ions, the Beer-Lambert law is also not straightforward to apply directly.</em></p>

<p class="transition-note"><em>Could we photograph the solution with a phone and let a computer bypass absorbance, predicting each component directly from color? Machine learning can learn the relationship between color and concentration from data, making this idea practical.</em></p>

<p class="transition-note"><em>This concludes the knowledge section. Next, pick up a camera and explore the colorful chemistry of potassium dichromate equilibrium.</em></p>

<div id="note-en-s2" class="annotation-modal">
  <div class="annotation-dialog">
    <a href="#" class="annotation-close" aria-label="Close">×</a>
    <h4>Ionization equilibrium of hydrogen chromate</h4>
    <p>The reaction HCrO<sub>4</sub><sup>−</sup> + H<sup>+</sup> ⇌ H<sub>2</sub>CrO<sub>4</sub> also exists in principle. Chromic acid, H<sub>2</sub>CrO<sub>4</sub>, is a moderately strong acid with two ionization steps. Because the first ionization constant K<sub>a1</sub> is much larger than K<sub>a2</sub>, molecular chromic acid generally needs to be considered only under extremely acidic conditions.</p>
  </div>
</div>

<div id="note-en-s3" class="annotation-modal">
  <div class="annotation-dialog">
    <a href="#" class="annotation-close" aria-label="Close">×</a>
    <h4>Thermodynamics</h4>
    <p>Thermodynamics studies thermal phenomena in macroscopic systems, transformations between heat and other forms of energy, and the changes in related physical quantities. Chemical equilibrium, enthalpy, and entropy all fall within its scope.</p>
  </div>
</div>

<div id="note-en-s4" class="annotation-modal">
  <div class="annotation-dialog">
    <a href="#" class="annotation-close" aria-label="Close">×</a>
    <h4>Under given conditions</h4>
    <p>The conditions are constant temperature, constant pressure, and zero non-expansion work. These are normally assumed for open-beaker reactions discussed in high-school chemistry.</p>
  </div>
</div>

<div id="note-en-s5" class="annotation-modal">
  <div class="annotation-dialog">
    <a href="#" class="annotation-close" aria-label="Close">×</a>
    <h4>Differential form of the van ’t Hoff equation</h4>
    <p>Over a sufficiently small temperature range, Δ<sub>r</sub>H<sub>m</sub><sup>°</sup> can be treated as temperature-independent, yielding:</p>
    <p><em>ln(K<sub>2</sub><sup>°</sup>/K<sub>1</sub><sup>°</sup>) = (Δ<sub>r</sub>H<sub>m</sub><sup>°</sup>/R)(1/T<sub>1</sub> − 1/T<sub>2</sub>)</em></p>
    <p>For an endothermic reaction, heating gives T<sub>2</sub> &gt; T<sub>1</sub>, so the right-hand side is positive and K<sub>2</sub><sup>°</sup> &gt; K<sub>1</sub><sup>°</sup>.</p>
  </div>
</div>

<div id="note-en-s6" class="annotation-modal">
  <div class="annotation-dialog">
    <a href="#" class="annotation-close" aria-label="Close">×</a>
    <h4>Interplay of two coupled equilibria</h4>
    <p>To apply the Beer-Lambert law to the concentrations of individual components, total absorbance must be measured at several wavelengths. Because total absorbance is the sum of the individual species contributions, the component concentrations can then be obtained by solving a system of linear equations.</p>
  </div>
</div>
