# 重铬酸钾溶液：从化学平衡到颜色预测

## 1　知识回顾

通过课程学习我们知道，很多化学反应是**可逆**的。在一定条件下的可逆反应，正反应和逆反应的速率相等，反应混合物中各组分的浓度保持不变的状态即为**化学平衡状态**。

对于一般的可逆反应：

$$
mA+nB \rightleftharpoons pC+qD
$$

任意时刻的**浓度商**为：

$$
Q=\frac{c(\mathrm{C})^p\,c(\mathrm{D})^q}
        {c(\mathrm{A})^m\,c(\mathrm{B})^n}
$$

该反应在一定温度下达到化学平衡后，浓度商为定值，记作 $K$。常数 $K$ 称为**化学平衡常数**，其数值大小与温度有关。如果改变影响平衡的一个因素，平衡就向着能够减弱这种改变的方向移动，这就是**勒夏特列原理**，即化学平衡移动原理。

<p class="transition-note"><em>如何直观感受化学平衡的移动？如何揭示勒夏特列原理背后的定性物理化学机制？下面我们将以重铬酸钾溶液为主要例子，从色彩变化出发探讨神奇的化学平衡。</em></p>

## 2　重铬酸钾溶液的变色反应

重铬酸钾溶液中主要存在两大可逆反应：

1. 氢铬酸根与重铬酸根的二聚平衡；
2. <a class="annotation-term" href="#note-zh-s2">氢铬酸根的电离平衡</a>。

对应的化学反应式为：

<div class="equilibrium-equation">
  <span class="species"><span class="formula dichromate">Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup>（橙色）</span><span class="species-name">重铬酸根</span></span>
  <span>+ H<sub>2</sub>O ⇌ 2</span>
  <span class="species"><span class="formula">HCrO<sub>4</sub><sup>−</sup></span><span class="species-name">氢铬酸根</span></span>
</div>

<div class="equilibrium-equation">
  <span class="species"><span class="formula">HCrO<sub>4</sub><sup>−</sup></span><span class="species-name">氢铬酸根</span></span>
  <span>⇌ H<sup>+</sup> +</span>
  <span class="species"><span class="formula chromate">CrO<sub>4</sub><sup>2−</sup>（黄色）</span><span class="species-name">铬酸根</span></span>
</div>

重铬酸根显橙色，铬酸根显黄色。因此，我们可以根据溶液颜色的变化判断物质浓度的相对大小，进而分析化学平衡的移动。

<p class="transition-note"><em>我们已经知道重铬酸钾溶液中存在两个关键平衡反应，其定量分析离不开平衡常数。然而，即使在等温条件下，前面定义的平衡常数也会随溶液组分不同而变化，这是为什么呢？</em></p>

## 3　活度的概念

“物质 B 的浓度”指单位体积混合物中物质 B 的物质的量。高中教材中通过浓度定义的平衡常数称为**经验平衡常数**。经验平衡常数不仅受温度影响，也会受到离子浓度影响。高中阶段所说的“平衡常数的大小只与温度有关”，隐含了反应体系为理想稀溶液的假设。

实际电解质溶液中，离子与离子、离子与溶剂（水分子）之间存在复杂的静电作用，使实际溶液中物质的<a class="annotation-term" href="#note-zh-s3">热力学</a>行为偏离理想状态。离子浓度越高、电荷数越大，这种影响通常越严重。为修正这种影响，可以定义：

$$
a_\mathrm{B}=\gamma_\mathrm{B}\frac{c_\mathrm{B}}{c^\circ}
$$

其中，$a_\mathrm{B}$ 是 B 的**活度**（无量纲），可理解为经过修正的浓度；$\gamma_\mathrm{B}$ 是 B 的活度系数，通常小于 1；$c^\circ$ 是标准浓度，通常为 $1\ \mathrm{mol\,L^{-1}}$。

修正后得到的热力学平衡常数称为**活度常数**（即溶液体系的**标准平衡常数**）。对于反应

$$
mA+nB \rightleftharpoons pC+qD
$$

其活度常数为：

