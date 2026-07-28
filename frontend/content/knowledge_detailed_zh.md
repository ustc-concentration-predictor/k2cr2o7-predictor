## 1　知识回顾

通过课程学习我们知道，很多化学反应是可逆的。在一定条件下的可逆反应，正反应和逆反应的速率相等，反应混合物中各组分的浓度保持不变的状态即为化学平衡状态。

对于一般的可逆反应：

$$
mA+nB\rightleftharpoons pC+qD
$$

任意时刻的浓度商为

$$
Q=\frac{c(\mathrm{C})^p\cdot c(\mathrm{D})^q}
        {c(\mathrm{A})^m\cdot c(\mathrm{B})^n}
$$

。该反应在一定温度下达到化学平衡态后，其浓度商为定值，记作

$$
\left[
\frac{c(\mathrm{C})^p\cdot c(\mathrm{D})^q}
     {c(\mathrm{A})^m\cdot c(\mathrm{B})^n}
\right]_{\mathrm e}=K
$$

（下标 e 表示反应体系达到化学平衡）。常数 $K$ 称为化学平衡常数，其数值大小与温度有关。如果改变影响平衡的一个因素，平衡就向着能够减弱这种改变的方向移动，这就是勒夏特列原理，即化学平衡移动原理。

<p class="transition-note"><em>如何直观感受化学平衡的移动？如何揭示勒夏特列原理背后的定性物理化学机制？下面我们将以重铬酸钾溶液为主要的例子，从色彩的变化上探讨神奇的化学平衡。</em></p>

## 2　重铬酸钾溶液的变色反应

重铬酸钾溶液中主要存在两大可逆反应：1. 氢铬酸根与重铬酸根的二聚平衡；2. <a class="annotation-term" href="#note-zh-s2">氢铬酸根的电离平衡</a>*。其化学反应式为：

