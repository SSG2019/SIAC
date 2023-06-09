clc,clear all, close all
m = 1;% 返回矩阵F的行数
n = 20;% 返回矩阵B的行数
a=1;
Psum=20;
w=[0.0026 0.0036 0.0020 0.0020 0.0030 0.0022 0.0114 0.0035 0.0025 0.0022 0.0023 0.0019 0.0022 0.0033 0.0039 0.0059 0.0023 0.0030 0.0013 0.0023]';
% 构建黎曼流形优化问题
mainfold = multinomialfactory(n, m);% 根据优化问题中的约束条件选择Complex Stiefel流形
problem.M = mainfold;
% 定义优化
problem.cost = @(p) sum(w.*(ones(n,1)-exp(-a./p/Psum)));% @后面的括弧中是待优化的参数列表
problem.egrad = @(p) -Psum*w.*a.*exp(-a./p/Psum)./(Psum^2*p.^2);% 通过矩阵求导计算出价值函数的欧式梯度
[p, ~, ~, ~] = trustregions(problem);% 