$$
K^\circ=\frac{a_\mathrm{C}^{p}a_\mathrm{D}^{q}}
{a_\mathrm{A}^{m}a_\mathrm{B}^{n}}
$$

该表达式与浓度常数 $K$ 具有相同形式。精确计算应使用活度和活度常数，但计算较复杂；对于稀溶液，活度系数接近 1，使用浓度和浓度常数造成的误差通常不大，因此仍得到广泛应用。

<p class="transition-note"><em>由活度获得的标准平衡常数是描述平衡的重要工具。但是，如果一个可逆反应尚未达到平衡，例如反应刚刚开始，或改变条件打破了已有平衡，我们如何判断反应进行的正、逆方向？反应进行到什么限度才能达到平衡？</em></p>

## 4　化学反应的方向与限度

高中教材告诉我们，通过比较浓度商 $Q$ 与平衡常数 $K$ 的相对大小，可以判断化学反应的方向；而在<a class="annotation-term" href="#note-zh-s4">一定条件下</a>，比较每摩尔化学反应的吉布斯自由能变与 0 的大小，又可以判断反应能否自发进行。二者可通过**化学反应等温式**建立热力学联系：

$$
\Delta_\mathrm{r}G_\mathrm{m}
=\Delta_\mathrm{r}G_\mathrm{m}^{\circ}+RT\ln Q
$$

下标 $\mathrm r$ 表示化学反应，下标 $\mathrm m$ 表示每摩尔化学反应，$\Delta_\mathrm{r}G_\mathrm{m}^{\circ}$ 是标准摩尔反应吉布斯自由能变化，可视为热力学“参照点”。

达到平衡时，$\Delta_\mathrm{r}G_\mathrm{m}=0$，且 $Q=K^\circ$，因此：

$$
\Delta_\mathrm{r}G_\mathrm{m}
=RT\ln\!\left(\frac{Q}{K^\circ}\right)
$$

所以，$Q$ 与 $K^\circ$ 的大小关系和 $\Delta_\mathrm{r}G_\mathrm{m}$ 与 0 的大小关系在判断反应方向时完全一致：

- $Q<K^\circ,\ \Delta_\mathrm{r}G_\mathrm{m}<0$：正反应自发进行；
- $Q=K^\circ,\ \Delta_\mathrm{r}G_\mathrm{m}=0$：反应达到平衡；
- $Q>K^\circ,\ \Delta_\mathrm{r}G_\mathrm{m}>0$：逆反应自发进行。

<div class="thought-card">
  <div class="thought-title">思考 1</div>
  <p>向橙色的重铬酸钾溶液中加入足量氢氧化钠，溶液会变成什么颜色？</p>
  <details>
    <summary>显示答案</summary>
    <div class="thought-answer">
      氢氧化钠使体系中 H<sup>+</sup> 浓度降低，HCrO<sub>4</sub><sup>−</sup> ⇌ H<sup>+</sup> + CrO<sub>4</sub><sup>2−</sup> 的浓度商减小，平衡右移，黄色 CrO<sub>4</sub><sup>2−</sup> 增多。HCrO<sub>4</sub><sup>−</sup> 的减少也使 Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup> + H<sub>2</sub>O ⇌ 2HCrO<sub>4</sub><sup>−</sup> 向右移动，橙色 Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup> 减少。因此，溶液颜色向黄色变化。
    </div>
  </details>
</div>

<p class="transition-note"><em>顾名思义，化学反应等温式只能用于温度不变的情况。那么，温度本身是如何影响化学平衡的呢？</em></p>

## 5　温度对化学平衡的影响

根据勒夏特列原理，升温会使化学平衡向吸热反应方向移动；降温会使平衡向放热反应方向移动。这一定性描述同样具有严格的热力学基础。

等压条件下，当温度从 $T$ 发生无限小变化时，标准平衡常数 $K^\circ$ 与温度的关系满足：

$$
\frac{\mathrm{d}\ln K^\circ}{\mathrm{d}T}
=\frac{\Delta_\mathrm{r}H_\mathrm{m}^{\circ}}{RT^2}
$$

该式称为化学平衡中范特霍夫公式的<a class="annotation-term" href="#note-zh-s5">微分式</a>。其中，$\Delta_\mathrm{r}H_\mathrm{m}^{\circ}$ 是各物质均处于标准态时的摩尔反应焓变。

