# Potassium dichromate equilibrium and color prediction

## 1. Chemical equilibrium

Many chemical reactions are reversible. Under fixed conditions, a reversible reaction reaches chemical equilibrium when the forward and reverse reaction rates become equal and the concentrations of each component remain macroscopically constant.

For a general reaction:

$$
mA+nB \rightleftharpoons pC+qD
$$

the reaction quotient, $Q$, is:

$$
Q=\frac{c(\mathrm{C})^p\,c(\mathrm{D})^q}
        {c(\mathrm{A})^m\,c(\mathrm{B})^n}
$$

At equilibrium, $Q$ becomes the equilibrium constant, $K$. If an external factor changes the system, the equilibrium shifts in the direction that reduces the effect of that change. This is Le Chatelier's principle.

## 2. Color change of K₂Cr₂O₇ solution

In potassium dichromate solution, the most important chromium(VI) equilibria are:

$$
\mathrm{Cr_2O_7^{2-}+H_2O \rightleftharpoons 2HCrO_4^-}
$$

$$
\mathrm{HCrO_4^- \rightleftharpoons H^+ + CrO_4^{2-}}
$$

$\mathrm{Cr_2O_7^{2-}}$ is orange, $\mathrm{CrO_4^{2-}}$ is yellow, and $\mathrm{HCrO_4^-}$ is weakly colored in the visible range. Therefore, solution color reflects the relative distribution of these chromium species.

When hydroxide is added, $[\mathrm{H^+}]$ decreases. The second equilibrium shifts toward $\mathrm{CrO_4^{2-}}$, and the first equilibrium also shifts toward $\mathrm{HCrO_4^-}$. The visible result is that the solution becomes more yellow.

## 3. Activity and concentration

In ideal dilute solutions, concentration can be used directly in equilibrium calculations. In real electrolyte solutions, ion-ion and ion-solvent interactions cause deviations from ideal behavior, especially at higher ionic strength or for highly charged ions.

To describe this, concentration is corrected into activity:

$$
a_\mathrm{B}=\gamma_\mathrm{B}\frac{c_\mathrm{B}}{c^\circ}
$$

where $a_\mathrm{B}$ is activity, $\gamma_\mathrm{B}$ is the activity coefficient, and $c^\circ$ is the standard concentration, usually $1\ \mathrm{mol\,L^{-1}}$. Strict thermodynamic equilibrium constants should use activities, but concentration-based constants are often acceptable for dilute solutions.

## 4. Reaction direction and Gibbs free energy

The direction of a reaction can be judged by comparing $Q$ and $K$. It can also be judged thermodynamically by the molar Gibbs free-energy change:

$$
\Delta_\mathrm{r}G=RT\ln\!\left(\frac{Q}{K}\right)
$$

Therefore:

- $Q<K$: the forward reaction is favored.
- $Q=K$: the system is at equilibrium.
- $Q>K$: the reverse reaction is favored.

This connects the high-school description of equilibrium movement with thermodynamic driving force.

## 5. Temperature effect

Temperature changes affect equilibrium constants. The van't Hoff relation describes the relationship between temperature and $K$:

$$
\frac{\mathrm{d}\ln K}{\mathrm{d}T}
=\frac{\Delta_\mathrm{r}H^\circ}{RT^2}
$$

For an endothermic reaction, increasing temperature increases $K$ and favors the forward reaction. For an exothermic reaction, increasing temperature decreases $K$ and disfavors the forward reaction.

For dichromate/chromate equilibria, if the relevant reactions are treated as endothermic, heating shifts the system toward more yellow $\mathrm{CrO_4^{2-}}$, while cooling makes the orange color deeper.

## 6. Color and chromium species concentration

Different chromium species have different electronic structures, so they absorb different wavelengths of light:

- $\mathrm{Cr_2O_7^{2-}}$ mainly absorbs blue-violet light, so the solution appears orange.
- $\mathrm{CrO_4^{2-}}$ mainly absorbs blue-green light, so the solution appears yellow.
- $\mathrm{HCrO_4^-}$ absorbs strongly toward the ultraviolet region and contributes less visible color.

The color depth is related to absorbing-species concentration. According to the Lambert-Beer law:

$$
A=\varepsilon bc
$$

$A$ is absorbance, $\varepsilon$ is molar absorptivity, $b$ is optical path length, and $c$ is the absorbing-species concentration. With multiple absorbing species, total absorbance is approximately the sum of the absorbance contributions from each species:

$$
A_{\mathrm{total}}=\sum_i \varepsilon_i b c_i
$$

This is why the current model predicts the visible-ion system by combining image color features with pH and equilibrium calculations.

## 7. Why total Cr(VI) is not always the best direct target

The prepared total chromium(VI) concentration is not the direct cause of the measured color. The color is controlled by the equilibrium concentrations of $\mathrm{Cr_2O_7^{2-}}$, $\mathrm{HCrO_4^-}$, and $\mathrm{CrO_4^{2-}}$. Diluting or changing pH changes both total concentration and species distribution.

Therefore, the deployed route is:

$$
\begin{aligned}
\text{image}+\mathrm{pH}
&\longrightarrow \text{illumination standardization}\\
&\longrightarrow \text{color-feature extraction}\\
&\longrightarrow \text{prediction of }\mathrm{HCrO_4^-}\text{ and }\mathrm{Cr_2O_7^{2-}}\\
&\longrightarrow \text{calculation of }\mathrm{CrO_4^{2-}}\text{ using }K_{a,2}\\
&\longrightarrow \text{estimated total Cr(VI)}
\end{aligned}
$$

This route better matches the chemistry behind the visible color.
