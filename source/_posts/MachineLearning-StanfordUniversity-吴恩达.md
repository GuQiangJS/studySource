---
title: 机器学习 - 斯坦福大学 吴恩达
date: 2018-12-01
updated: 2018-12-01
tags:
 - 编程
 - 机器学习
 - 吴恩达
categories:
 - 机器学习
mathjax: true
description: <!—more—->
typora-root-url: MachineLearning-StanfordUniversity-吴恩达
---

### Week 1

#### What is Machine Learning?

Two definitions of Machine Learning are offered. Arthur Samuel described it as: "the field of study that gives computers the ability to learn without being explicitly programmed." This is an older, informal definition.

Tom Mitchell provides a more modern definition: "A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E."

Example: playing checkers.

E = the experience of playing many games of checkers

T = the task of playing checkers.

P = the probability that the program will win the next game.

In general, any machine learning problem can be assigned to one of two broad classifications:

Supervised learning and Unsupervised learning.

#### 什么是机器学习？

提供了机器学习的两个定义。 Arthur Samuel将其描述为：“研究领域，使计算机无需明确编程即可学习。” 这是一个较旧的非正式定义。

Tom Mitchell提供了一个更现代的定义：“据说计算机程序可以从经验E中学习某些任务T和绩效测量P，如果它在T中的任务中的表现（由P测量）随经验E而提高。“

示例：玩跳棋。

E =玩许多跳棋游戏的经验

T =玩跳棋的任务。

P =程序赢得下一场比赛的概率。

通常，任何机器学习问题都可以分配到两个广泛的分类之一：

监督学习和无监督学习。

#### Supervised Learning

In supervised learning, we are given a data set and already know what our correct output should look like, having the idea that there is a relationship between the input and the output.

Supervised learning problems are categorized into "regression" and "classification" problems. In a regression problem, we are trying to predict results within a continuous output, meaning that we are trying to map input variables to some continuous function. In a classification problem, we are instead trying to predict results in a discrete output. In other words, we are trying to map input variables into discrete categories.

**Example 1:**

Given data about the size of houses on the real estate market, try to predict their price. Price as a function of size is a continuous output, so this is a regression problem.

We could turn this example into a classification problem by instead making our output about whether the house "sells for more or less than the asking price." Here we are classifying the houses based on price into two discrete categories.

**Example 2**:

(a) Regression - Given a picture of a person, we have to predict their age on the basis of the given picture

(b) Classification - Given a patient with a tumor, we have to predict whether the tumor is malignant or benign.

#### 监督学习

在有监督的学习中，我们得到一个数据集，并且已经知道我们的正确输出应该是什么样的，并且认为输入和输出之间存在关系。

监督学习问题分为“回归”和“分类”问题。在回归问题中，我们试图在连续输出中预测结果，这意味着我们正在尝试将输入变量映射到某个连续函数。在分类问题中，我们试图在离散输出中预测结果。换句话说，我们试图将输入变量映射到离散类别。

例1：

鉴于有关房地产市场房屋面积的数据，请尝试预测房价。作为大小函数的价格是连续输出，因此这是一个回归问题。

我们可以将这个例子变成一个分类问题，而不是让我们的输出关于房子“卖得多于还是低于要价”。在这里，我们将基于价格的房屋分为两个不同的类别。

例2：

（a）回归 - 鉴于一个人的照片，我们必须根据给定的图片预测他们的年龄

（b）分类 - 鉴于患有肿瘤的患者，我们必须预测肿瘤是恶性的还是良性的。

#### Unsupervised Learning

Unsupervised learning allows us to approach problems with little or no idea what our results should look like. We can derive structure from data where we don't necessarily know the effect of the variables.

We can derive this structure by clustering the data based on relationships among the variables in the data.

With unsupervised learning there is no feedback based on the prediction results.

**Example:**

Clustering: Take a collection of 1,000,000 different genes, and find a way to automatically group these genes into groups that are somehow similar or related by different variables, such as lifespan, location, roles, and so on.

