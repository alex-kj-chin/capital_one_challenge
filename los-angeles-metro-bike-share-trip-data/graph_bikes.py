import matplotlib.pyplot as plt
bike_mileages = [608.1654611361625, 574.7526842913712, 531.6639553229022, 497.0760048113524, 491.1617481624875, 485.9790475562513, 465.7056167108374, 464.9429375262222, 462.55441943039824, 459.9749045292864, 456.93690944989504, 455.29866918894004, 454.37087112332193, 453.14743686602714, 452.166972458869, 448.82399857073045, 448.6045267451896, 445.98470160152937, 445.43748065980697, 443.8117066090981, 443.79093197898845, 443.75844796771514, 441.8836550493935, 440.8055126868706, 440.16005799762866, 440.0920284753905, 440.011136555896, 438.6377801739594, 437.35559212138605, 435.81681388088316, 435.7423276069826, 433.52687263956665, 430.39612194181154, 429.14836308514805, 428.80026659413835, 427.8532938355294, 426.58482726697116, 425.73277783736694, 424.52068725067744, 423.2233343086517, 423.1308358592615, 422.31101436841044, 422.22125866632564, 420.98566124941203, 420.26383670421313, 417.96351677976753, 414.83153451192817, 414.1687815614666, 412.2190501288271, 411.2958502054336, 411.0729773706401, 410.091859221634, 409.91430283352395, 409.2688414785174, 407.4641563069536, 405.2505400767537, 403.55723979572366, 403.4100306778791, 403.0693706918107, 402.03962155712645, 401.26199655326485, 400.85172204128844, 400.5727195539313, 399.72807763610996, 399.05259490418877, 397.7173532037559, 396.07751835949693, 395.6959460044931, 394.6365211755298, 393.1530761366999, 391.7981837710071, 391.5809454361249, 391.39110486330446, 390.70757521641895, 390.34301376794434, 390.0161916508219, 389.8895023523093, 389.62144751728255, 389.18295900380576, 389.0177429377525, 388.78710437640575, 387.3532672174698, 387.01843148453617, 386.50994471992055, 386.1437084733028, 386.0258819891121, 385.8980847500805, 385.6470618252412, 385.361712424332, 384.75261063996584, 384.3946073109525, 384.38981684652896, 383.97435757538494, 382.98109013145967, 382.90883710035615, 382.5884739320974, 377.194087947012, 375.1541068187939, 374.3015596667416, 373.43317057707856, 372.5149945348173, 371.5395707994218, 371.264749332293, 370.37374707678816, 369.44056932295524, 368.93153195007676, 368.9283872994341, 368.4958198628657, 367.5641846993402, 366.8129038221074, 366.47341615041717, 366.28495170681697, 364.26323004372927, 364.06988010904973, 363.50949818040147, 363.3060050900707, 362.838742578027, 361.53710664413524, 361.13621937748434, 360.6044691541215, 360.2389370234728, 359.99343812866897, 359.57928133963105, 358.87096911135615, 358.4715355030077, 358.0960708048513, 357.96193335074116, 357.59327324754065, 357.3870909846273, 357.00001976022577, 356.78808794108784, 356.6464423388885, 355.027471862633, 355.02443982488575, 354.5464575200403, 353.9773769391738, 353.760493187833, 352.9415671762974, 352.7813041673587, 351.0228955870615, 350.6719940518181, 350.35457385915277, 350.31484087418727, 349.87456807624295, 349.83346540889073, 348.58281511793774, 348.45847808921104, 347.84733960516456, 347.65858268425944, 347.2581806315485, 347.17812298570453, 345.6907734312392, 345.1752823481383, 345.05241216454715, 344.68498879743754, 342.9941385003598, 342.98152715799756, 342.7024861531391, 342.68751041772333, 342.10927377364123, 341.3477252792085, 341.3159320523712, 340.57389535092585, 339.96955592328374, 339.40573790052747, 339.31789439358187, 339.2443429898505, 339.22281268265675, 339.0358132091487, 338.91891329675735, 338.69714196960217, 338.39398814756504, 337.90927082613314, 337.23621090214726, 337.21187030897715, 336.9671239626794, 336.60201836291117, 336.20961914177576, 335.692530542227, 335.24502007004423, 334.23702975850586, 333.93701057723564, 333.47460636070093, 333.44720725065997, 332.3636274214355, 332.2372451627601, 332.0599497291902, 331.95934023897746, 330.5478408910481, 330.17958669686914, 329.76550230698996, 329.6934773173075, 329.3863117630248, 328.85516567591316, 328.5406499985256, 328.4596563508611, 328.0432861358267, 328.0291890291857, 327.44339964205733, 326.30773132334235, 326.18268390151644, 325.63994920508713, 325.222436136993, 324.75594111924, 324.62535844217075, 324.623683405556, 324.5855210803746, 324.1821715014111, 324.08972642559394, 324.0070568137411, 323.58163930237816, 323.076981531238, 322.901940854332, 322.8328947376449, 322.774127041334, 322.58935186650206, 322.4087868510283, 322.3740451851103, 321.8098528010047, 321.5440930128763, 321.4173539736483, 321.3523159646873, 320.5515140372399, 320.42263688692617, 320.0799471981691, 320.0141482739372, 319.7497239314141, 319.68999896737614, 319.07818384926946, 318.9808256833038, 318.5483642227541, 318.33334857093826, 318.2318591992988, 317.7788892519965, 317.633590477493, 317.57126595829743, 317.31269049249147, 317.3000629571765, 316.7979524057089, 315.5404218738352, 315.4278112555144, 315.13174162025416, 314.8492264860579, 314.3256296567939, 313.66964046589436, 313.38038896838134, 313.18057420629356, 312.88474013619833, 312.7723949876962, 312.6074535364497, 312.00420301828467, 310.9460999044361, 310.3596406490573, 309.6790539383946, 309.4525706495922, 309.261068536969, 308.961055179864, 308.7712845801788, 307.98910622369124, 307.63126911391737, 307.50385289153223, 307.18545031232065, 307.01593345949686, 306.092803092406, 304.97439079325085, 304.8922145166691, 304.7382622421153, 304.51194485344087, 304.02119169081715, 303.85895342825273, 303.47425722259567, 303.17462851594587, 302.83109357442277, 302.7083846386916, 301.8478821832943, 301.8136353691011, 301.79920057255237, 301.6908721928724, 301.36342780585665, 301.3244560899663, 301.29978366679364, 300.64728167867594, 300.63605904063655, 300.5863362998955, 299.7930286234857, 299.15282851062693, 298.9434652721752, 298.91427236998953, 298.89747229454434, 298.72314939095594, 297.7484837950882, 297.0474236198293, 296.88783092581644, 296.734872092157, 296.482972871763, 296.16606307409126, 296.03811515496585, 295.7608560772347, 295.48465563622085, 294.87494217927514, 294.84352565003763, 294.8264458610167, 294.48806547347755, 294.2836081783199, 294.0594782368306, 293.9355718725102, 293.9316842767689, 293.52775792562767, 293.2977530663111, 292.987679149231, 292.8835333317365, 292.84835467522464, 292.7423935638475, 292.47004046726494, 292.46123497810873, 292.38223093617995, 291.62451680931036, 291.5697519383455, 291.2750148784881, 290.2384126301496, 290.1210502267338, 289.8170364718326, 289.7941720623945, 289.50530460633695, 289.43397002835445, 288.4022687012095, 288.3448483096494, 287.9914767507714, 287.96202169813637, 287.7999164267428, 287.7615593792298, 287.1576749465083, 287.10253686533366, 286.12353731170276, 285.9042999604519, 285.90369804081223, 285.7823374619056, 285.7172375998486, 285.6728644621468, 285.5818801472851, 285.3606447766727, 284.88816386829615, 284.8510337519802, 284.7702535030228, 284.44205564129135, 284.28072601438646, 284.0282420559307, 283.61300420797886, 283.313281322155, 283.1245919386684, 282.70461545668365, 282.14293953173893, 280.70323336294797, 280.56909080294423, 280.2022610783103, 280.15477994400214, 279.96499994710683, 279.76882068429427, 279.356950078339, 279.34662860349783, 279.02291328870814, 278.84254698392533, 277.9187980796162, 277.76699338454137, 277.0157625576297, 276.9217062474979, 276.6921598982048, 276.4975952449649, 276.27371447055583, 276.029223797136, 275.7651877004334, 275.75070917390644, 275.4741493191889, 275.09016073304826, 274.943489424804, 274.5637602043592, 274.55238823275386, 274.46027911998425, 274.25157713558934, 274.0415078591021, 273.8237189797042, 273.43054007407113, 272.73343730018706, 272.43425412599333, 272.14919244186734, 272.1018234929682, 271.7826619055828, 271.7599636665317, 271.22392207578696, 271.2151413074324, 270.69320040289045, 270.30184239489245, 269.86785329520274, 269.7258228490969, 269.71470121040034, 269.5852807340995, 269.09094009160276, 268.4212582196799, 267.66017069478346, 267.63750175981716, 267.2358367235271, 266.80311622844, 266.65349262921546, 266.45853827254666, 266.42837741361626, 266.3329945330291, 266.02017012888354, 266.0017110655258, 265.5011156442518, 265.0347197035307, 264.62626381807394, 264.6226173432706, 264.55833750696775, 264.20134407806785, 264.02429349433845, 263.85855070736113, 263.08523143145953, 262.69132869969275, 262.2208400913928, 261.92099457278584, 261.83064030313164, 261.7563027325194, 261.5368155289599, 260.62929521230416, 260.083532398006, 259.94237233074574, 259.71384812946815, 259.6792350801492, 259.6778534065561, 259.4866442091728, 259.2457379193166, 259.1132834716281, 258.98869641611077, 258.887372135177, 258.60723127781284, 257.8085466021032, 257.78888673957425, 257.1756770034506, 256.76340812166205, 256.72825990433836, 256.6052727703244, 256.2313594185915, 256.00143281010224, 255.97794128103976, 255.8803813157078, 255.4312018742499, 255.20878304037663, 255.101139475197, 254.98691775167956, 254.8078609554711, 254.55421310002168, 254.3747275506864, 254.20973988078237, 253.87106604904682, 253.33263023576174, 252.92418561115534, 252.65463020971504, 252.1840049586489, 252.08101408678743, 251.20668619796558, 250.7531750896776, 250.00008502884154, 249.5521300508256, 249.53043332189134, 248.7851754048457, 248.50982378834473, 248.43912750019024, 248.42076689408765, 248.3099961182314, 248.13159057808957, 247.73763000128753, 247.31110427621562, 246.67747946236247, 246.63236252734936, 246.59264166073052, 246.5122550423163, 246.51113147027277, 246.1657100038917, 246.16066982604232, 245.85741664270802, 245.36878536179873, 245.08969223718714, 245.08892783886762, 244.07635770355043, 243.91687608829457, 243.49594277172085, 243.4702527810945, 242.0049758686958, 241.3765655611864, 241.2406705376327, 241.0413470904352, 240.90337475023318, 240.79527005930757, 240.66731817709146, 240.6220122426056, 240.21694052181667, 240.0972178090456, 239.6316048117158, 239.19357719939984, 238.92332697659688, 238.8572709147088, 238.6057799256651, 238.23058494388528, 237.4971879166322, 237.43594257867548, 237.4304124894815, 236.8008241035813, 236.65877425882272, 236.36820641982902, 236.1749140931962, 235.9792941305281, 235.08510870500294, 234.8327088615428, 234.25257492766013, 233.9257525968259, 233.82985764256225, 233.30847930234899, 233.3017666870755, 232.5263616572775, 232.45221970067826, 232.38115405551184, 232.0432410142941, 231.64661898584768, 230.3004567835234, 230.2869421157488, 229.68440307548096, 228.99694735802908, 228.88810234841023, 228.5522459201683, 228.1931834261218, 227.55603610751194, 227.53497312921616, 227.3836014019802, 226.61494767441275, 226.32014636374132, 226.20922956934714, 225.87190261943468, 225.74282307556, 225.71453995021338, 225.29598347832587, 225.0980373613656, 224.3918201933306, 224.00282018350154, 223.680470781302, 223.63019692971642, 223.44329510439516, 222.84451610396442, 222.81164981111306, 222.4078828029188, 222.18777073560614, 221.87022978978143, 221.2396533599281, 221.08254644685093, 220.76920173338513, 220.66981221414892, 219.9576701799285, 219.452711741462, 218.75725123083473, 218.36730444246382, 217.57491216379026, 217.47671670066805, 217.40324365235895, 217.1534668250638, 217.05648339696364, 216.9985465658469, 216.8505485387076, 215.8965016347954, 215.8097539605653, 215.34852466969576, 214.5774834178768, 214.39500882109175, 214.0210559218074, 213.35324992941563, 212.6541634642201, 212.42195745501851, 212.25976853639997, 212.11181918129722, 211.7796445827889, 211.58584116831548, 211.1848566134003, 211.0243624493684, 210.37687447935784, 210.2849540021321, 210.28188133457783, 209.62069264974272, 209.30125112010077, 209.05564002440946, 208.71945406180384, 208.61871477581923, 208.35483296142172, 208.16653797561986, 207.90599530566584, 207.2616984620681, 206.09254748708705, 204.83562294713155, 204.77555569198861, 204.76400979796315, 203.82498137287897, 203.81359220218778, 203.4534598665145, 203.30672480423976, 203.3000150585668, 203.1819198867373, 202.40848671603072, 202.23952376243204, 202.12677621261878, 201.04806397148064, 200.97679583418926, 200.63519236693676, 200.46142779515688, 200.10100586909485, 200.08644845222852, 199.84255875887104, 199.2097771265335, 198.72740713439222, 198.2087326303955, 197.891695032276, 197.81585018442075, 197.66898412905508, 197.57284598740475, 197.555975599414, 197.10825025730182, 196.55962279198118, 195.57995966829185, 194.85667371815057, 194.66198870770563, 194.249806660073, 194.14988066557603, 193.86925848161005, 193.72343941055973, 192.92824346696202, 192.76658560598722, 192.53566907039493, 192.44874051881794, 192.0777277037476, 191.88812746619647, 191.19335376619586, 189.83155858903854, 189.0606896955032, 188.77084389682594, 188.02508966914917, 187.69632213623422, 187.57623051294334, 187.4983541271166, 186.42074365283463, 186.09769689916035, 185.6017834190801, 185.4269494467761, 185.37695424321552, 185.28113538601912, 184.2707501474982, 184.12309262680955, 184.00263492622216, 183.23473860336745, 182.84806315305283, 182.6721160692286, 182.6430074444854, 182.2745394502397, 182.09017941922457, 180.75051999019144, 180.25254744228923, 180.10874224245313, 179.8010487609165, 179.44674943882808, 179.42177251442521, 179.30730037716663, 179.02734074876145, 178.89293881188954, 177.76839759913452, 177.10245004910075, 176.89540411874577, 176.88220550809103, 175.09295638070407, 174.75302131525194, 174.13326890150068, 173.8155981113115, 173.42354712134903, 173.17005849306224, 171.0952918745709, 170.44950976808292, 170.09567393781282, 170.0589741936051, 169.03951336287372, 168.31274438544975, 167.9326678409387, 165.59695327860769, 165.29835106122937, 164.89317876740057, 164.57283923612079, 164.09536354270853, 163.96324935502585, 163.37750803486054, 163.07097963740165, 162.93196124848572, 162.10161248041277, 159.54379683584736, 157.97839749791757, 157.8549877369351, 157.68433169341458, 157.57746044635283, 157.55348413554123, 157.08428127299953, 156.96282143005783, 156.47653818245792, 155.44951538740375, 155.31412224246458, 154.86539127253997, 154.68540468450922, 154.62031042610866, 154.5652792164524, 153.8448920473001, 153.4525013223517, 152.6910884160933, 151.59515543536256, 151.28493406060525, 150.99458065009281, 149.6173048536962, 149.18721894363796, 148.77477318437252, 142.9288670947138, 142.52466852673422, 140.21530094322307, 139.37141822608848, 138.30580254461495, 137.05593746793392, 136.77036190217885, 135.56433386484747, 135.3916739657005, 135.16413364316412, 134.95235440669583, 134.92316999605495, 133.78716063311188, 133.6390387332948, 133.63874179945367, 133.00078541948284, 131.5116428820633, 128.09207353373287, 127.34988211948027, 122.67386246849169, 122.10183793366768, 119.44684040519662, 119.39976058583892, 118.2734470190657, 118.25223463439738, 117.94724908252212, 117.90521740788425, 112.7344863740154, 111.8637837689769, 110.93147970810716, 108.26043783642886, 104.51789525166849, 103.92289869052135, 92.67199624268187, 92.4286247140711, 90.78215633345037, 90.56026679683751, 85.16217648917691, 77.82630099733527, 63.68612781046504, 56.79472991271999, 16.108746314025662, 10.79118090402367]

plt.hist(bike_mileages, bins=50, facecolor='red')
plt.title("Bike Mileages")
plt.xlabel("Total Running Miles")
plt.ylabel("Number of Bikes")
fig = plt.gcf()
fig.savefig("bike_mileages.png")