对于吸热反应，$\Delta_\mathrm{r}H_\mathrm{m}^{\circ}>0$，因此 $\mathrm{d}\ln K^\circ/\mathrm{d}T>0$，即 $K^\circ$ 随温度升高而增大，升温有利于正反应。对于放热反应，$\Delta_\mathrm{r}H_\mathrm{m}^{\circ}<0$，平衡常数随温度升高而减小，升温不利于正反应。

<div class="thought-card">
  <div class="thought-title">思考 2</div>
  <p>已知 Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup> + H<sub>2</sub>O ⇌ 2HCrO<sub>4</sub><sup>−</sup> 和 HCrO<sub>4</sub><sup>−</sup> ⇌ H<sup>+</sup> + CrO<sub>4</sub><sup>2−</sup> 均为吸热反应。对适当浓度的重铬酸钾溶液降温或加热，颜色分别会怎样变化？</p>
  <details>
    <summary>显示答案</summary>
    <div class="thought-answer">
      吸热反应升温时平衡常数增大，两步平衡均向正反应方向移动：橙色 Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup> 浓度降低，黄色 CrO<sub>4</sub><sup>2−</sup> 浓度升高，溶液颜色偏黄。反之，降温会使溶液的橙色加深。
    </div>
  </details>
</div>

<p class="transition-note"><em>到这里，我们已经了解了反应平衡、影响平衡的因素以及平衡移动。在把这些知识用于重铬酸钾溶液的颜色变化实验之前，还需要弄清溶液颜色与离子组成之间的具体物理关系。</em></p>

## 6　溶液颜色与离子组成

首先，不同离子会呈现不同颜色：重铬酸根显橙色，铬酸根显黄色，氢铬酸根则几乎无色。这是因为它们的电子能级结构不同。白光照射溶液时，离子中的电子会吸收特定波长的光，从基态跃迁到激发态。某种物质吸收最强的波长称为其**特征吸收波长**。

重铬酸根主要吸收蓝紫光，剩余的红黄光混合呈橙色；铬酸根主要吸收蓝绿光，剩余光呈黄色；氢铬酸根主要吸收人眼不可见的紫外光，在可见光区吸收较弱。因此，分析溶液的颜色种类——更严谨地说，分析其特征吸收波长——可以帮助判断有色离子的组成。

其次，溶液颜色深浅与有色离子浓度有关。吸光度定义为：

$$
A=\log_{10}\!\left(\frac{I_0}{I}\right)
$$

其中，$I_0$ 为入射光强度，$I$ 为透射光强度。根据**朗伯-比尔定律**：

$$
A=\varepsilon bc
$$

其中，$\varepsilon$ 为摩尔吸光系数，$b$ 为光程，$c$ 为吸光物质浓度。吸光度 $A$ 与吸光物种浓度 $c$ 成正比；当存在多种吸光物种时，总吸光度是各物种吸光度之和。

因此，在入射光条件固定时，重铬酸钾溶液中各种含铬离子的浓度直接决定溶液颜色。在一些简单情形下，含铬离子浓度可与溶液颜色建立一一对应关系，为离子浓度预测提供可行性。

<div class="thought-card">
  <div class="thought-title">思考 3</div>
  <p>Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup> 浓度为 <em>c</em> 的重铬酸钾溶液吸光度为 <em>A</em>。将其稀释一倍后，在相同条件下测量，吸光度一定是 <em>A</em>/2 吗？</p>
  <details>
    <summary>显示答案</summary>
    <div class="thought-answer">
      不一定。朗伯-比尔定律中的“浓度”是单一吸光物种的实际平衡浓度，而不是配制的总浓度。稀释会使 Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup> + H<sub>2</sub>O ⇌ 2HCrO<sub>4</sub><sup>−</sup> 向离子数较多的一侧移动，同时 HCrO<sub>4</sub><sup>−</sup> ⇌ H<sup>+</sup> + CrO<sub>4</sub><sup>2−</sup> 也会移动。Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup> 会在 <em>c</em>/2 基础上进一步降低，新生成物种对吸光度的贡献又不同。因此，总吸光度与总 Cr 浓度之间不是简单线性关系，而是<a class="annotation-term" href="#note-zh-s6">由两步平衡共同决定的</a>。
    </div>
  </details>
