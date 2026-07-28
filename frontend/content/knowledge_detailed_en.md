## 1　Review of Fundamental Concepts

As learned in the course, many chemical reactions are reversible. For a reversible reaction under given conditions, when the rates of the forward and reverse reactions are equal, and the concentrations of all components in the reaction mixture remain constant, the system is in a state of chemical equilibrium.

For a general reversible reaction:

$$
mA+nB\rightleftharpoons pC+qD
$$

The reaction quotient at any moment is defined as

$$
Q=\frac{c(\mathrm{C})^p\cdot c(\mathrm{D})^q}
        {c(\mathrm{A})^m\cdot c(\mathrm{B})^n}
$$

. When this reaction reaches chemical equilibrium at a given temperature, this reaction quotient becomes a constant value, denoted as

$$
\left[
\frac{c(\mathrm{C})^p\cdot c(\mathrm{D})^q}
     {c(\mathrm{A})^m\cdot c(\mathrm{B})^n}
\right]_{\mathrm e}=K
$$

(the subscript 'e' indicates that the reaction system has reached chemical equilibrium). This constant $K$ is termed the chemical equilibrium constant, and its numerical value depends on the temperature. If a factor affecting the equilibrium is changed, the equilibrium will shift in a direction that tends to counteract this change. This is known as Le Châtelier's principle, i.e., the principle of chemical equilibrium shift.

<p class="transition-note"><em>How can we intuitively perceive the shift in chemical equilibrium? How can we uncover the qualitative physicochemical mechanisms behind Le Châtelier's principle? Below, we will use a potassium dichromate solution as a primary example to explore the fascinating chemistry of equilibrium through changes in color.</em></p>

## 2　The Color Change Reactions of Potassium Dichromate Solution

In a potassium dichromate solution, two major reversible reactions coexist: 1. The dimerization equilibrium between hydrogen chromate and dichromate ions; and 2. <a class="annotation-term" href="#note-en-s2">The ionization equilibrium of hydrogen chromate ions</a>*. Their chemical equations are:

$$
\underset{\text{Dichromate}}{\color{#E87500}{\mathrm{Cr_2O_7^{2-}\ (orange)}}}
+\underset{\text{Water}}{\mathrm{H_2O}}
\rightleftharpoons
2\underset{\text{Hydrogen chromate}}{\mathrm{HCrO_4^-}}
$$

$$
\underset{\text{Hydrogen chromate}}{\mathrm{HCrO_4^-}}
\rightleftharpoons
\underset{\text{Hydrogen ion}}{\mathrm{H^+}}+
\underset{\text{Chromate}}{\color{#D4A000}{\mathrm{CrO_4^{2-}\ (yellow)}}}
$$

Since the dichromate ion appears orange and the chromate ion appears yellow, we can monitor the shifts in chemical equilibrium by observing changes in the solution's color, which reflect the relative concentrations of the species involved.

<p class="transition-note"><em>We have now learned that there are two key equilibrium reactions in potassium dichromate solution, and their quantitative analysis cannot be done without the use of equilibrium constants. However, in reality, even under isothermal conditions, the equilibrium constants we defined earlier can change with the composition of the solution. Why is that?</em></p>

## 3　The Concept of Activity

We know that the "concentration $c_\mathrm{B}$" of a substance B refers to the amount of substance of B per unit volume of the mixture. The equilibrium constant defined using concentrations in high school textbooks is termed the empirical equilibrium constant. The magnitude of an empirical equilibrium constant is influenced not only by temperature but also by ionic concentration. The statement we often use in high school chemistry—that "the magnitude of the equilibrium constant depends only on temperature"—implicitly assumes that the reaction system behaves as an ideal dilute solution. However, in real electrolyte solutions, complex electrostatic interactions exist between ions, as well as between ions and solvent (water) molecules. These interactions cause the <a class="annotation-term" href="#note-en-s3">thermodynamic</a>* behavior of species in the actual solution to deviate from the ideal state. The higher the ionic concentration and the greater the charge number, the more severe the deviation. To account for these effects, a correction must be applied to the ionic concentration:

$$
a_\mathrm{B}=\gamma_\mathrm{B}\frac{c_\mathrm{B}}{c^\Theta}
$$

Here, $a_\mathrm{B}$ is the activity of B (a dimensionless quantity), which can be understood as a corrected concentration; $\gamma_\mathrm{B}$ is the activity coefficient of B, typically less than unity; and $c^\Theta$ is the standard concentration, usually taken as $1\ \mathrm{mol/L}$. The thermodynamic equilibrium constant derived from activities is called the activity constant $K^\Theta$, which is the standard equilibrium constant for the solution system. For the reaction

$$
mA+nB\rightleftharpoons pC+qD
$$

, the expression for the activity constant is:

$$
K^\Theta=
\left[
\frac{a_\mathrm{C}^p\cdot a_\mathrm{D}^q}
     {a_\mathrm{A}^m\cdot a_\mathrm{B}^n}
\right]_{\mathrm e}
$$

This expression is analogous in form to the concentration constant $K$. Accurate calculations should employ activities and the activity constant, but these are more complex. Using concentrations and concentration constants is considerably simpler, and for dilute solutions, the error is often negligible (as activity coefficients approach unity at low ionic concentrations). Therefore, this simpler approach remains widely used.

<p class="transition-note"><em>The standard equilibrium constant derived from activity is an important tool for describing equilibrium, but if a reversible reaction has not yet reached equilibrium (for example, if the reaction has just started or if conditions have been changed to break an existing equilibrium), how can we determine the direction—forward or reverse—in which the reaction will proceed? And to what extent must the reaction proceed before equilibrium is reached?</em></p>

## 4　The Direction and Extent of Chemical Reactions

High school textbooks teach us that by comparing the reaction quotient $Q$ with the equilibrium constant $K$, we can determine the direction of a chemical reaction. Furthermore, <a class="annotation-term" href="#note-en-s4">under given conditions</a>*, comparing the Gibbs free energy change per mole of reaction, $\Delta G$, with zero allows us to judge whether a reaction can occur spontaneously. These two perspectives are connected thermodynamically through the van 't Hoff reaction isotherm.

According to the reaction isotherm:

$$
\Delta_\mathrm rG_\mathrm m
=\Delta_\mathrm rG_\mathrm m^\Theta+RT\ln Q
$$

Here, the subscript 'r' denotes a chemical reaction, 'm' indicates per mole of reaction, and $\Delta_\mathrm rG_\mathrm m^\Theta$ is the standard molar Gibbs free energy change of the reaction, which can be regarded as a thermodynamic "reference point." When $\Delta_\mathrm rG_\mathrm m=0$, the chemical reaction has reached equilibrium. At this point, the reaction quotient $Q$ is the standard equilibrium constant $K^\Theta$, so

$$
\Delta_\mathrm rG_\mathrm m^\Theta+RT\ln K^\Theta=0
$$

. Substituting this into the reaction isotherm yields:

$$
\Delta_\mathrm rG_\mathrm m=RT\ln\frac{Q}{K^\Theta}
$$

From this, it becomes clear that the comparison between $Q$ and $K^\Theta$ is equivalent to the comparison between $\Delta_\mathrm rG_\mathrm m$ and zero when judging the direction of a chemical reaction. Therefore:

$$
\text{If }Q<K^\Theta,\text{ then }\Delta G<0:
\text{ the forward reaction is spontaneous.}
$$

$$
\text{If }Q=K^\Theta,\text{ then }\Delta G=0:
\text{ the reaction is at equilibrium, i.e., it has reached its maximum extent.}
$$

$$
\text{If }Q>K^\Theta,\text{ then }\Delta G>0:
\text{ the reverse reaction is spontaneous.}
$$

<div class="thought-card">
  <div class="thought-title">Think 1:</div>
  <p>If sufficient sodium hydroxide is added to an orange potassium dichromate solution, what color will the solution turn?</p>
  <details>
    <summary><span class="answer-show">Show answer</span><span class="answer-hide">Hide answer</span></summary>
    <div class="thought-answer">
      The addition of sodium hydroxide reduces the concentration of hydrogen ions in the system. This causes the reaction quotient Q for the equilibrium HCrO<sub>4</sub><sup>−</sup> ⇌ H<sup>+</sup> + CrO<sub>4</sub><sup>2−</sup> to decrease, shifting the equilibrium to the right. This increases the concentration of CrO<sub>4</sub><sup>2−</sup> and decreases that of HCrO<sub>4</sub><sup>−</sup>. Simultaneously, the decrease in HCrO<sub>4</sub><sup>−</sup> concentration also reduces the reaction quotient for the equilibrium Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup> + H<sub>2</sub>O ⇌ 2HCrO<sub>4</sub><sup>−</sup>, shifting it to the right and reducing the concentration of Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup>. Consequently, the concentration of yellow CrO<sub>4</sub><sup>2−</sup> increases while that of orange Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup> decreases, causing the system's color to shift towards yellow.
    </div>
  </details>
</div>

<p class="transition-note"><em>As the name suggests, the van 't Hoff reaction isotherm applies only when the temperature is constant. So how does temperature itself affect chemical equilibrium?</em></p>

## 5　The Effect of Temperature on Chemical Equilibrium

As we know from Le Châtelier's principle, increasing temperature shifts chemical equilibrium in the direction of the endothermic reaction, while decreasing temperature favors the exothermic direction. This qualitative relationship is also underpinned by rigorous thermodynamic principles. At constant pressure, when the system temperature changes from $T$ to $T+\Delta T$ (where $\Delta T$ is infinitesimally small), the relationship between the standard equilibrium constant $K^\Theta$ and the temperature change $\Delta T$ is given by:

$$
\frac{\Delta\ln K^\Theta}{\Delta T}
=\frac{\Delta_\mathrm rH_\mathrm m^\Theta}{RT^2}
$$

This equation is the <a class="annotation-term" href="#note-en-s5">differential form</a>* of the van 't Hoff equation in chemical equilibrium, where $\Delta_\mathrm rH_\mathrm m^\Theta$ is the standard molar reaction enthalpy change (with all species in their standard states). It is evident that for an endothermic reaction, $\Delta_\mathrm rH_\mathrm m^\Theta>0$, and $\Delta\ln K^\Theta/\Delta T>0$, meaning $K^\Theta$ increases with temperature, favoring the forward reaction. For an exothermic reaction, $\Delta_\mathrm rH_\mathrm m^\Theta<0$, and $\Delta\ln K^\Theta/\Delta T<0$, so $K^\Theta$ decreases with temperature, which is unfavorable for the forward reaction.

<div class="thought-card">
  <div class="thought-title">Think 2:</div>
  <p>Given that the reactions Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup> + H<sub>2</sub>O ⇌ 2HCrO<sub>4</sub><sup>−</sup> and HCrO<sub>4</sub><sup>−</sup> ⇌ H<sup>+</sup> + CrO<sub>4</sub><sup>2−</sup> are both endothermic, how would the color of a suitably concentrated potassium dichromate solution change upon cooling or heating?</p>
  <details>
    <summary><span class="answer-show">Show answer</span><span class="answer-hide">Hide answer</span></summary>
    <div class="thought-answer">
      For an endothermic reaction, Δ<sub>r</sub>H<sub>m</sub><sup>Θ</sup>&gt;0. Raising the temperature increases K<sup>Θ</sup>. Since Q&lt;K<sup>Θ</sup>, both reactions shift spontaneously in the forward direction. This leads to a decrease in the concentration of orange Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup> and an increase in yellow CrO<sub>4</sub><sup>2−</sup>, making the solution appear more yellow. Conversely, cooling would deepen the orange color of the solution.
    </div>
  </details>
</div>

<p class="transition-note"><em>At this point, you have learned about reaction equilibrium, the factors that affect it, and how equilibrium shifts. Before we apply this knowledge to experiments on the color changes of potassium dichromate solutions, we first need to clarify the specific physical relationship between the color of a solution and its ionic composition.</em></p>

## 6　Solution Color and Ionic Composition

First, different ions exhibit different colors—for example, dichromate appears orange, chromate appears yellow, and hydrogen chromate is almost colorless. Why is this the case? This arises from their distinct internal electronic energy level structures. When white light (containing all colors) shines on the solution, electrons within the ions absorb light of specific wavelengths, transitioning from their ground state to an excited state. A given substance exhibits maximum absorption of photons at a specific wavelength, known as its characteristic absorption wavelength. The dichromate ion primarily absorbs blue-violet light; the remaining transmitted light, composed of red and yellow components, mixes to appear orange. The chromate ion mainly absorbs blue-green light, leaving red-orange light, which appears yellow. The hydrogen chromate ion, however, absorbs primarily in the ultraviolet region, which is invisible to the human eye. Therefore, it shows almost no absorption in the visible spectrum and appears nearly colorless to the naked eye. Hence, by analyzing the type of color exhibited by a solution—more rigorously, by the characteristic wavelengths of light it absorbs—we can infer the composition of colored ions present.

Second, the depth of a solution's color is related to the concentration of colored ions. As a general rule, a higher concentration of colored ions results in a deeper color. This intuitive conclusion is also supported by a physical law. To quantify the depth of color, we use absorbance $A$ to describe how much light the solution has "blocked": $A=\log(I_0/I)$, where $I_0$ is the intensity of the incident light and $I$ is the intensity of the transmitted light. According to the Beer-Lambert law:

$$
A=\varepsilon bc
$$

Here, $\varepsilon$ is the molar absorptivity (an intrinsic property of the absorbing substance, which also depends on the wavelength of incident light, the solvent, and temperature), $b$ is the path length (the actual distance light travels through the solution), and $c$ is the concentration of the absorbing substance. The Beer-Lambert law tells us that absorbance $A$ is directly proportional to the concentration $c$ of the absorbing species. When multiple absorbing species are present in a solution, the total absorbance is the sum of the absorbances of the individual species.

Therefore, for a given incident light, the concentration of the various chromium-containing ions in a potassium dichromate solution directly determines the color of the solution. In some simpler cases, the concentration of chromium-containing ions can be correlated one-to-one with the solution color, offering a feasible approach for predicting ion concentrations in the system.

<div class="thought-card">
  <div class="thought-title">Think 3:</div>
  <p>A potassium dichromate solution with a Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup> concentration of c has an absorbance A. If this solution is diluted twofold and measured under the same conditions, will the absorbance be exactly A/2?</p>
  <details>
    <summary><span class="answer-show">Show answer</span><span class="answer-hide">Hide answer</span></summary>
    <div class="thought-answer">
      Not necessarily. The Beer-Lambert law, which states a direct proportionality between absorbance and concentration, applies strictly to a single absorbing species. The "concentration" in this context refers to the actual equilibrium concentration of that absorbing species, not the total concentration prepared. When a potassium dichromate solution is diluted, the total ion concentration of the system decreases. For the equilibrium Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup> + H<sub>2</sub>O ⇌ 2HCrO<sub>4</sub><sup>−</sup>, Le Châtelier's principle dictates that the equilibrium shifts to the side with more ions, i.e., to the right (the reaction HCrO<sub>4</sub><sup>−</sup> ⇌ H<sup>+</sup> + CrO<sub>4</sub><sup>2−</sup> also shifts rightward concurrently). On the one hand, the concentration of Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup> decreases further from the simple c/2 value. On the other hand, the contributions to absorbance from the generated HCrO<sub>4</sub><sup>−</sup> and CrO<sub>4</sub><sup>2−</sup> are often different from that of Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup>. Consequently, the measured total absorbance of the solution is not linearly related to the total chromium concentration; rather, it is <a class="annotation-term" href="#note-en-s6">governed by the interplay of the two coupled equilibria</a>.*
    </div>
  </details>
</div>

<div class="transition-note">
  <p><em>Above, we have explained the physical origin of color at the microscopic level (characteristic absorption wavelengths) and established the quantitative relationship between color depth and concentration (the Beer-Lambert law). Therefore, in theory, as long as we know the color of a solution, we can deduce the concentrations of its components—provided that we can accurately establish the correspondence between "color" and "concentration."</em></p>
  <p><em>Traditionally, this work is done with a spectrophotometer: it precisely measures the absorbance at specific wavelengths and then calculates the concentration using the Beer-Lambert law. However, spectrophotometers are expensive and relatively complicated to operate, making them inconvenient for on-site or rapid testing. At the same time, Thought Question 3 also tells us that for systems like potassium dichromate solutions, which contain multiple colored ionic species, applying the Beer-Lambert law is not straightforward.</em></p>
  <p><em>At this point, you might be thinking: can we just take a photo of the solution with our phone and let a computer skip the "absorbance" step and directly tell us the concentrations of each component from the color? In recent years, the development of machine learning has turned this idea into reality. Machine learning can learn the correspondence between color and concentration from large amounts of data, without needing to know physical quantities such as absorbance or molar absorptivity. We can easily analyze the ion concentrations in potassium dichromate solutions without even stepping into a lab!</em></p>
  <p><em>This brings us to the end of the knowledge section. Next, we can pick up our cameras and explore the colorful chemistry of potassium dichromate solutions in equilibrium! Are you ready?</em></p>
</div>

<div id="note-en-s2" class="annotation-modal">
  <div class="annotation-dialog">
    <a href="#" class="annotation-close" aria-label="Close">×</a>
    <h4>The ionization equilibrium of hydrogen chromate ions</h4>
    <p>Theoretically, the reaction HCrO<sub>4</sub><sup>−</sup> + H<sup>+</sup> ⇌ H<sub>2</sub>CrO<sub>4</sub> also exists. Chromic acid (H<sub>2</sub>CrO<sub>4</sub>) is a moderately strong acid with two steps of ionization in solution. However, because the ionization constant of the first step (K<sub>a1</sub>) is much greater than that of the second step (K<sub>a2</sub>), the presence of the chromic acid molecule is only considered under extremely acidic conditions.</p>
  </div>
</div>

<div id="note-en-s3" class="annotation-modal">
  <div class="annotation-dialog">
    <a href="#" class="annotation-close" aria-label="Close">×</a>
    <h4>Thermodynamic</h4>
    <p>Thermodynamics studies the thermal phenomena of macroscopic systems, the conversion between heat and other forms of energy, and the changes in related physical quantities that accompany these transformations. Chemical equilibrium, enthalpy, entropy, etc., all fall within the scope of thermodynamics.</p>
  </div>
</div>

<div id="note-en-s4" class="annotation-modal">
  <div class="annotation-dialog">
    <a href="#" class="annotation-close" aria-label="Close">×</a>
    <h4>Under given conditions</h4>
    <p>These conditions refer to constant temperature, constant pressure, and zero non-expansion work. These conditions are typically satisfied by default for reactions in open beakers, as discussed in high school chemistry.</p>
  </div>
</div>

<div id="note-en-s5" class="annotation-modal">
  <div class="annotation-dialog">
    <a href="#" class="annotation-close" aria-label="Close">×</a>
    <h4>Differential form</h4>
    <p>For relatively small temperature ranges, Δ<sub>r</sub>H<sub>m</sub><sup>Θ</sup> can be approximated as a temperature-independent constant, leading to the integrated form of the van 't Hoff equation:</p>
    <p><em>ln(K<sup>Θ</sup><sub>T2</sub>/K<sup>Θ</sup><sub>T1</sub>) = (Δ<sub>r</sub>H<sub>m</sub><sup>Θ</sup>/R)(1/T<sub>1</sub> − 1/T<sub>2</sub>)</em></p>
    <p>This equation also provides a basis for understanding the effect of temperature on the equilibrium constant. For an endothermic reaction, Δ<sub>r</sub>H<sub>m</sub><sup>Θ</sup>&gt;0; when the temperature increases (T<sub>2</sub>&gt;T<sub>1</sub>), the right-hand side of the equation is positive, hence K<sup>Θ</sup><sub>T2</sub>&gt;K<sup>Θ</sup><sub>T1</sub>, indicating an increase in the equilibrium constant.</p>
  </div>
</div>

<div id="note-en-s6" class="annotation-modal">
  <div class="annotation-dialog">
    <a href="#" class="annotation-close" aria-label="Close">×</a>
    <h4>Governed by the interplay of the two coupled equilibria</h4>
    <p>If we want to use the Beer-Lambert law to analyze the concentrations of various components in the solution, we need to measure the total absorbance at different wavelengths (the total absorbance is the sum of the absorbances of each individual species), and then solve a system of linear equations.</p>
  </div>
</div>