Non-clustering: The "Cocktail Party Algorithm", allows you to find structure in a chaotic environment. (i.e. identifying individual voices and music from a mesh of sounds at a [cocktail party](https://en.wikipedia.org/wiki/Cocktail_party_effect)).

#### 无监督学习

无监督学习使我们能够在很少或根本不知道我们的结果应该是什么样的情况下解决问题。 我们可以从数据中导出结构，我们不一定知道变量的影响。

我们可以通过基于数据中变量之间的关系聚类数据来推导出这种结构。

在无监督学习的情况下，没有基于预测结果的反馈。

例：

聚类：收集1,000,000个不同基因的集合，并找到一种方法将这些基因自动分组成不同的相似或通过不同变量相关的组，例如寿命，位置，角色等。

非聚类：“鸡尾酒会算法”允许您在混乱的环境中查找结构。 （即在鸡尾酒会上识别来自声音网格的个别声音和音乐）。

### Model Representation

To establish notation for future use, we’ll use $x^{(i)}$ to denote the “input” variables (living area in this example), also called input features, and $y^{(i)}$ to denote the “output” or target variable that we are trying to predict (price). A pair $(x^{(i)} , y^{(i)} )$ is called a training example, and the dataset that we’ll be using to learn—a list of m training examples $(x^{(i)} , y^{(i)} )$ ;i=1,...,m—is called a training set. Note that the superscript “(i)” in the notation is simply an index into the training set, and has nothing to do with exponentiation. We will also use X to denote the space of input values, and Y to denote the space of output values. In this example, X = Y = ℝ.

To describe the supervised learning problem slightly more formally, our goal is, given a training set, to learn a function h : X → Y so that h(x) is a “good” predictor for the corresponding value of y. For historical reasons, this function h is called a hypothesis. Seen pictorially, the process is therefore like this:

![img](H6qTdZmYEeaagxL7xdFKxA_2f0f671110e8f7446bb2b5b2f75a8874_Screenshot-2016-10-23-20.14.58.png?expiry=1543795200000&hmac=-eFQGqvyfXYeOBHwKAosEPlxxf2iyo4NJLLcuSY5V-8.png)

When the target variable that we’re trying to predict is continuous, such as in our housing example, we call the learning problem a regression problem. When y can take on only a small number of discrete values (such as if, given the living area, we wanted to predict if a dwelling is a house or an apartment, say), we call it a classification problem.

#### 模型表示

为了建立未来使用的符号，我们将使用 $x^{(i)}$来表示“输入”变量（在此示例中为生活区域），也称为输入要素，并使用$y^{(i)}$来表示“输出“或我们试图预测的目标变量（价格）。一对（$x^{(i)}$，$y^{(i)}$）被称为训练示例，我们将用于学习的数据集 -  m个训练样例列表（$x^{(i)}$，$y^{(i)}$）; i = 1，...，m-称为训练集。请注意，符号中的上标“（i）”只是训练集的索引，与取幂无关。我们还将使用X来表示输入值的空间，并使用Y来表示输出值的空间。在这个例子中，X = Y =ℝ。

为了更加正式地描述监督学习问题，我们的目标是，在给定训练集的情况下，学习函数h：X→Y，使得h（x）是y的对应值的“好”预测器。由于历史原因，该函数h被称为假设。从图中可以看出，这个过程是这样的：

![img](H6qTdZmYEeaagxL7xdFKxA_2f0f671110e8f7446bb2b5b2f75a8874_Screenshot-2016-10-23-20.14.58.png?expiry=1543795200000&hmac=-eFQGqvyfXYeOBHwKAosEPlxxf2iyo4NJLLcuSY5V-8.png)

当我们试图预测的目标变量是连续的时，例如在我们的住房示例中，我们将学习问题称为回归问题。当y只能承担少量离散值时（例如，如果给定生活区域，我们想要预测住宅是房屋还是公寓，请说），我们称之为分类问题。

#### Cost Function

We can measure the accuracy of our hypothesis function by using a **cost function**. This takes an average difference (actually a fancier version of an average) of all the results of the hypothesis with inputs from x's and the actual output y's.

$J(\theta_0, \theta_1) = \dfrac {1}{2m} \displaystyle \sum _{i=1}^m \left ( \hat{y}_{i}- y_{i} \right)^2 = \dfrac {1}{2m} \displaystyle \sum _{i=1}^m \left (h_\theta (x_{i}) - y_{i} \right)^2$

To break it apart, it is $\frac{1}{2}\bar{x}$ where $\bar{x}$ is the mean of the squares of $h_\theta (x_{i}) - y_{i}$ , or the difference between the predicted value and the actual value.

This function is otherwise called the "Squared error function", or "Mean squared error". The mean is halved $\left(\frac{1}{2}\right)$ as a convenience for the computation of the gradient descent, as the derivative term of the square function will cancel out the $\frac{1}{2}$ term. The following image summarizes what the cost function does:

![](R2YF5Lj3EeajLxLfjQiSjg_110c901f58043f995a35b31431935290_Screen-Shot-2016-12-02-at-5.23.31-PM.png?expiry=1543795200000&hmac=PxtG5Kq3XlGNP5qMhbAmIrZ1W1AkKJOPIgcY2NfHdd4.png)

#### 成本函数

我们可以使用成本函数来衡量我们的假设函数的准确性。 这需要假设的所有结果与x和实际输出y的输入之间的平均差异（实际上是平均值的更高版本）。

$J(\theta_0, \theta_1) = \dfrac {1}{2m} \displaystyle \sum _{i=1}^m \left ( \hat{y}_{i}- y_{i} \right)^2 = \dfrac {1}{2m} \displaystyle \sum _{i=1}^m \left (h_\theta (x_{i}) - y_{i} \right)^2$

为了区分它，它是$\frac{1}{2}\bar{x}$其中$\bar{x}$是$h_\theta (x_{i}) - y_{i}$ 的平方的平均值，或者 预测值与实际值之间的差异。

此函数另外称为“平方误差函数”或“均方误差”。 平均值减半$\left(\frac{1}{2}\right)$以方便计算梯度下降，因为平方函数的导数项将抵消$\frac{1}{2}$ 项。 下图总结了成本函数的作用：

![](R2YF5Lj3EeajLxLfjQiSjg_110c901f58043f995a35b31431935290_Screen-Shot-2016-12-02-at-5.23.31-PM.png?expiry=1543795200000&hmac=PxtG5Kq3XlGNP5qMhbAmIrZ1W1AkKJOPIgcY2NfHdd4.png)

#### Gradient Descent

So we have our hypothesis function and we have a way of measuring how well it fits into the data. Now we need to estimate the parameters in the hypothesis function. That's where gradient descent comes in.

Imagine that we graph our hypothesis function based on its fields $\theta_0$ and $\theta_1$ (actually we are graphing the cost function as a function of the parameter estimates). We are not graphing x and y itself, but the parameter range of our hypothesis function and the cost resulting from selecting a particular set of parameters.

We put $\theta_0$ on the x axis and $\theta_1$ on the y axis, with the cost function on the vertical z axis. The points on our graph will be the result of the cost function using our hypothesis with those specific theta parameters. The graph below depicts such a setup.

![img](bn9SyaDIEeav5QpTGIv-Pg_0d06dca3d225f3de8b5a4a7e92254153_Screenshot-2016-11-01-23.48.26.png?expiry=1543795200000&hmac=LCxVuGHteW6iXuI4phZkKO7edFtRTbW6w7mbz9K9KBQ.png)

We will know that we have succeeded when our cost function is at the very bottom of the pits in our graph, i.e. when its value is the minimum. The red arrows show the minimum points in the graph.

The way we do this is by taking the derivative (the tangential line to a function) of our cost function. The slope of the tangent is the derivative at that point and it will give us a direction to move towards. We make steps down the cost function in the direction with the steepest descent. The size of each step is determined by the parameter α, which is called the learning rate.

For example, the distance between each 'star' in the graph above represents a step determined by our parameter α. A smaller α would result in a smaller step and a larger α results in a larger step. The direction in which the step is taken is determined by the partial derivative of $J(\theta_0,\theta_1)$. Depending on where one starts on the graph, one could end up at different points. The image above shows us two different starting points that end up in two different places.

The gradient descent algorithm is:

repeat until convergence:

$\theta_j := \theta_j - \alpha \frac{\partial}{\partial \theta_j} J(\theta_0, \theta_1)$

where

j=0,1 represents the feature index number.

At each iteration j, one should simultaneously update the parameters $\theta_1$, $\theta_2$,...,$\theta_n$. Updating a specific parameter prior to calculating another one on the $j^{(th)}$ iteration would yield to a wrong implementation.

![img](yr-D1aDMEeai9RKvXdDYag_627e5ab52d5ff941c0fcc741c2b162a0_Screenshot-2016-11-02-00.19.56.png?expiry=1543795200000&hmac=LswhSw8rNSExqigPYLaeZhtqFAEjCibnLfixFipL8Wo.png)

#### 梯度下降

所以我们有假设函数，我们有一种方法可以衡量它与数据的匹配程度。现在我们需要估计假设函数中的参数。这就是梯度下降的地方。

想象一下，我们基于其字段$\theta_0$和$\theta_1$来绘制我们的假设函数（实际上我们将成本函数绘制为参数估计的函数）。我们不是绘制x和y本身，而是我们的假设函数的参数范围以及选择一组特定参数所产生的成本。

我们将$\theta_0$放在x轴上，将$\theta_1$放在y轴上，使用成本函数放在垂直z轴上。我们的图上的点将是成本函数的结果，使用我们的假设和那些特定的θ参数。下图描绘了这样的设置。

![img](bn9SyaDIEeav5QpTGIv-Pg_0d06dca3d225f3de8b5a4a7e92254153_Screenshot-2016-11-01-23.48.26.png?expiry=1543795200000&hmac=LCxVuGHteW6iXuI4phZkKO7edFtRTbW6w7mbz9K9KBQ.png)

我们知道，当我们的成本函数位于图中凹坑的最底部时，即当它的值是最小值时，我们已经成功了。红色箭头显示图表中的最小点。

我们这样做的方法是采用我们的成本函数的导数（一个函数的切线）。切线的斜率是该点的导数，它将为我们提供一个朝向的方向。我们在最陡下降的方向上降低成本函数。每个步骤的大小由参数α确定，该参数称为学习率。

例如，上图中每个“星”之间的距离表示由参数α确定的步长。较小的α将导致较小的步长，较大的α将导致较大的步长。采取步骤的方向由$J(\theta_0,\theta_1)$的偏导数确定。根据图表的开始位置，可能会在不同的点上结束。上图显示了两个不同的起点，最终出现在两个不同的地方。

梯度下降算法是：

重复直到收敛：

$\theta_j := \theta_j - \alpha \frac{\partial}{\partial \theta_j} J(\theta_0, \theta_1)$

哪里

j = 0,1表示特征索引号。

在每次迭代j中，应该同时更新参数 $\theta_1$, $\theta_2$,...,$\theta_n$。在$j^{(th)}$迭代中计算另一个参数之前更新特定参数将导致错误的实现。

#### Gradient Descent Intuition

In this video we explored the scenario where we used one parameter \theta_1θ1 and plotted its cost function to implement a gradient descent. Our formula for a single parameter was :

Repeat until convergence:

$\theta_1:=\theta_1-\alpha \frac{d}{d\theta_1} J(\theta_1)$

Regardless of the slope's sign for $\frac{d}{d\theta_1} J(\theta_1)$, $\theta_1$ eventually converges to its minimum value. The following graph shows that when the slope is negative, the value of $\theta_1$ increases and when it is positive, the value of $\theta_1$ decreases.

![img](SMSIxKGUEeav5QpTGIv-Pg_ad3404010579ac16068105cfdc8e950a_Screenshot-2016-11-03-00.05.06.png?expiry=1543795200000&hmac=qz6YC0unrvOGX4Z0Sz2taEOVFrCjq44zRDr92GgpE-g.png)

On a side note, we should adjust our parameter $\alpha$ to ensure that the gradient descent algorithm converges in a reasonable time. Failure to converge or too much time to obtain the minimum value imply that our step size is wrong.

![img](UJpiD6GWEeai9RKvXdDYag_3c3ad6625a2a4ec8456f421a2f4daf2e_Screenshot-2016-11-03-00.05.27.png?expiry=1543795200000&hmac=9gqguFi828OXMHtF2EO6Y0YnTWJt1rbPTblOqtNnVKg.png)

#### How does gradient descent converge with a fixed step size $\alpha$?

The intuition behind the convergence is that $\frac{d}{d\theta_1} J(\theta_1)$ approaches 0 as we approach the bottom of our convex function. At the minimum, the derivative will always be 0 and thus we get:

$\theta_1:=\theta_1-\alpha * 0$

![img](RDcJ-KGXEeaVChLw2Vaaug_cb782d34d272321e88f202940c36afe9_Screenshot-2016-11-03-00.06.00.png?expiry=1543795200000&hmac=fy8dCMVuN6kHPQi0AXJIj3nYssZCDRBie7KfBUatcQA.png)

#### 渐变下降直觉

在本视频中，我们探讨了使用一个参数$\theta_1$并绘制其成本函数以实现梯度下降的场景。我们的单个参数公式是：

重复直到收敛：

$\theta_1:=\theta_1-\alpha \frac{d}{d\theta_1} J(\theta_1)$

无论$\frac{d}{d\theta_1} J(\theta_1)$的斜率符号如何，$\theta_1$ 最终会收敛到其最小值。下图显示当斜率为负时，$\theta_1$ 的值增加，当它为正时，$\theta_1$ 的值减小。

![img](SMSIxKGUEeav5QpTGIv-Pg_ad3404010579ac16068105cfdc8e950a_Screenshot-2016-11-03-00.05.06.png?expiry=1543795200000&hmac=qz6YC0unrvOGX4Z0Sz2taEOVFrCjq44zRDr92GgpE-g.png)

另外，我们应该调整参数$\alpha$以确保梯度下降算法在合理的时间内收敛。没有收敛或太多时间来获得最小值意味着我们的步长是错误的。

![img](SMSIxKGUEeav5QpTGIv-Pg_ad3404010579ac16068105cfdc8e950a_Screenshot-2016-11-03-00.05.06.png?expiry=1543795200000&hmac=qz6YC0unrvOGX4Z0Sz2taEOVFrCjq44zRDr92GgpE-g.png)

梯度下降如何与固定步长$\alpha$收敛？

收敛背后的直觉是$\frac{d}{d\theta_1} J(\theta_1)$接近0时，我们接近凸函数的底部。至少，导数总是0，因此得到：

$\theta_1:=\theta_1-\alpha * 0$

![img](RDcJ-KGXEeaVChLw2Vaaug_cb782d34d272321e88f202940c36afe9_Screenshot-2016-11-03-00.06.00.png?expiry=1543795200000&hmac=fy8dCMVuN6kHPQi0AXJIj3nYssZCDRBie7KfBUatcQA.png)

#### Gradient Descent For Linear Regression

**Note:** [At 6:15 "h(x) = -900 - 0.1x" should be "h(x) = 900 - 0.1x"]

When specifically applied to the case of linear regression, a new form of the gradient descent equation can be derived. We can substitute our actual cost function and our actual hypothesis function and modify the equation to :

repeat until convergence: 
$$
\theta_0:=\theta_0-\alpha \frac{1}{m}\sum_{i=1}^{m}(h_0(x_i)-y_i)\\
\theta_1:=\theta_1-\alpha \frac{1}{m}\sum_{i=1}^{m}(h_0(x_i)-y_i)
$$
where m is the size of the training set, $\theta_0$ a constant that will be changing simultaneously with \theta_1θ1 and $x_{i}$, $y_{i}$ are values of the given training set (data).

Note that we have separated out the two cases for $\theta_j$ into separate equations for $\theta_0$ and $\theta_1$; and that for $\theta_1$ we are multiplying $x_{i}$ at the end due to the derivative. The following is a derivation of $\frac{\partial}{\partial \theta_j}J(\theta)$ for a single example :

![img](QFpooaaaEea7TQ6MHcgMPA_cc3c276df7991b1072b2afb142a78da1_Screenshot-2016-11-09-08.30.54.png?expiry=1543795200000&hmac=CjXGIj3j-xL5ILAOakC4qa_q_lAi8DJZJf92IjrIbQs.png)

The point of all this is that if we start with a guess for our hypothesis and then repeatedly apply these gradient descent equations, our hypothesis will become more and more accurate.

So, this is simply gradient descent on the original cost function J. This method looks at every example in the entire training set on every step, and is called **batch gradient descent**. Note that, while gradient descent can be susceptible to local minima in general, the optimization problem we have posed here for linear regression has only one global, and no other local, optima; thus gradient descent always converges (assuming the learning rate α is not too large) to the global minimum. Indeed, J is a convex quadratic function. Here is an example of gradient descent as it is run to minimize a quadratic function.

![img](xAQBlqaaEeawbAp5ByfpEg_24e9420f16fdd758ccb7097788f879e7_Screenshot-2016-11-09-08.36.49.png?expiry=1543795200000&hmac=-Ha3-BmgxowJXpq8qQvVOH9Or5glCvf77rBHeyQ1TS4.png)

The ellipses shown above are the contours of a quadratic function. Also shown is the trajectory taken by gradient descent, which was initialized at (48,30). The x’s in the figure (joined by straight lines) mark the successive values of $\theta$ that gradient descent went through as it converged to its minimum.

#### 线性回归的梯度下降

注意：[在6:15“h（x）= -900  -  0.1x”应为“h（x）= 900  -  0.1x”]

当具体应用于线性回归的情况时，可以导出梯度下降方程的新形式。我们可以替换我们的实际成本函数和我们的实际假设函数，并将等式修改为：

重复直到收敛：

$$
\theta_0:=\theta_0-\alpha \frac{1}{m}\sum_{i=1}^{m}(h_0(x_i)-y_i)\\
\theta_1:=\theta_1-\alpha \frac{1}{m}\sum_{i=1}^{m}(h_0(x_i)-y_i)
$$


其中m是训练集的大小，$\theta_0$ 将与$\theta_1$和$x_ {i}$同时改变的常数，$y_{i}$是给定训练集（数据）的值。

请注意，我们已将$\theta_j$的两个案例分离为$\theta_0$和$\theta_1$的单独等式;而对于$\theta_1$，由于导数，我们在末尾乘以$x_ {i}$。以下是单个示例的$\frac{\partial}{\partial \theta_j}J(\theta)$的派生：

![img](QFpooaaaEea7TQ6MHcgMPA_cc3c276df7991b1072b2afb142a78da1_Screenshot-2016-11-09-08.30.54.png?expiry=1543795200000&hmac=CjXGIj3j-xL5ILAOakC4qa_q_lAi8DJZJf92IjrIbQs.png)

所有这一切的要点是，如果我们从猜测开始，然后重复应用这些梯度下降方程，我们的假设将变得越来越准确。

因此，这只是原始成本函数J的梯度下降。该方法在每个步骤中查看整个训练集中的每个示例，并称为批量梯度下降。需要注意的是，虽然梯度下降一般可以对局部最小值敏感，但我们在线性回归中提出的优化问题只有一个全局，而没有其他局部最优;因此，梯度下降总是收敛（假设学习率$\alpha$不是太大）到全局最小值。实际上，J是凸二次函数。下面是梯度下降的示例，因为它是为了最小化二次函数而运行的。

![img](xAQBlqaaEeawbAp5ByfpEg_24e9420f16fdd758ccb7097788f879e7_Screenshot-2016-11-09-08.36.49.png?expiry=1543795200000&hmac=-Ha3-BmgxowJXpq8qQvVOH9Or5glCvf77rBHeyQ1TS4.png)

上面显示的椭圆是二次函数的轮廓。还示出了梯度下降所采用的轨迹，其在（48,30）处初始化。图中的x（由直线连接）标记渐变下降经历的连续值$\theta$，当它收敛到最小值时。