</div>

<p class="transition-note"><em>以上内容从微观层面解释了颜色产生的物理原因，并建立了颜色深浅与浓度的定量关系。因此，理论上只要知道溶液颜色，就可以反推出各组分浓度——前提是能够精准建立“颜色”与“浓度”的对应关系。</em></p>

<p class="transition-note"><em>传统上，这项工作由分光光度计完成。但分光光度计价格较高、操作相对复杂，不便于现场或快速检测；对于含有多种有色离子的重铬酸钾溶液，直接应用朗伯-比尔定律也并不简单。</em></p>

<p class="transition-note"><em>我们能否用手机拍摄溶液，让计算机跳过“吸光度”，直接根据颜色给出各组分浓度？机器学习能够从大量数据中学习颜色与浓度的对应关系，使这一设想成为现实。</em></p>

<p class="transition-note"><em>知识讲解到这里结束。接下来，可以拿起相机，探索重铬酸钾溶液绚丽多彩的化学平衡。</em></p>

<div id="note-zh-s2" class="annotation-modal">
  <div class="annotation-dialog">
    <a href="#" class="annotation-close" aria-label="关闭">×</a>
    <h4>氢铬酸根的电离平衡</h4>
    <p>理论上还存在 HCrO<sub>4</sub><sup>−</sup> + H<sup>+</sup> ⇌ H<sub>2</sub>CrO<sub>4</sub>。铬酸 H<sub>2</sub>CrO<sub>4</sub> 是中等强度酸，在溶液中有两步电离；第一步电离平衡常数 K<sub>a1</sub> 远大于第二步 K<sub>a2</sub>，所以只有在极端酸性条件下才需要重点考虑铬酸分子的存在。</p>
  </div>
</div>

<div id="note-zh-s3" class="annotation-modal">
  <div class="annotation-dialog">
    <a href="#" class="annotation-close" aria-label="关闭">×</a>
    <h4>热力学</h4>
    <p>热力学研究宏观体系的热现象、热与其他能量形式之间的转换关系，以及体系变化时相关物理量的变化。化学平衡、焓和熵等均属于热力学的研究范围。</p>
  </div>
</div>

<div id="note-zh-s4" class="annotation-modal">
  <div class="annotation-dialog">
    <a href="#" class="annotation-close" aria-label="关闭">×</a>
    <h4>一定条件下</h4>
    <p>这里指等温、等压且非体积功为零。高中阶段讨论的敞口烧杯反应通常默认满足这些条件。</p>
  </div>
</div>

<div id="note-zh-s5" class="annotation-modal">
  <div class="annotation-dialog">
    <a href="#" class="annotation-close" aria-label="关闭">×</a>
    <h4>范特霍夫公式的微分式</h4>
    <p>若温度变化范围不大，可近似认为 Δ<sub>r</sub>H<sub>m</sub><sup>°</sup> 与温度无关，从而得到积分式：</p>
    <p><em>ln(K<sub>2</sub><sup>°</sup>/K<sub>1</sub><sup>°</sup>) = (Δ<sub>r</sub>H<sub>m</sub><sup>°</sup>/R)(1/T<sub>1</sub> − 1/T<sub>2</sub>)</em></p>
    <p>对于吸热反应，升温时 T<sub>2</sub> &gt; T<sub>1</sub>，右侧为正，因此 K<sub>2</sub><sup>°</sup> &gt; K<sub>1</sub><sup>°</sup>。</p>
  </div>
</div>

<div id="note-zh-s6" class="annotation-modal">
  <div class="annotation-dialog">
    <a href="#" class="annotation-close" aria-label="关闭">×</a>
    <h4>两步平衡共同决定</h4>
    <p>若要用朗伯-比尔定律分析溶液中各组分浓度，需要测量不同波长下的总吸光度。总吸光度是各单一物种吸光度的加和，随后需通过求解线性方程组得到各物种浓度。</p>
  </div>
</div>
