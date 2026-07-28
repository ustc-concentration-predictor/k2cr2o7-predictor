# 重铬酸钾平衡与颜色预测

## 1. 化学平衡

许多化学反应都是可逆反应。在一定条件下，可逆反应的正、逆反应速率相等，反应混合物中各组分的浓度在宏观上保持不变，此时体系达到化学平衡。

对于一般反应：

$$
mA+nB \rightleftharpoons pC+qD
$$

反应的浓度商 $Q$ 为：

$$
Q=\frac{c(\mathrm{C})^p\,c(\mathrm{D})^q}
        {c(\mathrm{A})^m\,c(\mathrm{B})^n}
$$

平衡时，$Q$ 等于平衡常数 $K$。当外界因素发生改变时，平衡会向着减弱该变化的方向移动，这就是勒夏特列原理。

## 2. K₂Cr₂O₇ 溶液的颜色变化

重铬酸钾溶液中最重要的铬(VI)平衡包括：

$$
\mathrm{Cr_2O_7^{2-}+H_2O \rightleftharpoons 2HCrO_4^-}
$$

$$
\mathrm{HCrO_4^- \rightleftharpoons H^+ + CrO_4^{2-}}
$$

$\mathrm{Cr_2O_7^{2-}}$ 呈橙色，$\mathrm{CrO_4^{2-}}$ 呈黄色，$\mathrm{HCrO_4^-}$ 在可见光区颜色较弱。因此，溶液颜色能够反映这些铬物种的相对分布。

加入氢氧化物后，$[\mathrm{H^+}]$ 降低，第二个平衡向 $\mathrm{CrO_4^{2-}}$ 方向移动，第一个平衡也会向 $\mathrm{HCrO_4^-}$ 方向移动，溶液整体变得更黄。

## 3. 活度与浓度

在理想稀溶液中，可以直接用浓度进行平衡计算。实际电解质溶液中，离子-离子和离子-溶剂相互作用会使体系偏离理想状态，离子强度越高或离子电荷越大，这种偏离通常越明显。

活度可表示为：

$$
a_\mathrm{B}=\gamma_\mathrm{B}\frac{c_\mathrm{B}}{c^\circ}
$$

其中，$a_\mathrm{B}$ 是活度，$\gamma_\mathrm{B}$ 是活度系数，$c^\circ$ 是标准浓度，通常为 $1\ \mathrm{mol\,L^{-1}}$。严格的热力学平衡常数应使用活度，但对于稀溶液，采用浓度常数通常也能得到可接受的近似。

## 4. 反应方向与吉布斯自由能

反应方向既可以通过比较 $Q$ 与 $K$ 判断，也可以通过摩尔反应吉布斯自由能变化判断：

$$
\Delta_\mathrm{r}G=RT\ln\!\left(\frac{Q}{K}\right)
$$

- $Q<K$：正反应方向有利；
- $Q=K$：体系处于平衡；
- $Q>K$：逆反应方向有利。

这将高中阶段的平衡移动描述与热力学驱动力联系起来。

## 5. 温度效应

温度变化会影响平衡常数。范特霍夫关系为：

$$
\frac{\mathrm{d}\ln K}{\mathrm{d}T}
=\frac{\Delta_\mathrm{r}H^\circ}{RT^2}
$$

对于吸热反应，升温使 $K$ 增大，有利于正反应；对于放热反应，升温使 $K$ 减小，不利于正反应。

如果将重铬酸根/铬酸根相关平衡视为吸热反应，升温会使体系中黄色的 $\mathrm{CrO_4^{2-}}$ 比例提高，而降温会使橙色加深。

## 6. 颜色与铬物种浓度

不同铬物种具有不同的电子结构，因此吸收不同波长的光：

- $\mathrm{Cr_2O_7^{2-}}$ 主要吸收蓝紫光，所以溶液呈橙色；
- $\mathrm{CrO_4^{2-}}$ 主要吸收蓝绿光，所以溶液呈黄色；
- $\mathrm{HCrO_4^-}$ 的强吸收更靠近紫外区，对可见颜色的贡献较小。

根据朗伯-比尔定律：

$$
A=\varepsilon bc
$$

$A$ 是吸光度，$\varepsilon$ 是摩尔吸光系数，$b$ 是光程，$c$ 是吸光物种浓度。存在多种吸光物种时，总吸光度近似为各物种贡献之和：

$$
A_{\mathrm{total}}=\sum_i \varepsilon_i b c_i
$$

因此，当前模型将图像颜色特征与 pH 和化学平衡计算相结合，用于预测可见铬物种的浓度。

## 7. 为什么总 Cr(VI) 不一定是最佳直接预测目标

配制的总铬(VI)浓度并不是测得颜色的直接原因。颜色由 $\mathrm{Cr_2O_7^{2-}}$、$\mathrm{HCrO_4^-}$ 和 $\mathrm{CrO_4^{2-}}$ 的平衡浓度共同控制；稀释或改变 pH 会同时改变总浓度和物种分布。

当前预测流程为：

$$
\begin{aligned}
\text{图像}+\mathrm{pH}
&\longrightarrow \text{光照标准化}\\
&\longrightarrow \text{颜色特征提取}\\
&\longrightarrow \text{预测 }\mathrm{HCrO_4^-}\text{ 和 }\mathrm{Cr_2O_7^{2-}}\\
&\longrightarrow \text{利用 }K_{a,2}\text{ 计算 }\mathrm{CrO_4^{2-}}\\
&\longrightarrow \text{估算总 Cr(VI)}
\end{aligned}
$$

这一流程更符合可见颜色背后的化学机理。
