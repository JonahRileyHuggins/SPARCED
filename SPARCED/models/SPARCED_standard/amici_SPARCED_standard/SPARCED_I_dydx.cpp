#include "amici/symbolic_functions.h"
#include "amici/defines.h"
#include "sundials/sundials_types.h"

#include <array>

#include "p.h"
#include "k.h"
#include "w.h"
#include "h.h"
#include "x.h"
#include "dwdx.h"

namespace amici {
namespace model_SPARCED_I {

void dydx_SPARCED_I(realtype *dydx, const realtype t, const realtype *x, const realtype *p, const realtype *k, const realtype *h, const realtype *w, const realtype *dwdx){
    dydx[0] = 1;
    dydx[959] = 1;
    dydx[1918] = 1;
    dydx[2877] = 1;
    dydx[3836] = 1;
    dydx[4795] = 1;
    dydx[5754] = 1;
    dydx[6713] = 1;
    dydx[7672] = 1;
    dydx[8631] = 1;
    dydx[9590] = 1;
    dydx[10549] = 1;
    dydx[11508] = 1;
    dydx[12467] = 1;
    dydx[13426] = 1;
    dydx[14385] = 1;
    dydx[15344] = 1;
    dydx[16303] = 1;
    dydx[17262] = 1;
    dydx[18221] = 1;
    dydx[19180] = 1;
    dydx[20139] = 1;
    dydx[21098] = 1;
    dydx[22057] = 1;
    dydx[23016] = 1;
    dydx[23975] = 1;
    dydx[24934] = 1;
    dydx[25893] = 1;
    dydx[26852] = 1;
    dydx[27811] = 1;
    dydx[28770] = 1;
    dydx[29729] = 1;
    dydx[30688] = 1;
    dydx[31647] = 1;
    dydx[32606] = 1;
    dydx[33565] = 1;
    dydx[34524] = 1;
    dydx[35483] = 1;
    dydx[36442] = 1;
    dydx[37401] = 1;
    dydx[38360] = 1;
    dydx[39319] = 1;
    dydx[40278] = 1;
    dydx[41237] = 1;
    dydx[42196] = 1;
    dydx[43155] = 1;
    dydx[44114] = 1;
    dydx[45073] = 1;
    dydx[46032] = 1;
    dydx[46991] = 1;
    dydx[47950] = 1;
    dydx[48909] = 1;
    dydx[49868] = 1;
    dydx[50827] = 1;
    dydx[51786] = 1;
    dydx[52745] = 1;
    dydx[53704] = 1;
    dydx[54663] = 1;
    dydx[55622] = 1;
    dydx[56581] = 1;
    dydx[57540] = 1;
    dydx[58499] = 1;
    dydx[59458] = 1;
    dydx[60417] = 1;
    dydx[61376] = 1;
    dydx[62335] = 1;
    dydx[63294] = 1;
    dydx[64253] = 1;
    dydx[65212] = 1;
    dydx[66171] = 1;
    dydx[67130] = 1;
    dydx[68089] = 1;
    dydx[69048] = 1;
    dydx[70007] = 1;
    dydx[70966] = 1;
    dydx[71925] = 1;
    dydx[72884] = 1;
    dydx[73843] = 1;
    dydx[74802] = 1;
    dydx[75761] = 1;
    dydx[76720] = 1;
    dydx[77679] = 1;
    dydx[78638] = 1;
    dydx[79597] = 1;
    dydx[80556] = 1;
    dydx[81515] = 1;
    dydx[82474] = 1;
    dydx[83433] = 1;
    dydx[84392] = 1;
    dydx[85351] = 1;
    dydx[86310] = 1;
    dydx[87269] = 1;
    dydx[88228] = 1;
    dydx[89187] = 1;
    dydx[90146] = 1;
    dydx[91105] = 1;
    dydx[92064] = 1;
    dydx[93023] = 1;
    dydx[93982] = 1;
    dydx[94941] = 1;
    dydx[95900] = 1;
    dydx[96859] = 1;
    dydx[97818] = 1;
    dydx[98777] = 1;
    dydx[99736] = 1;
    dydx[100695] = 1;
    dydx[101654] = 1;
    dydx[102613] = 1;
    dydx[103572] = 1;
    dydx[104531] = 1;
    dydx[105490] = 1;
    dydx[106449] = 1;
    dydx[107408] = 1;
    dydx[108367] = 1;
    dydx[109326] = 1;
    dydx[110285] = 1;
    dydx[111244] = 1;
    dydx[112203] = 1;
    dydx[113162] = 1;
    dydx[114121] = 1;
    dydx[115080] = 1;
    dydx[116039] = 1;
    dydx[116998] = 1;
    dydx[117957] = 1;
    dydx[118916] = 1;
    dydx[119875] = 1;
    dydx[120834] = 1;
    dydx[121793] = 1;
    dydx[122752] = 1;
    dydx[123711] = 1;
    dydx[124670] = 1;
    dydx[125629] = 1;
    dydx[126588] = 1;
    dydx[127547] = 1;
    dydx[128506] = 1;
    dydx[129465] = 1;
    dydx[130424] = 1;
    dydx[131383] = 1;
    dydx[132342] = 1;
    dydx[133301] = 1;
    dydx[134260] = 1;
    dydx[135219] = 1;
    dydx[136178] = 1;
    dydx[137137] = 1;
    dydx[138096] = 1;
    dydx[139055] = 1;
    dydx[140014] = 1;
    dydx[140973] = 1;
    dydx[141932] = 1;
    dydx[142891] = 1;
    dydx[143850] = 1;
    dydx[144809] = 1;
    dydx[145768] = 1;
    dydx[146727] = 1;
    dydx[147686] = 1;
    dydx[148645] = 1;
    dydx[149604] = 1;
    dydx[150563] = 1;
    dydx[151522] = 1;
    dydx[152481] = 1;
    dydx[153440] = 1;
    dydx[154399] = 1;
    dydx[155358] = 1;
    dydx[156317] = 1;
    dydx[157276] = 1;
    dydx[158235] = 1;
    dydx[159194] = 1;
    dydx[160153] = 1;
    dydx[161112] = 1;
    dydx[162071] = 1;
    dydx[163030] = 1;
    dydx[163989] = 1;
    dydx[164948] = 1;
    dydx[165907] = 1;
    dydx[166866] = 1;
    dydx[167825] = 1;
    dydx[168784] = 1;
    dydx[169743] = 1;
    dydx[170702] = 1;
    dydx[171661] = 1;
    dydx[172620] = 1;
    dydx[173579] = 1;
    dydx[174538] = 1;
    dydx[175497] = 1;
    dydx[176456] = 1;
    dydx[177415] = 1;
    dydx[178374] = 1;
    dydx[179333] = 1;
    dydx[180292] = 1;
    dydx[181251] = 1;
    dydx[182210] = 1;
    dydx[183169] = 1;
    dydx[184128] = 1;
    dydx[185087] = 1;
    dydx[186046] = 1;
    dydx[187005] = 1;
    dydx[187964] = 1;
    dydx[188923] = 1;
    dydx[189882] = 1;
    dydx[190841] = 1;
    dydx[191800] = 1;
    dydx[192759] = 1;
    dydx[193718] = 1;
    dydx[194677] = 1;
    dydx[195636] = 1;
    dydx[196595] = 1;
    dydx[197554] = 1;
    dydx[198513] = 1;
    dydx[199472] = 1;
    dydx[200431] = 1;
    dydx[201390] = 1;
    dydx[202349] = 1;
    dydx[203308] = 1;
    dydx[204267] = 1;
    dydx[205226] = 1;
    dydx[206185] = 1;
    dydx[207144] = 1;
    dydx[208103] = 1;
    dydx[209062] = 1;
    dydx[210021] = 1;
    dydx[210980] = 1;
    dydx[211939] = 1;
    dydx[212898] = 1;
    dydx[213857] = 1;
    dydx[214816] = 1;
    dydx[215775] = 1;
    dydx[216734] = 1;
    dydx[217693] = 1;
    dydx[218652] = 1;
    dydx[219611] = 1;
    dydx[220570] = 1;
    dydx[221529] = 1;
    dydx[222488] = 1;
    dydx[223447] = 1;
    dydx[224406] = 1;
    dydx[225365] = 1;
    dydx[226324] = 1;
    dydx[227283] = 1;
    dydx[228242] = 1;
    dydx[229201] = 1;
    dydx[230160] = 1;
    dydx[231119] = 1;
    dydx[232078] = 1;
    dydx[233037] = 1;
    dydx[233996] = 1;
    dydx[234955] = 1;
    dydx[235914] = 1;
    dydx[236873] = 1;
    dydx[237832] = 1;
    dydx[238791] = 1;
    dydx[239750] = 1;
    dydx[240709] = 1;
    dydx[241668] = 1;
    dydx[242627] = 1;
    dydx[243586] = 1;
    dydx[244545] = 1;
    dydx[245504] = 1;
    dydx[246463] = 1;
    dydx[247422] = 1;
    dydx[248381] = 1;
    dydx[249340] = 1;
    dydx[250299] = 1;
    dydx[251258] = 1;
    dydx[252217] = 1;
    dydx[253176] = 1;
    dydx[254135] = 1;
    dydx[255094] = 1;
    dydx[256053] = 1;
    dydx[257012] = 1;
    dydx[257971] = 1;
    dydx[258930] = 1;
    dydx[259889] = 1;
    dydx[260848] = 1;
    dydx[261807] = 1;
    dydx[262766] = 1;
    dydx[263725] = 1;
    dydx[264684] = 1;
    dydx[265643] = 1;
    dydx[266602] = 1;
    dydx[267561] = 1;
    dydx[268520] = 1;
    dydx[269479] = 1;
    dydx[270438] = 1;
    dydx[271397] = 1;
    dydx[272356] = 1;
    dydx[273315] = 1;
    dydx[274274] = 1;
    dydx[275233] = 1;
    dydx[276192] = 1;
    dydx[277151] = 1;
    dydx[278110] = 1;
    dydx[279069] = 1;
    dydx[280028] = 1;
    dydx[280987] = 1;
    dydx[281946] = 1;
    dydx[282905] = 1;
    dydx[283864] = 1;
    dydx[284823] = 1;
    dydx[285782] = 1;
    dydx[286741] = 1;
    dydx[287700] = 1;
    dydx[288659] = 1;
    dydx[289618] = 1;
    dydx[290577] = 1;
    dydx[291536] = 1;
    dydx[292495] = 1;
    dydx[293454] = 1;
    dydx[294413] = 1;
    dydx[295372] = 1;
    dydx[296331] = 1;
    dydx[297290] = 1;
    dydx[298249] = 1;
    dydx[299208] = 1;
    dydx[300167] = 1;
    dydx[301126] = 1;
    dydx[302085] = 1;
    dydx[303044] = 1;
    dydx[304003] = 1;
    dydx[304962] = 1;
    dydx[305921] = 1;
    dydx[306880] = 1;
    dydx[307839] = 1;
    dydx[308798] = 1;
    dydx[309757] = 1;
    dydx[310716] = 1;
    dydx[311675] = 1;
    dydx[312634] = 1;
    dydx[313593] = 1;
    dydx[314552] = 1;
    dydx[315511] = 1;
    dydx[316470] = 1;
    dydx[317429] = 1;
    dydx[318388] = 1;
    dydx[319347] = 1;
    dydx[320306] = 1;
    dydx[321265] = 1;
    dydx[322224] = 1;
    dydx[323183] = 1;
    dydx[324142] = 1;
    dydx[325101] = 1;
    dydx[326060] = 1;
    dydx[327019] = 1;
    dydx[327978] = 1;
    dydx[328937] = 1;
    dydx[329896] = 1;
    dydx[330855] = 1;
    dydx[331814] = 1;
    dydx[332773] = 1;
    dydx[333732] = 1;
    dydx[334691] = 1;
    dydx[335650] = 1;
    dydx[336609] = 1;
    dydx[337568] = 1;
    dydx[338527] = 1;
    dydx[339486] = 1;
    dydx[340445] = 1;
    dydx[341404] = 1;
    dydx[342363] = 1;
    dydx[343322] = 1;
    dydx[344281] = 1;
    dydx[345240] = 1;
    dydx[346199] = 1;
    dydx[347158] = 1;
    dydx[348117] = 1;
    dydx[349076] = 1;
    dydx[350035] = 1;
    dydx[350994] = 1;
    dydx[351953] = 1;
    dydx[352912] = 1;
    dydx[353871] = 1;
    dydx[354830] = 1;
    dydx[355789] = 1;
    dydx[356748] = 1;
    dydx[357707] = 1;
    dydx[358666] = 1;
    dydx[359625] = 1;
    dydx[360584] = 1;
    dydx[361543] = 1;
    dydx[362502] = 1;
    dydx[363461] = 1;
    dydx[364420] = 1;
    dydx[365379] = 1;
    dydx[366338] = 1;
    dydx[367297] = 1;
    dydx[368256] = 1;
    dydx[369215] = 1;
    dydx[370174] = 1;
    dydx[371133] = 1;
    dydx[372092] = 1;
    dydx[373051] = 1;
    dydx[374010] = 1;
    dydx[374969] = 1;
    dydx[375928] = 1;
    dydx[376887] = 1;
    dydx[377846] = 1;
    dydx[378805] = 1;
    dydx[379764] = 1;
    dydx[380723] = 1;
    dydx[381682] = 1;
    dydx[382641] = 1;
    dydx[383600] = 1;
    dydx[384559] = 1;
    dydx[385518] = 1;
    dydx[386477] = 1;
    dydx[387436] = 1;
    dydx[388395] = 1;
    dydx[389354] = 1;
    dydx[390313] = 1;
    dydx[391272] = 1;
    dydx[392231] = 1;
    dydx[393190] = 1;
    dydx[394149] = 1;
    dydx[395108] = 1;
    dydx[396067] = 1;
    dydx[397026] = 1;
    dydx[397985] = 1;
    dydx[398944] = 1;
    dydx[399903] = 1;
    dydx[400862] = 1;
    dydx[401821] = 1;
    dydx[402780] = 1;
    dydx[403739] = 1;
    dydx[404698] = 1;
    dydx[405657] = 1;
    dydx[406616] = 1;
    dydx[407575] = 1;
    dydx[408534] = 1;
    dydx[409493] = 1;
    dydx[410452] = 1;
    dydx[411411] = 1;
    dydx[412370] = 1;
    dydx[413329] = 1;
    dydx[414288] = 1;
    dydx[415247] = 1;
    dydx[416206] = 1;
    dydx[417165] = 1;
    dydx[418124] = 1;
    dydx[419083] = 1;
    dydx[420042] = 1;
    dydx[421001] = 1;
    dydx[421960] = 1;
    dydx[422919] = 1;
    dydx[423878] = 1;
    dydx[424837] = 1;
    dydx[425796] = 1;
    dydx[426755] = 1;
    dydx[427714] = 1;
    dydx[428673] = 1;
    dydx[429632] = 1;
    dydx[430591] = 1;
    dydx[431550] = 1;
    dydx[432509] = 1;
    dydx[433468] = 1;
    dydx[434427] = 1;
    dydx[435386] = 1;
    dydx[436345] = 1;
    dydx[437304] = 1;
    dydx[438263] = 1;
    dydx[439222] = 1;
    dydx[440181] = 1;
    dydx[441140] = 1;
    dydx[442099] = 1;
    dydx[443058] = 1;
    dydx[444017] = 1;
    dydx[444976] = 1;
    dydx[445935] = 1;
    dydx[446894] = 1;
    dydx[447853] = 1;
    dydx[448812] = 1;
    dydx[449771] = 1;
    dydx[450730] = 1;
    dydx[451689] = 1;
    dydx[452648] = 1;
    dydx[453607] = 1;
    dydx[454566] = 1;
    dydx[455525] = 1;
    dydx[456484] = 1;
    dydx[457443] = 1;
    dydx[458402] = 1;
    dydx[459361] = 1;
    dydx[460320] = 1;
    dydx[461279] = 1;
    dydx[462238] = 1;
    dydx[463197] = 1;
    dydx[464156] = 1;
    dydx[465115] = 1;
    dydx[466074] = 1;
    dydx[467033] = 1;
    dydx[467992] = 1;
    dydx[468951] = 1;
    dydx[469910] = 1;
    dydx[470869] = 1;
    dydx[471828] = 1;
    dydx[472787] = 1;
    dydx[473746] = 1;
    dydx[474705] = 1;
    dydx[475664] = 1;
    dydx[476623] = 1;
    dydx[477582] = 1;
    dydx[478541] = 1;
    dydx[479500] = 1;
    dydx[480459] = 1;
    dydx[481418] = 1;
    dydx[482377] = 1;
    dydx[483336] = 1;
    dydx[484295] = 1;
    dydx[485254] = 1;
    dydx[486213] = 1;
    dydx[487172] = 1;
    dydx[488131] = 1;
    dydx[489090] = 1;
    dydx[490049] = 1;
    dydx[491008] = 1;
    dydx[491967] = 1;
    dydx[492926] = 1;
    dydx[493885] = 1;
    dydx[494844] = 1;
    dydx[495803] = 1;
    dydx[496762] = 1;
    dydx[497721] = 1;
    dydx[498680] = 1;
    dydx[499639] = 1;
    dydx[500598] = 1;
    dydx[501557] = 1;
    dydx[502516] = 1;
    dydx[503475] = 1;
    dydx[504434] = 1;
    dydx[505393] = 1;
    dydx[506352] = 1;
    dydx[507311] = 1;
    dydx[508270] = 1;
    dydx[509229] = 1;
    dydx[510188] = 1;
    dydx[511147] = 1;
    dydx[512106] = 1;
    dydx[513065] = 1;
    dydx[514024] = 1;
    dydx[514983] = 1;
    dydx[515942] = 1;
    dydx[516901] = 1;
    dydx[517860] = 1;
    dydx[518819] = 1;
    dydx[519778] = 1;
    dydx[520737] = 1;
    dydx[521696] = 1;
    dydx[522655] = 1;
    dydx[523614] = 1;
    dydx[524573] = 1;
    dydx[525532] = 1;
    dydx[526491] = 1;
    dydx[527450] = 1;
    dydx[528409] = 1;
    dydx[529368] = 1;
    dydx[530327] = 1;
    dydx[531286] = 1;
    dydx[532245] = 1;
    dydx[533204] = 1;
    dydx[534163] = 1;
    dydx[535122] = 1;
    dydx[536081] = 1;
    dydx[537040] = 1;
    dydx[537999] = 1;
    dydx[538958] = 1;
    dydx[539917] = 1;
    dydx[540876] = 1;
    dydx[541835] = 1;
    dydx[542794] = 1;
    dydx[543753] = 1;
    dydx[544712] = 1;
    dydx[545671] = 1;
    dydx[546630] = 1;
    dydx[547589] = 1;
    dydx[548548] = 1;
    dydx[549507] = 1;
    dydx[550466] = 1;
    dydx[551425] = 1;
    dydx[552384] = 1;
    dydx[553343] = 1;
    dydx[554302] = 1;
    dydx[555261] = 1;
    dydx[556220] = 1;
    dydx[557179] = 1;
    dydx[558138] = 1;
    dydx[559097] = 1;
    dydx[560056] = 1;
    dydx[561015] = 1;
    dydx[561974] = 1;
    dydx[562933] = 1;
    dydx[563892] = 1;
    dydx[564851] = 1;
    dydx[565810] = 1;
    dydx[566769] = 1;
    dydx[567728] = 1;
    dydx[568687] = 1;
    dydx[569646] = 1;
    dydx[570605] = 1;
    dydx[571564] = 1;
    dydx[572523] = 1;
    dydx[573482] = 1;
    dydx[574441] = 1;
    dydx[575400] = 1;
    dydx[576359] = 1;
    dydx[577318] = 1;
    dydx[578277] = 1;
    dydx[579236] = 1;
    dydx[580195] = 1;
    dydx[581154] = 1;
    dydx[582113] = 1;
    dydx[583072] = 1;
    dydx[584031] = 1;
    dydx[584990] = 1;
    dydx[585949] = 1;
    dydx[586908] = 1;
    dydx[587867] = 1;
    dydx[588826] = 1;
    dydx[589785] = 1;
    dydx[590744] = 1;
    dydx[591703] = 1;
    dydx[592662] = 1;
    dydx[593621] = 1;
    dydx[594580] = 1;
    dydx[595539] = 1;
    dydx[596498] = 1;
    dydx[597457] = 1;
    dydx[598416] = 1;
    dydx[599375] = 1;
    dydx[600334] = 1;
    dydx[601293] = 1;
    dydx[602252] = 1;
    dydx[603211] = 1;
    dydx[604170] = 1;
    dydx[605129] = 1;
    dydx[606088] = 1;
    dydx[607047] = 1;
    dydx[608006] = 1;
    dydx[608965] = 1;
    dydx[609924] = 1;
    dydx[610883] = 1;
    dydx[611842] = 1;
    dydx[612801] = 1;
    dydx[613760] = 1;
    dydx[614719] = 1;
    dydx[615678] = 1;
    dydx[616637] = 1;
    dydx[617596] = 1;
    dydx[618555] = 1;
    dydx[619514] = 1;
    dydx[620473] = 1;
    dydx[621432] = 1;
    dydx[622391] = 1;
    dydx[623350] = 1;
    dydx[624309] = 1;
    dydx[625268] = 1;
    dydx[626227] = 1;
    dydx[627186] = 1;
    dydx[628145] = 1;
    dydx[629104] = 1;
    dydx[630063] = 1;
    dydx[631022] = 1;
    dydx[631981] = 1;
    dydx[632940] = 1;
    dydx[633899] = 1;
    dydx[634858] = 1;
    dydx[635817] = 1;
    dydx[636776] = 1;
    dydx[637735] = 1;
    dydx[638694] = 1;
    dydx[639653] = 1;
    dydx[640612] = 1;
    dydx[641571] = 1;
    dydx[642530] = 1;
    dydx[643489] = 1;
    dydx[644448] = 1;
    dydx[645407] = 1;
    dydx[646366] = 1;
    dydx[647325] = 1;
    dydx[648284] = 1;
    dydx[649243] = 1;
    dydx[650202] = 1;
    dydx[651161] = 1;
    dydx[652120] = 1;
    dydx[653079] = 1;
    dydx[654038] = 1;
    dydx[654997] = 1;
    dydx[655956] = 1;
    dydx[656915] = 1;
    dydx[657874] = 1;
    dydx[658833] = 1;
    dydx[659792] = 1;
    dydx[660751] = 1;
    dydx[661710] = 1;
    dydx[662669] = 1;
    dydx[663628] = 1;
    dydx[664587] = 1;
    dydx[665546] = 1;
    dydx[666505] = 1;
    dydx[667464] = 1;
    dydx[668423] = 1;
    dydx[669382] = 1;
    dydx[670341] = 1;
    dydx[671300] = 1;
    dydx[672259] = 1;
    dydx[673218] = 1;
    dydx[674177] = 1;
    dydx[675136] = 1;
    dydx[676095] = 1;
    dydx[677054] = 1;
    dydx[678013] = 1;
    dydx[678972] = 1;
    dydx[679931] = 1;
    dydx[680890] = 1;
    dydx[681849] = 1;
    dydx[682808] = 1;
    dydx[683767] = 1;
    dydx[684726] = 1;
    dydx[685685] = 1;
    dydx[686644] = 1;
    dydx[687603] = 1;
    dydx[688562] = 1;
    dydx[689521] = 1;
    dydx[690480] = 1;
    dydx[691439] = 1;
    dydx[692398] = 1;
    dydx[693357] = 1;
    dydx[694316] = 1;
    dydx[695275] = 1;
    dydx[696234] = 1;
    dydx[697193] = 1;
    dydx[698152] = 1;
    dydx[699111] = 1;
    dydx[700070] = 1;
    dydx[701029] = 1;
    dydx[701988] = 1;
    dydx[702947] = 1;
    dydx[703906] = 1;
    dydx[704865] = 1;
    dydx[705824] = 1;
    dydx[706783] = 1;
    dydx[707742] = 1;
    dydx[708701] = 1;
    dydx[709660] = 1;
    dydx[710619] = 1;
    dydx[711578] = 1;
    dydx[712537] = 1;
    dydx[713496] = 1;
    dydx[714455] = 1;
    dydx[715414] = 1;
    dydx[716373] = 1;
    dydx[717332] = 1;
    dydx[718291] = 1;
    dydx[719250] = 1;
    dydx[720209] = 1;
    dydx[721168] = 1;
    dydx[722127] = 1;
    dydx[723086] = 1;
    dydx[724045] = 1;
    dydx[725004] = 1;
    dydx[725963] = 1;
    dydx[726922] = 1;
    dydx[727881] = 1;
    dydx[728840] = 1;
    dydx[729799] = 1;
    dydx[730758] = 1;
    dydx[731717] = 1;
    dydx[732676] = 1;
    dydx[733635] = 1;
    dydx[734594] = 1;
    dydx[735553] = 1;
    dydx[736512] = 1;
    dydx[737471] = 1;
    dydx[738430] = 1;
    dydx[739389] = 1;
    dydx[740348] = 1;
    dydx[741307] = 1;
    dydx[742266] = 1;
    dydx[743225] = 1;
    dydx[744184] = 1;
    dydx[745143] = 1;
    dydx[746102] = 1;
    dydx[747061] = 1;
    dydx[748020] = 1;
    dydx[748979] = 1;
    dydx[749938] = 1;
    dydx[750897] = 1;
    dydx[751856] = 1;
    dydx[752815] = 1;
    dydx[753774] = 1;
    dydx[754733] = 1;
    dydx[755692] = 1;
    dydx[756651] = 1;
    dydx[757610] = 1;
    dydx[758569] = 1;
    dydx[759528] = 1;
    dydx[760487] = 1;
    dydx[761446] = 1;
    dydx[762405] = 1;
    dydx[763364] = 1;
    dydx[764323] = 1;
    dydx[765282] = 1;
    dydx[766241] = 1;
    dydx[767200] = 1;
    dydx[768159] = 1;
    dydx[769118] = 1;
    dydx[770077] = 1;
    dydx[771036] = 1;
}

} // namespace amici
} // namespace model_SPARCED_I