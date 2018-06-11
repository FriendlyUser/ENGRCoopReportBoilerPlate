% supercomputer exaflop per second
comperYear = 3.154e25
elecCostPerYear = 1.989e6
numComputations = zeros(1,480);
superComp = zeros(1,480);
superCompCostPower = zeros(1,480);
for w = 32:512
    numComputations(w-31)=2^w;
    superComp(w-31) = numComputations(w-31)/comperYear;
    superCompCostPower(w-31) = superComp(w-31)*elecCostPerYear;
end
wxe =32:1:512
%loglog(wxe,superComp)

%Quick computation for quantum computer
%gaming comp teraflop
gamingperYear = 3.154e17
gamingCompPower1 = zeros(1,480);
gamingComp1 = zeros(1,480);
quantCost = comperYear * [1000000 100000000000 100000000000000 1000000000000000];
quantComp1 = zeros(1,480);
quantCompPower1 = quantComp1;
quantComp2 = quantComp1;
quantCompPower2 = quantComp2;
quantComp3 = quantComp1;
quantComp4 = quantComp1;
quantCompPower3 = quantComp3;
quantCompPower4 = quantComp4;
for w = 32:512
    gamingComp1(w-31) = numComputations(w-31)/gamingperYear;
    gamingCompPower1(w-31) = gamingComp1(w-31)*elecCostPerYear;
    
    quantComp1(w-31) = numComputations(w-31)/quantCost(1);
    quantCompPower1(w-31) = quantComp1(w-31)*elecCostPerYear;
    
    quantComp2(w-31) = numComputations(w-31)/quantCost(2);
    quantCompPower2(w-31) = quantComp2(w-31)*elecCostPerYear;
    
    quantComp3(w-31) = numComputations(w-31)/quantCost(3);
    quantCompPower3(w-31) = quantComp3(w-31)*elecCostPerYear;
    
    quantComp4(w-31) = numComputations(w-31)/quantCost(4);
    quantCompPower4(w-31) = quantComp4(w-31)*elecCostPerYear;
end
figure
wxeb = []
yyaxis left
semilogy(log2(wxe), superComp,':b')                               %# plot on log2 x-scale

set(gca, 'XTickLabel',[])                      %# suppress current x-labels

xt = get(gca, 'XTick');
yl = get(gca, 'YLim');
str = cellstr( num2str(xt(:),'2^{%1.2g}') );      %# format x-ticks as 2^{xx}
hTxt = text(xt, yl(ones(size(xt))), str, ...   %# create text at same locations
    'Interpreter','tex', ...                   %# specify tex interpreter
    'VerticalAlignment','top', ...             %# v-align to be underneath
    'HorizontalAlignment','center');           %# h-aligh to be centered

title('Years for decryption vs key bit size')
xlabel('Length of bits(32 bit to 512 bit)')
ylabel('Year for brute force decryption')
yyaxis right

semilogy(log2(wxe), superCompCostPower,':r')
ylabel('Total Electricity Cost in $ CAD')
hold on 
 
 yyaxis right
 y2lims=ylim;  % return limits
% do whatever manipulations on those values wanted here
ylim([1e-50 1e150])
% %set(gcf,'visible','off')
% semilogy(log2(wxe), superCompCostPower,'-r')
 semilogy(log2(wxe), gamingCompPower1,'--r')
 semilogy(log2(wxe), quantCompPower4,'-r')
% %set(gcf,'visible','on')
% 
% 
% % Create second Y axes on the right.
% %a2 = axes('YAxisLocation', 'Right')
% % Hide second plot.
% %set(a2, 'color', 'none')
% %set(a2, 'XTick', [])
% % Set scala for second Y.
% %set(a2, 'YLim', [0 1000000000000000000000000000000000000000000000000000000000000000000000])
% 
 yyaxis left
% % Gaming comp
 semilogy(log2(wxe), gamingComp1,'--b')                               %# plot on log2 x-scale
% 
% %semilogy(log2(wxe), quantComp1)                               %# plot on log2 x-scale
% %semilogy(log2(wxe), quantComp2)                               %# plot on log2 x-scale
% %semilogy(log2(wxe), quantComp3)                               %# plot on log2 x-scale
 semilogy(log2(wxe), quantComp4,'-b')                               %# plot on log2 x-scale

%yyaxis right
%semilogy(log2(wxe), gamingCompPower1,'--r')
%semilogy(log2(wxe), quantCompPower4,':r')


%%% Draw the vertical lines at 2^5 2^6 2^7 and 2^8
%ystart = [10e -2 -3 -1 -2 -3];
%yend = [1 2 3 1 2 3];

%powersOf2 = [32, 64]
%hold on;
%for i = 1:4
%    semilogy([powersOf2(i) powersOf2(i)], [0 1e100]);
%end

lgd = legend({'1 exaflop','1 teraflop','1 peta exaflops','Cost for 1 exaflop','Cost for 1 teraflop','Cost for 1 peta teraflops'},'Location','northwest','NumColumns',2)
title(lgd,'Computer FLOPS and electricity Costs')

% print('epicPic.png','-dpng','-r300')