$$
\underset{\text{重铬酸根}}{\color{#E87500}{\mathrm{Cr_2O_7^{2-}\ （橙色）}}}
+\underset{\text{水}}{\mathrm{H_2O}}
\rightleftharpoons
2\underset{\text{氢铬酸根}}{\mathrm{HCrO_4^-}}
$$

$$
\underset{\text{氢铬酸根}}{\mathrm{HCrO_4^-}}
\rightleftharpoons
\underset{\text{氢离子}}{\mathrm{H^+}}+
\underset{\text{铬酸根}}{\color{#D4A000}{\mathrm{CrO_4^{2-}\ （黄色）}}}
$$

重铬酸根显橙色，铬酸根显黄色，所以我们可以根据溶液颜色的变化来判断物质浓度的相对大小，进而分析化学平衡的移动。

<p class="transition-note"><em>我们已经知道了重铬酸钾溶液中存在两个关键的平衡反应，其定量分析离不开平衡常数的使用。然而，实际即便在等温条件下，我们前面定义的平衡常数也会随溶液组分不同而变化，这是为什么呢？</em></p>

## 3　活度的概念

我们知道，“B 的浓度 $c_\mathrm{B}$”指的是单位体积混合物中物质 B 的物质的量，高中教材中通过浓度定义的平衡常数为“经验平衡常数”。经验平衡常数的大小不仅受温度影响，还会受到离子浓度的影响。我们在高中的知识体系中认为“平衡常数的大小只与温度有关”，蕴含着反应体系为理想稀溶液的假设。然而，在实际电解质溶液中，离子与离子、离子与溶剂（水分子）间存在复杂的静电作用，使得实际溶液中物质的<a class="annotation-term" href="#note-zh-s3">热力学</a>*行为偏离理想状态，离子浓度越高、电荷数越大，影响越严重。为了克服这种影响，需要对离子浓度进行修正：

$$
a_\mathrm{B}=\gamma_\mathrm{B}\frac{c_\mathrm{B}}{c^\Theta}
$$

其中，$a_\mathrm{B}$ 称为 B 的活度（无量纲），可以理解为经过修正的浓度；修正项 $\gamma_\mathrm{B}$ 称为 B 的活度系数，通常小于 1；$c^\Theta$ 为标准浓度，通常为 $1\ \mathrm{mol/L}$。修正后得到的热力学平衡常数称为活度常数 $K^\Theta$（即溶液系统的标准平衡常数）。反应

$$
mA+nB\rightleftharpoons pC+qD
$$

的活度常数表达式为

$$
K^\Theta=
\left[
\frac{a_\mathrm{C}^p\cdot a_\mathrm{D}^q}
     {a_\mathrm{A}^m\cdot a_\mathrm{B}^n}
\right]_{\mathrm e}
$$

与浓度常数 $K$ 具有相同的表达形式。精确计算应该使用活度和活度常数，但是比较复杂。使用浓度和浓度常数的计算相对简单得多，对稀溶液而言误差也不大（离子浓度较低时活度系数约等于 1），所以仍然广泛应用。

<p class="transition-note"><em>由活度获得的标准平衡常数是描述平衡的重要工具，但是，如果一个可逆反应尚未达到平衡（比如反应刚刚进行或改变条件打破已有的平衡），那么我们如何得知反应发生的正/逆方向呢？反应发生到什么限度才能达到平衡呢？</em></p>

## 4　化学反应的方向与限度

高中教材告诉我们，通过比较浓度商 $Q$ 与反应平衡常数 $K$ 的相对大小，就可以判断化学反应的正逆方向，而<a class="annotation-term" href="#note-zh-s4">一定条件下</a>*每摩尔化学反应的吉布斯自由能变 $\Delta G$ 与 0 的相对大小又可以判断反应是否能自发进行。二者可以通过化学反应等温式搭建热力学上的桥梁。

根据化学反应等温式

$$
\Delta_\mathrm rG_\mathrm m
=\Delta_\mathrm rG_\mathrm m^\Theta+RT\ln Q
$$

其中下标 r 表示化学反应，下标 m 表示每摩尔化学反应，$\Delta_\mathrm rG_\mathrm m^\Theta$ 为化学反应的标准摩尔吉布斯自由能变化值，可以看作热力学上的“参照点”。当 $\Delta_\mathrm rG_\mathrm m=0$ 时，化学反应达到平衡，此时的浓度商 $Q$ 即为标准平衡常数 $K^\Theta$，所以

$$
\Delta_\mathrm rG_\mathrm m^\Theta+RT\ln K^\Theta=0
$$

。代入化学反应等温式得

$$
\Delta_\mathrm rG_\mathrm m=RT\ln\frac{Q}{K^\Theta}
$$

到此，我们不难看出，$Q$ 与 $K$ 的大小关系与 $\Delta_\mathrm rG_\mathrm m$ 与 0 的大小关系在判断化学反应方向上是等同的。因此，

$$
Q<K^\Theta,\quad \Delta G<0\qquad \text{自发进行正反应}
$$

$$
Q=K^\Theta,\quad \Delta G=0\qquad \text{反应达到平衡，即达到最大反应限度}
$$

$$
Q>K^\Theta,\quad \Delta G>0\qquad \text{自发进行逆反应}
$$

<div class="thought-card">
  <div class="thought-title">思考1：</div>
  <p>向橙色的重铬酸钾溶液中加入足量氢氧化钠，那么溶液会变成什么颜色？</p>
  <details>
    <summary><span class="answer-show">显示答案</span><span class="answer-hide">隐藏答案</span></summary>
    <div class="thought-answer">
      氢氧化钠的加入降低体系中氢离子浓度，反应 HCrO<sub>4</sub><sup>−</sup> ⇌ H<sup>+</sup> + CrO<sub>4</sub><sup>2−</sup> 的浓度商 Q 减小，平衡右移，使 CrO<sub>4</sub><sup>2−</sup> 浓度增大，HCrO<sub>4</sub><sup>−</sup> 浓度减小。同时，HCrO<sub>4</sub><sup>−</sup> 浓度减小也使反应 Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup> + H<sub>2</sub>O ⇌ 2HCrO<sub>4</sub><sup>−</sup> 浓度商减小，平衡右移，Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup> 浓度降低。故黄色的 CrO<sub>4</sub><sup>2−</sup> 浓度增大，橙色的 Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup> 浓度降低，体系颜色会向黄色变化。
    </div>
  </details>
</div>

<p class="transition-note"><em>顾名思义，化学反应等温式只能用于温度不变的情况。那么温度本身是如何影响化学平衡的呢？</em></p>

## 5　温度对化学平衡的影响

我们知道，根据勒夏特列原理，升温会使化学平衡向吸热反应的方向移动；降温会使化学平衡向放热反应的方向移动。这一定性的关系描述同样蕴含着严格的热力学原理。等压情况下，当系统温度从 $T$ 变化为 $T+\Delta T$ 时（$\Delta T$ 无限小），化学反应的标准平衡常数 $K^\Theta$ 与温度变化量 $\Delta T$ 的关系满足

$$
\frac{\Delta\ln K^\Theta}{\Delta T}
=\frac{\Delta_\mathrm rH_\mathrm m^\Theta}{RT^2}
$$

该式称为化学平衡中的范特霍夫公式的<a class="annotation-term" href="#note-zh-s5">微分式</a>*，其中 $\Delta_\mathrm rH_\mathrm m^\Theta$ 是各物质均处于标准态时的摩尔反应焓变值。可见，对于吸热反应，$\Delta_\mathrm rH_\mathrm m^\Theta>0$，$\Delta\ln K^\Theta/\Delta T>0$，即 $K^\Theta$ 随温度的升高而增大，升温对正向反应有利。对于放热反应，$\Delta_\mathrm rH_\mathrm m^\Theta<0$，$\Delta\ln K^\Theta/\Delta T<0$，即 $K^\Theta$ 随温度的升高而减小，升温对正向反应不利。

<div class="thought-card">
  <div class="thought-title">思考2：</div>
  <p>已知反应 Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup> + H<sub>2</sub>O ⇌ 2HCrO<sub>4</sub><sup>−</sup> 与 HCrO<sub>4</sub><sup>−</sup> ⇌ H<sup>+</sup> + CrO<sub>4</sub><sup>2−</sup> 均为吸热反应，那么对适当浓度的重铬酸钾溶液进行降温或加热，溶液颜色分别会怎样变化？</p>
  <details>
    <summary><span class="answer-show">显示答案</span><span class="answer-hide">隐藏答案</span></summary>
    <div class="thought-answer">
      吸热反应 Δ<sub>r</sub>H<sub>m</sub><sup>Θ</sup>&gt;0，升温使 K<sup>Θ</sup> 增大，Q&lt;K<sup>Θ</sup>，两反应均自发正向移动，橙色 Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup> 浓度降低，黄色 CrO<sub>4</sub><sup>2−</sup> 浓度升高，溶液颜色偏黄。反之，降温使溶液橙色加深。
    </div>
  </details>
</div>

<p class="transition-note"><em>到这里，大家已经了解了反应的平衡，影响平衡的因素，以及平衡的移动。在将这些知识点应用在重铬酸钾溶液的颜色变化实验之前，我们需要先弄清楚溶液颜色与离子组成之间的具体物理关系。</em></p>

## 6　溶液颜色与离子组成

首先，不同离子会呈现不同的颜色，比如重铬酸根显橙色，铬酸根显黄色，氢铬酸根则几乎无色，这是为什么呢？这是因为它们内部的电子能级结构不同，当白光（包含所有颜色）照射溶液时，离子中的电子会吸收特定波长的光，从基态跃迁到激发态。某种物质会对特定波长的光子吸收最强烈，该波长称为该物质的特征吸收波长。重铬酸根主要吸收蓝紫光，剩下的红黄光混合成橙色；铬酸根主要吸收蓝绿光，剩下的红橙光混合成黄色；氢铬酸根吸收的则主要是人类看不见的紫外光，所以在可见光区几乎没有吸收，肉眼看起来接近无色。因此，通过分析溶液的颜色种类（更严谨地说，溶液吸收光的特征波长），就可以判断有色离子组成。

其次，溶液颜色的深浅与有色离子的浓度有关，可以简单认为有色离子浓度越大，溶液颜色越深。这一直观的结论也有物理定律支撑。为了量化颜色的深与浅，人们采用吸光度 $A$ 来描述溶液“拦住了多少光”：$A=\log(I_0/I)$，$I_0$ 为入射光强度，$I$ 为透射光强度。根据朗伯-比尔定律，

$$
A=\varepsilon bc
$$

其中 $\varepsilon$ 为摩尔吸光系数（反映吸光物质固有属性，也与入射光波长、溶剂、温度有关），$b$ 为光程长度（光在溶液中实际穿过的距离），$c$ 为吸光物质浓度。朗伯-比尔定律告诉我们，吸光度 $A$ 与吸光物质的浓度 $c$ 成正比。当溶液中有多种吸光物种时，总吸光度是各物种吸光度的加和。

因此，在入射光一定的情况下，重铬酸钾溶液中各种含铬离子的浓度直接决定了溶液的颜色。在一些简单的情形下，体系中含铬离子的浓度可以与溶液颜色建立一一对应的关系，为体系的离子浓度预测提供了可行性。

<div class="thought-card">
  <div class="thought-title">思考3：</div>
  <p>Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup> 浓度为 c 的重铬酸钾溶液吸光度为 A，将其稀释一倍后用同样的条件进行测量，溶液吸光度一定是 A/2 吗？</p>
  <details>
    <summary><span class="answer-show">显示答案</span><span class="answer-hide">隐藏答案</span></summary>
    <div class="thought-answer">
      并不是。朗伯-比尔定律描述的吸光度与物质浓度的正比关系仅仅针对单一吸光物质，其“浓度”指吸光物种的实际平衡浓度，而非配制的总浓度。当对重铬酸钾溶液进行稀释时，针对反应 Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup> + H<sub>2</sub>O ⇌ 2HCrO<sub>4</sub><sup>−</sup>，体系总离子浓度降低，根据勒夏特列原理，平衡向总离子浓度升高的方向移动，即平衡右移（反应 HCrO<sub>4</sub><sup>−</sup> ⇌ H<sup>+</sup> + CrO<sub>4</sub><sup>2−</sup> 也同时正向移动）。一方面，Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup> 浓度会在 c/2 的基础上进一步降低；另一方面，生成的 HCrO<sub>4</sub><sup>−</sup> 与 CrO<sub>4</sub><sup>2−</sup> 对吸光度的贡献往往与 Cr<sub>2</sub>O<sub>7</sub><sup>2−</sup> 不同。因此，我们所测量的溶液总吸光度与总 Cr 浓度之间并不是简单的线性关系，而是<a class="annotation-term" href="#note-zh-s6">由两步平衡共同决定的</a>*。
    </div>
  </details>
</div>

<div class="transition-note">
  <p><em>以上我们从微观层面解释了颜色产生的物理原因（特征吸收波长），也建立了颜色深浅与浓度的定量关系（朗伯-比尔定律）。所以，理论上只要知道了溶液的颜色，就可以反推出其中各组分的浓度——前提是我们能够精准地建立“颜色”与“浓度”之间的对应关系。</em></p>
  <p><em>传统上，这项工作通常由分光光度计完成：它精确测量特定波长的吸光度，然后通过朗伯-比尔定律计算浓度。但分光光度计价格不菲，操作也相对复杂，不便于现场或快速检测。同时，思考3也告诉我们，对于重铬酸钾溶液这种含有多样有色离子的体系，朗伯比尔定律应用起来并不简单。</em></p>
  <p><em>大家此刻有没有这样的想法：我们能不能用手机拍一张溶液的照片，让计算机跳过“吸光度”，直接通过颜色来告诉我们各个组分的浓度呢？近年来，机器学习技术的发展让我们的想法成为了现实。机器学习可通过大量数据学习颜色与浓度之间的对应关系，无需预知吸光度、摩尔吸光系数等物理量。我们无需走进实验室就可以轻松分析重铬酸钾溶液中的离子浓度了！</em></p>
  <p><em>知识讲解部分到这里就结束了，接下来我们可以拿起相机，探究重铬酸钾溶液绚丽多彩的化学平衡了！大家准备好了吗？</em></p>
</div>

<div id="note-zh-s2" class="annotation-modal">
  <div class="annotation-dialog">
    <a href="#" class="annotation-close" aria-label="关闭">×</a>
    <h4>氢铬酸根的电离平衡</h4>
    <p>理论上也存在反应 HCrO<sub>4</sub><sup>−</sup> + H<sup>+</sup> ⇌ H<sub>2</sub>CrO<sub>4</sub>。铬酸 H<sub>2</sub>CrO<sub>4</sub> 为中等强度酸，在溶液中存在两步电离，但第一步的电离平衡常数（K<sub>a1</sub>）远大于第二步（K<sub>a2</sub>），所以极端酸性的条件下才会考虑铬酸分子的存在。</p>
  </div>
</div>

<div id="note-zh-s3" class="annotation-modal">
  <div class="annotation-dialog">
    <a href="#" class="annotation-close" aria-label="关闭">×</a>
    <h4>热力学</h4>
    <p>热力学研究宏观系统的热现象、热和其他形式能量之间的转换关系，以及系统变化时所引起的这些物理量的变化。化学平衡、焓、熵等都属于热力学的研究范围。</p>
  </div>
</div>

<div id="note-zh-s4" class="annotation-modal">
  <div class="annotation-dialog">
    <a href="#" class="annotation-close" aria-label="关闭">×</a>
    <h4>一定条件下</h4>
    <p>该条件指等温等压且非体积功为零。高中阶段讨论的敞口烧杯反应中，上述条件通常默认满足。</p>
  </div>
</div>

<div id="note-zh-s5" class="annotation-modal">
  <div class="annotation-dialog">
    <a href="#" class="annotation-close" aria-label="关闭">×</a>
    <h4>微分式</h4>
    <p>若温度变化范围不大，Δ<sub>r</sub>H<sub>m</sub><sup>Θ</sup> 近似为与温度无关的常数，则可得到范特霍夫公式的定积分式：</p>
    <p><em>ln(K<sup>Θ</sup><sub>T2</sub>/K<sup>Θ</sup><sub>T1</sub>) = (Δ<sub>r</sub>H<sub>m</sub><sup>Θ</sup>/R)(1/T<sub>1</sub> − 1/T<sub>2</sub>)</em></p>
    <p>也可以根据这个公式理解温度对平衡常数的影响。对于吸热反应，Δ<sub>r</sub>H<sub>m</sub><sup>Θ</sup>&gt;0，升温使 T<sub>2</sub>&gt;T<sub>1</sub>，则等式大于零，所以 K<sup>Θ</sup><sub>T2</sub>&gt;K<sup>Θ</sup><sub>T1</sub>，平衡常数增大。</p>
  </div>
</div>

<div id="note-zh-s6" class="annotation-modal">
  <div class="annotation-dialog">
    <a href="#" class="annotation-close" aria-label="关闭">×</a>
    <h4>由两步平衡共同决定的</h4>
    <p>此时如果需要应用朗伯比尔定律来分析溶液中各组分的浓度，则需要测量不同波长下的总吸光度（总吸光度为各个单一物种吸光度的加和），再求解线性方程组。</p>
  </div>
</div>
