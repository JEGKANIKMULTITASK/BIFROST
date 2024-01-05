"""
This McStasScript file was generated from a
McStas instrument file. It was checked after 
by Daniel Lomholt Christensen.
"""
from mcstasscript.interface import instr, plotter, functions


elementLength1_part_1 = [0.5   , 0.5   , 0.5   , 0.5   , 0.5   , 0.5   , 0.5   , 0.5   ,
       0.5   , 0.5   , 0.5   , 0.5   , 0.5   , 0.5   , 0.5   , 0.5   ,
       0.5   , 0.5   , 0.5   , 0.5   , 0.5   , 0.5   , 0.5   , 0.5   ,
       0.5   , 0.5   , 0.5   , 0.5   , 0.5   , 0.5   , 0.5   , 0.5   ,
       0.5   , 0.5   , 0.5   , 0.5   , 0.0158, 0.4842, 0.5   , 0.5   ,
       0.1432]

mValues1vertical_part_1 = [1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5,
       1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 2. , 2. , 2. , 2. ,
       2. , 2. , 2. , 2. , 2. , 2. , 2. , 2. , 2. , 2. , 0. , 2. , 2. ,
       2.5, 2.5]

mValues1horizontal_part_1 =[1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5,
       1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5,
       1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 2. , 2. , 2. , 2. , 0. , 2. , 2.5,
       2.5, 2.5] 

elementLength1_part_2 = [0.3168, 0.5   , 0.4632]

mValues1vertical_part_2 = [2.5, 3. , 3. ]

mValues1horizontal_part_2 = [2.5, 3. , 3. ]

elementLength1_part_3 = [0.0596, 0.5   ]

mValues1vertical_part_3 = [3. , 3.5]

mValues1horizontal_part_3 = [3., 3.]

elementLength1_part_4 = [0.0667, 0.5   , 0.0047]

mValues1vertical_part_4 = [3.5, 3.5, 3.5]

mValues1horizontal_part_4 = [3. , 3.5, 3.5]

elementLength6S = [0.48844444, 0.48844444, 0.48844444, 0.48844444, 0.48844444,
       0.48844444, 0.48844444, 0.06121889, 0.02349   , 0.40373556,
       0.07626444, 0.015     , 0.39671   ]

mValues6verticalS = [3.5, 3.5, 3. , 3. , 2.5, 2.5, 2.5, 2.5, 0. , 2. , 2. , 0. , 2. ]
mValues6horizontalS =[3. , 3. , 2.5, 2.5, 2.5, 2. , 1.5, 1.5, 0. , 1.5, 1.5, 0. , 1.5]
elementLength3S = [0.5   , 0.5   , 0.5   , 0.5   , 0.5   , 0.5   , 0.5   , 0.02  ,
       0.48  , 0.5   , 0.5   , 0.5   , 0.5   , 0.5   , 0.5   , 0.5   ,
       0.5   , 0.5   , 0.5   , 0.5   , 0.5   , 0.5   , 0.5   , 0.5   ,
       0.5   , 0.5   , 0.5   , 0.5   , 0.5   , 0.5   , 0.5   , 0.5   ,
       0.5   , 0.5   , 0.5   , 0.5   , 0.5   , 0.5   , 0.5   , 0.5   ,
       0.5   , 0.5   , 0.5   , 0.5   , 0.5   , 0.5   , 0.5   , 0.5   ,
       0.5   , 0.5   , 0.4288]

mValues3verticalS = [2. , 2. , 2. , 2. , 2. , 2. , 2. , 0. , 2. , 2. , 2. , 2. , 2. ,
       2. , 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5,
       1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5,
      1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5]

mValues3horizontalS = [2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 0. , 2. , 2. , 2. , 2. , 2. ,
       2. , 2. , 2. , 2. , 2. , 2. , 2. , 2. , 2. , 2. , 2. , 1.5, 1.5,
       1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5,
       1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5]





EGCESE = instr.McStas_instr("EGCESE_generated")

 
C_mValues1vertical_part_1 = EGCESE.add_declare_var("double", "C_mValues1vertical_part_1", value= mValues1vertical_part_1, array=len(mValues1vertical_part_1))
C_elementLength1_part_1 = EGCESE.add_declare_var("double", "C_elementLength1_part_1", value=elementLength1_part_1 , array=len(elementLength1_part_1))
C_mValues1horizontal_part_1 = EGCESE.add_declare_var("double", "C_mValues1horizontal_part_1", value=mValues1horizontal_part_1 , array=len(mValues1horizontal_part_1))


C_elementLength1_part_2 = EGCESE.add_declare_var("double", "C_elementLength1_part_2", value=elementLength1_part_2 , array=len(elementLength1_part_2))
C_mValues1vertical_part_2 = EGCESE.add_declare_var("double", "C_mValues1vertical_part_2", value=mValues1vertical_part_2 , array=len(mValues1vertical_part_2))
C_mValues1horizontal_part_2 = EGCESE.add_declare_var("double", "C_mValues1horizontal_part_2", value=mValues1horizontal_part_2 , array=len(mValues1horizontal_part_2))


C_elementLength1_part_3 = EGCESE.add_declare_var("double", "C_elementLength1_part_3", value=elementLength1_part_3 , array=len(elementLength1_part_3))
C_mValues1vertical_part_3 = EGCESE.add_declare_var("double", "C_mValues1vertical_part_3", value=mValues1vertical_part_3 , array=len(mValues1vertical_part_3))
C_mValues1horizontal_part_3 = EGCESE.add_declare_var("double", "C_mValues1horizontal_part_3", value=mValues1horizontal_part_3 , array=len(mValues1horizontal_part_3))


C_elementLength1_part_4 = EGCESE.add_declare_var("double", "C_elementLength1_part_4", value=elementLength1_part_4 , array=len(elementLength1_part_4))
C_mValues1vertical_part_4 = EGCESE.add_declare_var("double", "C_mValues1vertical_part_4", value=mValues1vertical_part_4 , array=len(mValues1vertical_part_4))
C_mValues1horizontal_part_4 = EGCESE.add_declare_var("double", "C_mValues1horizontal_part_4", value=mValues1horizontal_part_4 , array=len(mValues1horizontal_part_4))


C_elementLength6S = EGCESE.add_declare_var("double", "C_elementLength6S", value=elementLength6S , array=len(elementLength6S))
C_mValues6verticalS = EGCESE.add_declare_var("double", "C_mValues6verticalS", value=mValues6verticalS , array=len(mValues6verticalS))
C_mValues6horizontalS = EGCESE.add_declare_var("double", "C_mValues6horizontalS", value=mValues6horizontalS , array=len(mValues6horizontalS))


C_elementLength3S = EGCESE.add_declare_var("double", "C_elementLength3S", value=elementLength3S, array=len(elementLength3S))
C_mValues3verticalS = EGCESE.add_declare_var("double", "C_mValues3verticalS", value=mValues3verticalS , array=len(mValues3verticalS))
C_mValues3horizontalS = EGCESE.add_declare_var("double", "C_mValues3horizontalS", value=mValues3horizontalS , array=len(mValues3horizontalS))












                                                       
                                                       
                                                       
                                                       
EGCESE.add_parameter("double", "WaveMin", value=1.0)
EGCESE.add_parameter("double", "WaveMax", value=10.0)
EGCESE.add_parameter("double", "E_0", value=4.0)
EGCESE.add_parameter("double", "L_0", value=0.0)
EGCESE.add_parameter("double", "chopPulseOpening", value=0.004)
EGCESE.add_parameter("double", "DivSlit0_width", value=0.1)
EGCESE.add_parameter("double", "DivSlit1_width", value=0.1)
EGCESE.add_parameter("double", "DivSlit2_width", value=0.1)
EGCESE.add_parameter("double", "DivSlit3_width", value=0.1)
EGCESE.add_parameter("double", "Npulse", value=1.0)
EGCESE.add_parameter("int", "print", value=0)
EGCESE.add_parameter("int", "makeVirtualSource", value=0)
EGCESE.add_parameter("int", "printMValues", value=0)
EGCESE.add_parameter("double", "power", value=2.0)
EGCESE.add_parameter("double", "BWopen", value=161.0)
EGCESE.add_declare_var("double", "chopPulseFrequencyOrder", value=14.0)
EGCESE.add_declare_var("double", "sampleSizeX", value=0.01)
EGCESE.add_declare_var("double", "sampleSizeY", value=0.01)
EGCESE.add_declare_var("double", "chopBWPos", value=78.0)
EGCESE.add_declare_var("double", "PscOff", value=0.0306)
EGCESE.add_declare_var("double", "discD", value=0.04)
EGCESE.add_declare_var("double", "monigap_length", value=0.02)
EGCESE.add_declare_var("double", "FOCopen1", value=38.26)
EGCESE.add_declare_var("double", "FOCopen2", value=52.01)
EGCESE.add_declare_var("double", "ChopTransBunker", value=0.00331)
EGCESE.add_declare_var("double", "ChopTransE2", value=0.00423)
EGCESE.add_declare_var("double", "x_div")
EGCESE.add_declare_var("double", "y_div")
EGCESE.add_declare_var("int", "flag")
EGCESE.add_declare_var("double", "u", value=1e-05)
EGCESE.add_declare_var("double", "lambda_0")
EGCESE.add_declare_var("double", "lambda_1")
EGCESE.add_declare_var("double", "v_0")
EGCESE.add_declare_var("double", "v_1")
EGCESE.add_declare_var("double", "InstLength")
EGCESE.add_declare_var("double", "chopPulseOffset")
EGCESE.add_declare_var("double", "chopPulsePhaseOffset")
EGCESE.add_declare_var("double", "chopPulseDist")
EGCESE.add_declare_var("double", "chopPulseOpen")
EGCESE.add_declare_var("double", "chopPulse2PhaseOffset")
EGCESE.add_declare_var("double", "chopFrameOverlap1Offset")
EGCESE.add_declare_var("double", "chopFrameOverlap1PhaseOffset")
EGCESE.add_declare_var("double", "chopFrameOverlap1Open")
EGCESE.add_declare_var("double", "chopFrameOverlap2Offset")
EGCESE.add_declare_var("double", "chopFrameOverlap2PhaseOffset")
EGCESE.add_declare_var("double", "chopFrameOverlap2Open")
EGCESE.add_declare_var("double", "chopBWOffset")
EGCESE.add_declare_var("double", "chopBWPhaseOffset")
EGCESE.add_declare_var("double", "chopBWOpen")
EGCESE.add_declare_var("double", "t_samp_center")
EGCESE.add_declare_var("double", "t_samp_0")
EGCESE.add_declare_var("double", "t_samp_1")
EGCESE.add_declare_var("double", "chopBW_t0")
EGCESE.add_declare_var("double", "chopBW_t1")
EGCESE.add_declare_var("double", "PulseHighFluxOffset")
EGCESE.add_declare_var("double", "WavelengthBand")
EGCESE.add_declare_var("double", "ModPulseLengthHighF")
EGCESE.add_declare_var("double", "chopPulsePossibleOpening")
EGCESE.add_declare_var("double", "sample_dist", value=0.5)
EGCESE.add_declare_var("double", "startXposition_straight", value=49.303484)
EGCESE.add_declare_var("double", "length5", value=17.9958)
EGCESE.add_declare_var("double", "benderStartXposition", value=24.376254)
EGCESE.add_declare_var("double", "length2", value=90.0)
EGCESE.add_declare_var("double", "length1", value=22.1142)
EGCESE.add_declare_var("double", "Linx1", value=24.364542)
EGCESE.add_declare_var("double", "Loutx1", value=2.250342)
EGCESE.add_declare_var("double", "Liny1", value=23.034433)
EGCESE.add_declare_var("double", "Louty1", value=0.920233)
EGCESE.add_declare_var("double", "alpha1", value=3.1)
EGCESE.add_declare_var("double", "Qc1", value=0.0217)
EGCESE.add_declare_var("double", "R01", value=0.99)
EGCESE.add_declare_var("double", "smallaxis_y1", value=0.090000/2)
EGCESE.add_declare_var("double", "smallaxis_x1", value=0.060000/2)

EGCESE.add_declare_var("int", "counter", value=0.0)
EGCESE.add_declare_var("double", "chopper_coordinate_offset", value=4.439)
EGCESE.add_declare_var("double", "curve_rot", value=0.0)
EGCESE.add_declare_var("double", "DivSlit0Gap", value=0.02)
EGCESE.add_declare_var("double", "DivSlit1Gap", value=0.02)
EGCESE.add_declare_var("double", "DivSlit2Gap", value=0.02)
EGCESE.add_declare_var("double", "DivSlit3Gap", value=0.02)
EGCESE.add_declare_var("double", "DivSlit1Pos", value=1.0814)
EGCESE.add_declare_var("double", "DivSlit2Pos", value=1.661)
EGCESE.add_declare_var("double", "DivSlit3Pos", value=2.961)
EGCESE.add_declare_var("double", "chopGap", value=0.04)
EGCESE.add_declare_var("double", "BW_chopGap", value=0.04)
EGCESE.add_declare_var("double", "chopFrameOverlap1Pos", value=8.53)
EGCESE.add_declare_var("double", "chopFrameOverlap2Pos", value=14.973)
EGCESE.add_declare_var("double", "benderAngle", value=0.01886551)
EGCESE.add_declare_var("int", "i")
EGCESE.append_initialize("if (L_0>0){ ")
EGCESE.append_initialize("	E_0=81.82/(L_0*L_0); ")
EGCESE.append_initialize("} ")

EGCESE.append_initialize("  ")
EGCESE.append_initialize("PulseHighFluxOffset=2.0e-4; ")
EGCESE.append_initialize("ModPulseLengthHighF=2.86e-3; ")
EGCESE.append_initialize("InstLength=162.0; ")
EGCESE.append_initialize("chopPulseDist= 4.41+0.032+2.0-0.1; ")
EGCESE.append_initialize("if  (chopPulseFrequencyOrder*chopPulseOpening > 170.0/360.0/14.0) {    /******* Check if pulse shapping chopper opening is large enough for requested frequency or reduce frequency *******/ ")
EGCESE.append_initialize("	 chopPulseFrequencyOrder=floor(170.0/360.0/14.0/chopPulseOpening); ")
EGCESE.append_initialize("	printf(\" \\n \\n Warning: Impossible combination of chopPulseFrequencyOrder and chopPulseOpening chosen, chopPulseFrequencyOrder reduced to: %f  \\n\", chopPulseFrequencyOrder); ")
EGCESE.append_initialize("} ")
EGCESE.append_initialize("lambda_1=1.0/(0.1106*sqrt(E_0));  /**** general chopper calculations **********/ ")
EGCESE.append_initialize("WavelengthBand = 1/(InstLength-chopPulseDist)/14.0/2.528e-4; ")
EGCESE.append_initialize("lambda_0=lambda_1-WavelengthBand; ")
EGCESE.append_initialize("v_0=3956.0/lambda_1;   ")
EGCESE.append_initialize("v_1=3956.0/lambda_0; ")
EGCESE.append_initialize("t_samp_center=PulseHighFluxOffset+ModPulseLengthHighF/2.0+(InstLength/v_1+InstLength/v_0)/2.0; ")
EGCESE.append_initialize("t_samp_0=t_samp_center-1.0/14.0/2.0; ")
EGCESE.append_initialize("t_samp_1=t_samp_center+1.0/14.0/2.0; ")
EGCESE.append_initialize("chopPulseOffset=(chopPulseDist/v_1+chopPulseDist/v_0)/2.0+ModPulseLengthHighF/2.0+PulseHighFluxOffset; ")
EGCESE.append_initialize("chopPulsePossibleOpening=chopPulseDist/v_0-chopPulseOffset; ")
EGCESE.append_initialize("chopPulsePhaseOffset=  (chopPulseOffset+ chopPulseOpening/2.0)*14.0*chopPulseFrequencyOrder*360.0-170.0/2.0; ")
EGCESE.append_initialize("chopPulse2PhaseOffset= chopPulsePhaseOffset- 360.0*(chopPulseOpening*14.0*chopPulseFrequencyOrder)+170.0; ")
EGCESE.append_initialize("if  (chopPulseFrequencyOrder == 0) {  ")
EGCESE.append_initialize("	chopPulsePhaseOffset= 0; ")
EGCESE.append_initialize("	chopPulse2PhaseOffset= 0; ")
EGCESE.append_initialize("		printf(\" \\n \\n Warning: Pulse shaping chopper parked! Setting the offsets to zero\"); ")
EGCESE.append_initialize("} ")
EGCESE.append_initialize("chopFrameOverlap1Open= 1.0/14.0/InstLength*(chopFrameOverlap1Pos)*1.5 ; ")
EGCESE.append_initialize("chopFrameOverlap1Offset=(  ( (chopFrameOverlap1Pos)/v_1+(chopFrameOverlap1Pos)/v_0)/2.0+PulseHighFluxOffset+ModPulseLengthHighF/2.0) ; ")
EGCESE.append_initialize("chopFrameOverlap1PhaseOffset=  (chopFrameOverlap1Offset)*14.0*360.0; ")
EGCESE.append_initialize("chopFrameOverlap2Open= 1.0/14.0/InstLength*(chopFrameOverlap2Pos)*1.65 ; ")
EGCESE.append_initialize("chopFrameOverlap2Offset=(  ( (chopFrameOverlap2Pos)/v_1+(chopFrameOverlap2Pos)/v_0)/2.0+PulseHighFluxOffset+ModPulseLengthHighF/2.0) ; ")
EGCESE.append_initialize("chopFrameOverlap2PhaseOffset=  (chopFrameOverlap2Offset)*14.0*360.0; ")
EGCESE.append_initialize("chopBW_t0= PulseHighFluxOffset+ModPulseLengthHighF/2.0 + chopBWPos/v_1; ")
EGCESE.append_initialize("chopBW_t1=  PulseHighFluxOffset+ModPulseLengthHighF/2.0 + chopBWPos/v_0; ")
EGCESE.append_initialize("chopBWOpen= 360.0/InstLength*(chopBWPos-chopPulseDist*1); ")
EGCESE.append_initialize("chopBWOffset=(chopBW_t0+chopBW_t1)/2.0; ")
EGCESE.append_initialize("chopBWPhaseOffset=  (chopBWOffset)*14.0*360.0; ")
EGCESE.append_initialize("if (printMValues==1) { ")
EGCESE.append_initialize("	FILE* fp = fopen(\"CoatingDistributions.txt\", \"w\"); ")
EGCESE.append_initialize("	fprintf(fp,\"Coating Distributions. From moderator towards sample:\\n\"); ")
EGCESE.append_initialize("	fprintf(fp,\"m_horizontal , m_vertical , C_elementlength:\\n\"); ")
EGCESE.append_initialize("	fprintf(fp,\"NBOA:\\n\"); ")
EGCESE.append_initialize("	for (i = 0 ; i < 13 ; i++){ ")
EGCESE.append_initialize("		fprintf(fp,\"%f , %f , %f\\n\",C_mValues6horizontalS[i],C_mValues6verticalS[i],C_elementLength6S[i]); ")
EGCESE.append_initialize("	} ")
EGCESE.append_initialize("	fprintf(fp,\"\\nCurved section:\\n\"); ")
EGCESE.append_initialize("	fprintf(fp,\"(%f,%f) , %f , %f\\n\",3.000000,3.500000,2.500000,18.0); ")
EGCESE.append_initialize("	 ")
EGCESE.append_initialize("	fprintf(fp,\"\\nExpanding ellipse:\\n\"); ")
EGCESE.append_initialize("	for (i = 0 ; i < 51 ; i++){ ")
EGCESE.append_initialize("		fprintf(fp,\"%f , %f , %f\\n\",C_mValues3horizontalS[i],C_mValues3verticalS[i],C_elementLength3S[i]); ")
EGCESE.append_initialize("	} ")
EGCESE.append_initialize("	 ")
EGCESE.append_initialize("	fprintf(fp,\"\\nLong Straight Section\\n\"); ")
EGCESE.append_initialize("	fprintf(fp,\"%f , %f , %f\\n\",1.500000,1.000000,90.0); ")
EGCESE.append_initialize("	fprintf(fp,\"\\nFocusing Ellipse\\n\"); ")
EGCESE.append_initialize("	for (i = 0 ; i < 41 ; i++){ ")
EGCESE.append_initialize("		fprintf(fp,\"%f , %f , %f\\n\", C_mValues1horizontal_part_1[i], C_mValues1vertical_part_1[i],C_elementLength1_part_1[i]); ")
EGCESE.append_initialize("	} ")
EGCESE.append_initialize("	fprintf(fp,\"2 cm gap for divJaw 3\\n\"); ")
EGCESE.append_initialize("	for (i = 0 ; i < 3 ; i++){ ")
EGCESE.append_initialize("		fprintf(fp,\"%f , %f , %f\\n\", C_mValues1horizontal_part_2[i], C_mValues1vertical_part_2[i],C_elementLength1_part_2[i]); ")
EGCESE.append_initialize("	} ")
EGCESE.append_initialize("	fprintf(fp,\"2 cm gap for divJaw 2\\n\"); ")
EGCESE.append_initialize("	for (i = 0 ; i < 2 ; i++){ ")
EGCESE.append_initialize("		fprintf(fp,\"%f , %f , %f\\n\", C_mValues1horizontal_part_3[i], C_mValues1vertical_part_3[i],C_elementLength1_part_3[i]); ")
EGCESE.append_initialize("	} ")
EGCESE.append_initialize("fprintf(fp,\"2 cm gap for divJaw 1 \\n\"); ")
EGCESE.append_initialize("	for (i = 0 ; i < 3 ; i++){ ")
EGCESE.append_initialize("		fprintf(fp,\"%f , %f , %f\\n\", C_mValues1horizontal_part_4[i], C_mValues1vertical_part_4[i],C_elementLength1_part_4[i]); ")
EGCESE.append_initialize("	} ")
EGCESE.append_initialize("fclose(fp); ")
EGCESE.append_initialize("} ")
EGCESE.append_initialize("printf(\"\\n part 3 length: %f\\n\",DivSlit2Pos-DivSlit1Gap/2.0-DivSlit2Gap/2.0-DivSlit1Pos); ")
EGCESE.append_initialize("printf(\"\\n part 4 length: %f\\n\",DivSlit1Pos-DivSlit1Gap/2.0-sample_dist); ")
EGCESE.add_declare_var("int", "element_index")
C_elementLength6S_total_length = EGCESE.add_declare_var("double", "C_elementLength6S_total_length")
EGCESE.append_initialize("C_elementLength6S_total_length=0;")
EGCESE.append_initialize("for (element_index=0;element_index<" + str(C_elementLength6S.vector) + ";element_index++) {")
EGCESE.append_initialize("  C_elementLength6S_total_length += C_elementLength6S[element_index];")
EGCESE.append_initialize("}")


Origin = EGCESE.add_component("Origin", "Progress_bar")
Origin.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

ESS_source = EGCESE.add_component("ESS_source", "ESS_butterfly")
ESS_source.sector = "\"W\""
ESS_source.beamline = 4
ESS_source.yheight = 0.030000
ESS_source.cold_frac = 0.500000
ESS_source.dist = 1.903398
ESS_source.focus_xw = "0.068797+2*0.01277"
ESS_source.focus_yh = 0.03472
ESS_source.c_performance = 1.0
ESS_source.t_performance = 1.0
ESS_source.Lmin = "WaveMin"
ESS_source.Lmax = "WaveMax"
ESS_source.tmax_multiplier = 1.500000
ESS_source.n_pulses = "Npulse"
ESS_source.acc_power = "power"
ESS_source.tfocus_dist = 6.32962
ESS_source.tfocus_time = "6.32962/v_0"
ESS_source.tfocus_width = "1.2*chopPulseOpening"
ESS_source.set_AT(['0', ' 0', ' 0'], RELATIVE="Origin")
ESS_source.set_ROTATED(['0', '0', '0'], RELATIVE="Origin")

StartOfGuide = EGCESE.add_component("StartOfGuide", "Arm")
StartOfGuide.set_AT(['0.01277', '0.000000', '1.903398-u'], RELATIVE="Origin")
StartOfGuide.set_ROTATED(['0', '-0.56', '0'], RELATIVE="Origin")

NBOA = EGCESE.add_component("NBOA", "Elliptic_guide_gravity")
NBOA.l = 4.39553
NBOA.xwidth = 0.069634
NBOA.yheight = 0.04862
NBOA.linxw = 3.4578
NBOA.loutxw = 0.415155
NBOA.linyh = 1.36
NBOA.loutyh = 3.487681
NBOA.dimensionsAt = "\"mid\""
NBOA.R0 = 0.990000
NBOA.Qc = 0.021700
NBOA.alpha = 3.100000
NBOA.mvaluesright = C_mValues6horizontalS
NBOA.mvaluesleft = C_mValues6horizontalS
NBOA.mvaluestop = C_mValues6verticalS
NBOA.mvaluesbottom = C_mValues6verticalS

NBOA.seglength = C_elementLength6S
NBOA.nSegments = C_elementLength6S.vector
NBOA.l = C_elementLength6S_total_length
NBOA.W=0.003000
NBOA.set_AT(['0', '0', 'u'], RELATIVE="StartOfGuide")

EndOfelement_6 = EGCESE.add_component("EndOfelement_6", "Arm")
EndOfelement_6.set_AT(['0', '0', '4.39553+2*u'], RELATIVE="PREVIOUS")

L_monBeforePSC1 = EGCESE.add_component("L_monBeforePSC1", "L_monitor")
L_monBeforePSC1.nL = 100
L_monBeforePSC1.filename = "\"L_monBeforePSC1.dat\""
L_monBeforePSC1.xwidth = 0.2
L_monBeforePSC1.yheight = 0.2
L_monBeforePSC1.Lmin = "lambda_1/2"
L_monBeforePSC1.Lmax = "lambda_0*2"
L_monBeforePSC1.restore_neutron = 1
L_monBeforePSC1.set_AT(['0', ' 0', ' u'], RELATIVE="PREVIOUS")

ToFBeforerPSC1 = EGCESE.add_component("ToFBeforerPSC1", "TOF_monitor")
ToFBeforerPSC1.nt = 1000
ToFBeforerPSC1.filename = "\"ToFBeforePSC1.dat\""
ToFBeforerPSC1.xwidth = 0.2
ToFBeforerPSC1.yheight = 0.2
ToFBeforerPSC1.tmax = 2e4
ToFBeforerPSC1.restore_neutron = 1
ToFBeforerPSC1.set_AT(['0', ' 0', ' u'], RELATIVE="PREVIOUS")

TofLambdaBeforePSC = EGCESE.add_component("TofLambdaBeforePSC", "TOFLambda_monitor")
TofLambdaBeforePSC.nL = 100
TofLambdaBeforePSC.nt = 100
TofLambdaBeforePSC.tmin = 0
TofLambdaBeforePSC.tmax = 2e4
TofLambdaBeforePSC.filename = "\"TofLambdaBeforePSC1.dat\""
TofLambdaBeforePSC.xwidth = "sampleSizeY"
TofLambdaBeforePSC.yheight = "sampleSizeY"
TofLambdaBeforePSC.Lmin = "lambda_0*0.5"
TofLambdaBeforePSC.Lmax = "lambda_1*2"
TofLambdaBeforePSC.restore_neutron = 1
TofLambdaBeforePSC.set_AT(['0', ' 0', ' u'], RELATIVE="PREVIOUS")

PulseShapingChopper = EGCESE.add_component("PulseShapingChopper", "DiskChopper")
PulseShapingChopper.theta_0 = 170.0
PulseShapingChopper.radius = 0.35
PulseShapingChopper.yheight = "0.047514+2*ChopTransBunker"
PulseShapingChopper.nu = "14.0*chopPulseFrequencyOrder"
PulseShapingChopper.nslit = 1
PulseShapingChopper.phase = "chopPulsePhaseOffset-0"
PulseShapingChopper.set_AT(['0', ' 0', ' PscOff'], RELATIVE="PREVIOUS")

ToFInsidePSC = EGCESE.add_component("ToFInsidePSC", "TOF_monitor")
ToFInsidePSC.nt = 1000
ToFInsidePSC.filename = "\"ToFInsidePSC.dat\""
ToFInsidePSC.xwidth = 0.2
ToFInsidePSC.yheight = 0.2
ToFInsidePSC.tmax = 2e4
ToFInsidePSC.restore_neutron = 1
ToFInsidePSC.set_AT(['0', ' 0', 'u'], RELATIVE="PREVIOUS")

PulseShapingChopper2 = EGCESE.add_component("PulseShapingChopper2", "DiskChopper")
PulseShapingChopper2.theta_0 = 170.0
PulseShapingChopper2.radius = 0.35
PulseShapingChopper2.yheight = "0.047514+2*ChopTransBunker"
PulseShapingChopper2.nu = "14.0*chopPulseFrequencyOrder"
PulseShapingChopper2.nslit = 1
PulseShapingChopper2.phase = "chopPulse2PhaseOffset+0"
PulseShapingChopper2.set_AT(['0', ' 0', ' discD'], RELATIVE="PREVIOUS")

TofLambdaAfterPSC2 = EGCESE.add_component("TofLambdaAfterPSC2", "TOFLambda_monitor")
TofLambdaAfterPSC2.nL = 100
TofLambdaAfterPSC2.nt = 100
TofLambdaAfterPSC2.tmin = 0
TofLambdaAfterPSC2.tmax = 2e4
TofLambdaAfterPSC2.filename = "\"TofLambdaAfterPSC2.dat\""
TofLambdaAfterPSC2.xwidth = "sampleSizeY"
TofLambdaAfterPSC2.yheight = "sampleSizeY"
TofLambdaAfterPSC2.Lmin = "lambda_0*0.5"
TofLambdaAfterPSC2.Lmax = "lambda_1*2"
TofLambdaAfterPSC2.restore_neutron = 1
TofLambdaAfterPSC2.set_AT(['0', ' 0', ' u'], RELATIVE="PREVIOUS")

ToFAfterPSC2 = EGCESE.add_component("ToFAfterPSC2", "TOF_monitor")
ToFAfterPSC2.nt = 1000
ToFAfterPSC2.filename = "\"ToFAfterPSC2.dat\""
ToFAfterPSC2.xwidth = 0.2
ToFAfterPSC2.yheight = 0.2
ToFAfterPSC2.tmax = 2e4
ToFAfterPSC2.restore_neutron = 1
ToFAfterPSC2.set_AT(['0', ' 0', 'u'], RELATIVE="PREVIOUS")

L_monAfterPSC2 = EGCESE.add_component("L_monAfterPSC2", "L_monitor")
L_monAfterPSC2.nL = 100
L_monAfterPSC2.filename = "\"L_monAfterPSC2.dat\""
L_monAfterPSC2.xwidth = 0.2
L_monAfterPSC2.yheight = 0.2
L_monAfterPSC2.Lmin = "lambda_1/2"
L_monAfterPSC2.Lmax = "lambda_0*2"
L_monAfterPSC2.restore_neutron = 1
L_monAfterPSC2.set_AT(['0', ' 0', ' u'], RELATIVE="PREVIOUS")

EndOfelement_5 = EGCESE.add_component("EndOfelement_5", "Arm")
EndOfelement_5.set_AT(['0', '0', '0.081707 '], RELATIVE="EndOfelement_6")

curved_guide_1_0 = EGCESE.add_component("curved_guide_1_0", "Guide_gravity")
curved_guide_1_0.w1 = 0.029534
curved_guide_1_0.h1 = 0.047514
curved_guide_1_0.w2 = 0.029534
curved_guide_1_0.h2 = 0.047514
curved_guide_1_0.l = 0.5
curved_guide_1_0.R0 = 0.990000
curved_guide_1_0.Qc = 0.021700
curved_guide_1_0.alpha = 3.100000
curved_guide_1_0.W = 0.003000
curved_guide_1_0.mleft = 3.000000
curved_guide_1_0.mright = 3.500000
curved_guide_1_0.mtop = 2.500000
curved_guide_1_0.mbottom = 2.500000
curved_guide_1_0.G = -9.82
curved_guide_1_0.set_AT(['0', '0', 'u'], RELATIVE="PREVIOUS")
curved_guide_1_0.set_ROTATED(['0', 'benderAngle', '0'], RELATIVE="PREVIOUS")

curved_guide_2_0 = EGCESE.add_component("curved_guide_2_0", "Guide_gravity")
curved_guide_2_0.w1 = 0.029534
curved_guide_2_0.h1 = 0.047514
curved_guide_2_0.w2 = 0.029534
curved_guide_2_0.h2 = 0.047514
curved_guide_2_0.l = 0.5
curved_guide_2_0.R0 = 0.990000
curved_guide_2_0.Qc = 0.021700
curved_guide_2_0.alpha = 3.100000
curved_guide_2_0.W = 0.003000
curved_guide_2_0.mleft = 3.000000
curved_guide_2_0.mright = 3.500000
curved_guide_2_0.mtop = 2.500000
curved_guide_2_0.mbottom = 2.500000
curved_guide_2_0.G = -9.82
curved_guide_2_0.set_AT(['7.57345916228e-10', '0', '0.500 + u + 6e-5'], RELATIVE="PREVIOUS")
curved_guide_2_0.set_ROTATED(['0', 'benderAngle', '0'], RELATIVE="PREVIOUS")

curved_guide_3_0 = EGCESE.add_component("curved_guide_3_0", "Guide_gravity")
curved_guide_3_0.w1 = 0.029534
curved_guide_3_0.h1 = 0.047514
curved_guide_3_0.w2 = 0.029534
curved_guide_3_0.h2 = 0.047514
curved_guide_3_0.l = 0.5
curved_guide_3_0.R0 = 0.990000
curved_guide_3_0.Qc = 0.021700
curved_guide_3_0.alpha = 3.100000
curved_guide_3_0.W = 0.003000
curved_guide_3_0.mleft = 3.000000
curved_guide_3_0.mright = 3.500000
curved_guide_3_0.mtop = 2.500000
curved_guide_3_0.mbottom = 2.500000
curved_guide_3_0.G = -9.82
curved_guide_3_0.set_AT(['7.57345916228e-10', '0', '0.500 + u + 6e-5'], RELATIVE="PREVIOUS")
curved_guide_3_0.set_ROTATED(['0', 'benderAngle', '0'], RELATIVE="PREVIOUS")

curved_guide_4_0 = EGCESE.add_component("curved_guide_4_0", "Guide_gravity")
curved_guide_4_0.w1 = 0.029534
curved_guide_4_0.h1 = 0.047514
curved_guide_4_0.w2 = 0.029534
curved_guide_4_0.h2 = 0.047514
curved_guide_4_0.l = 0.5
curved_guide_4_0.R0 = 0.990000
curved_guide_4_0.Qc = 0.021700
curved_guide_4_0.alpha = 3.100000
curved_guide_4_0.W = 0.003000
curved_guide_4_0.mleft = 3.000000
curved_guide_4_0.mright = 3.500000
curved_guide_4_0.mtop = 2.500000
curved_guide_4_0.mbottom = 2.500000
curved_guide_4_0.G = -9.82
curved_guide_4_0.set_AT(['7.57345916228e-10', '0', '0.500 + u + 6e-5'], RELATIVE="PREVIOUS")
curved_guide_4_0.set_ROTATED(['0', 'benderAngle', '0'], RELATIVE="PREVIOUS")

curved_guide_5_beforeChopper = EGCESE.add_component("curved_guide_5_beforeChopper", "Guide_gravity")
curved_guide_5_beforeChopper.w1 = 0.029534
curved_guide_5_beforeChopper.h1 = 0.047514
curved_guide_5_beforeChopper.w2 = 0.029534
curved_guide_5_beforeChopper.h2 = 0.047514
curved_guide_5_beforeChopper.l = 0.13
curved_guide_5_beforeChopper.R0 = 0.990000
curved_guide_5_beforeChopper.Qc = 0.021700
curved_guide_5_beforeChopper.alpha = 3.100000
curved_guide_5_beforeChopper.W = 0.003000
curved_guide_5_beforeChopper.mleft = 3.000000
curved_guide_5_beforeChopper.mright = 3.500000
curved_guide_5_beforeChopper.mtop = 2.500000
curved_guide_5_beforeChopper.mbottom = 2.500000
curved_guide_5_beforeChopper.G = -9.82
curved_guide_5_beforeChopper.set_AT(['7.57345916228e-10', '0', '0.500 + u + 6e-5'], RELATIVE="PREVIOUS")
curved_guide_5_beforeChopper.set_ROTATED(['0', 'benderAngle', '0'], RELATIVE="PREVIOUS")

L_monBeforeFOC1 = EGCESE.add_component("L_monBeforeFOC1", "L_monitor")
L_monBeforeFOC1.nL = 100
L_monBeforeFOC1.filename = "\"L_monBeforeFOC1.dat\""
L_monBeforeFOC1.xwidth = 0.2
L_monBeforeFOC1.yheight = 0.2
L_monBeforeFOC1.Lmin = "lambda_0/2.0"
L_monBeforeFOC1.Lmax = "lambda_1*2.0"
L_monBeforeFOC1.restore_neutron = 1
L_monBeforeFOC1.set_AT(['0', ' 0', ' 0.13+u'], RELATIVE="PREVIOUS")
L_monBeforeFOC1.set_ROTATED(['0', ' 0', ' 0'], RELATIVE="PREVIOUS")

ToFBeforeFOC1 = EGCESE.add_component("ToFBeforeFOC1", "TOF_monitor")
ToFBeforeFOC1.nt = 1000
ToFBeforeFOC1.filename = "\"ToFBeforeFOC1.dat\""
ToFBeforeFOC1.xwidth = 0.2
ToFBeforeFOC1.yheight = 0.2
ToFBeforeFOC1.tmax = 2e4
ToFBeforeFOC1.restore_neutron = 1
ToFBeforeFOC1.set_AT(['0', ' 0', ' u'], RELATIVE="PREVIOUS")

FOC1 = EGCESE.add_component("FOC1", "DiskChopper")
FOC1.theta_0 = "FOCopen1"
FOC1.radius = 0.35
FOC1.yheight = "0.047514+2*ChopTransBunker"
FOC1.nu = 14
FOC1.nslit = 1
FOC1.phase = "chopFrameOverlap1PhaseOffset"
FOC1.set_AT(['0', ' 0', '0.02'], RELATIVE="PREVIOUS")
FOC1.set_ROTATED(['0', '0', '0'], RELATIVE="PREVIOUS")

ToFAfterFOC1 = EGCESE.add_component("ToFAfterFOC1", "TOF_monitor")
ToFAfterFOC1.nt = 1000
ToFAfterFOC1.filename = "\"ToFAfterFOC1.dat\""
ToFAfterFOC1.xwidth = 0.2
ToFAfterFOC1.yheight = 0.2
ToFAfterFOC1.tmax = 2e4
ToFAfterFOC1.restore_neutron = 1
ToFAfterFOC1.set_AT(['0', ' 0', ' u'], RELATIVE="PREVIOUS")

L_monAfterFOC1 = EGCESE.add_component("L_monAfterFOC1", "L_monitor")
L_monAfterFOC1.nL = 100
L_monAfterFOC1.filename = "\"L_monAfterFOC1.dat\""
L_monAfterFOC1.xwidth = 0.2
L_monAfterFOC1.yheight = 0.2
L_monAfterFOC1.Lmin = "lambda_0/2.0"
L_monAfterFOC1.Lmax = "lambda_1*2.0"
L_monAfterFOC1.restore_neutron = 1
L_monAfterFOC1.set_AT(['0', ' 0', ' u'], RELATIVE="PREVIOUS")

curved_guide_5_afterChopper = EGCESE.add_component("curved_guide_5_afterChopper", "Guide_gravity")
curved_guide_5_afterChopper.w1 = 0.029534
curved_guide_5_afterChopper.h1 = 0.047514
curved_guide_5_afterChopper.w2 = 0.029534
curved_guide_5_afterChopper.h2 = 0.047514
curved_guide_5_afterChopper.l = 0.33
curved_guide_5_afterChopper.R0 = 0.990000
curved_guide_5_afterChopper.Qc = 0.021700
curved_guide_5_afterChopper.alpha = 3.100000
curved_guide_5_afterChopper.W = 0.003000
curved_guide_5_afterChopper.mleft = 3.000000
curved_guide_5_afterChopper.mright = 3.500000
curved_guide_5_afterChopper.mtop = 2.500000
curved_guide_5_afterChopper.mbottom = 2.500000
curved_guide_5_afterChopper.G = -9.82
curved_guide_5_afterChopper.set_AT(['0', '0', '0.17'], RELATIVE="curved_guide_5_beforeChopper")
curved_guide_5_afterChopper.set_ROTATED(['0', '0', '0'], RELATIVE="curved_guide_5_beforeChopper")

curved_guide_6_0 = EGCESE.add_component("curved_guide_6_0", "Guide_gravity")
curved_guide_6_0.w1 = 0.029534
curved_guide_6_0.h1 = 0.047514
curved_guide_6_0.w2 = 0.029534
curved_guide_6_0.h2 = 0.047514
curved_guide_6_0.l = 0.5
curved_guide_6_0.R0 = 0.990000
curved_guide_6_0.Qc = 0.021700
curved_guide_6_0.alpha = 3.100000
curved_guide_6_0.W = 0.003000
curved_guide_6_0.mleft = 3.000000
curved_guide_6_0.mright = 3.500000
curved_guide_6_0.mtop = 2.500000
curved_guide_6_0.mbottom = 2.500000
curved_guide_6_0.G = -9.82
curved_guide_6_0.set_AT(['7.57345916228e-10', '0', '0.33+u'], RELATIVE="PREVIOUS")
curved_guide_6_0.set_ROTATED(['0', 'benderAngle', '0'], RELATIVE="PREVIOUS")

curved_guide_7_0 = EGCESE.add_component("curved_guide_7_0", "Guide_gravity")
curved_guide_7_0.w1 = 0.029534
curved_guide_7_0.h1 = 0.047514
curved_guide_7_0.w2 = 0.029534
curved_guide_7_0.h2 = 0.047514
curved_guide_7_0.l = 0.5
curved_guide_7_0.R0 = 0.990000
curved_guide_7_0.Qc = 0.021700
curved_guide_7_0.alpha = 3.100000
curved_guide_7_0.W = 0.003000
curved_guide_7_0.mleft = 3.000000
curved_guide_7_0.mright = 3.500000
curved_guide_7_0.mtop = 2.500000
curved_guide_7_0.mbottom = 2.500000
curved_guide_7_0.G = -9.82
curved_guide_7_0.set_AT(['7.57345916228e-10', '0', '0.500 + u + 6e-5'], RELATIVE="PREVIOUS")
curved_guide_7_0.set_ROTATED(['0', 'benderAngle', '0'], RELATIVE="PREVIOUS")

curved_guide_8_0 = EGCESE.add_component("curved_guide_8_0", "Guide_gravity")
curved_guide_8_0.w1 = 0.029534
curved_guide_8_0.h1 = 0.047514
curved_guide_8_0.w2 = 0.029534
curved_guide_8_0.h2 = 0.047514
curved_guide_8_0.l = 0.5
curved_guide_8_0.R0 = 0.990000
curved_guide_8_0.Qc = 0.021700
curved_guide_8_0.alpha = 3.100000
curved_guide_8_0.W = 0.003000
curved_guide_8_0.mleft = 3.000000
curved_guide_8_0.mright = 3.500000
curved_guide_8_0.mtop = 2.500000
curved_guide_8_0.mbottom = 2.500000
curved_guide_8_0.G = -9.82
curved_guide_8_0.set_AT(['7.57345916228e-10', '0', '0.500 + u + 6e-5'], RELATIVE="PREVIOUS")
curved_guide_8_0.set_ROTATED(['0', 'benderAngle', '0'], RELATIVE="PREVIOUS")

curved_guide_9_0 = EGCESE.add_component("curved_guide_9_0", "Guide_gravity")
curved_guide_9_0.w1 = 0.029534
curved_guide_9_0.h1 = 0.047514
curved_guide_9_0.w2 = 0.029534
curved_guide_9_0.h2 = 0.047514
curved_guide_9_0.l = 0.5
curved_guide_9_0.R0 = 0.990000
curved_guide_9_0.Qc = 0.021700
curved_guide_9_0.alpha = 3.100000
curved_guide_9_0.W = 0.003000
curved_guide_9_0.mleft = 3.000000
curved_guide_9_0.mright = 3.500000
curved_guide_9_0.mtop = 2.500000
curved_guide_9_0.mbottom = 2.500000
curved_guide_9_0.G = -9.82
curved_guide_9_0.set_AT(['7.57345916228e-10', '0', '0.500 + u + 6e-5'], RELATIVE="PREVIOUS")
curved_guide_9_0.set_ROTATED(['0', 'benderAngle', '0'], RELATIVE="PREVIOUS")

curved_guide_10_0 = EGCESE.add_component("curved_guide_10_0", "Guide_gravity")
curved_guide_10_0.w1 = 0.029534
curved_guide_10_0.h1 = 0.047514
curved_guide_10_0.w2 = 0.029534
curved_guide_10_0.h2 = 0.047514
curved_guide_10_0.l = 0.5
curved_guide_10_0.R0 = 0.990000
curved_guide_10_0.Qc = 0.021700
curved_guide_10_0.alpha = 3.100000
curved_guide_10_0.W = 0.003000
curved_guide_10_0.mleft = 3.000000
curved_guide_10_0.mright = 3.500000
curved_guide_10_0.mtop = 2.500000
curved_guide_10_0.mbottom = 2.500000
curved_guide_10_0.G = -9.82
curved_guide_10_0.set_AT(['7.57345916228e-10', '0', '0.500 + u + 6e-5'], RELATIVE="PREVIOUS")
curved_guide_10_0.set_ROTATED(['0', 'benderAngle', '0'], RELATIVE="PREVIOUS")

curved_guide_11_0 = EGCESE.add_component("curved_guide_11_0", "Guide_gravity")
curved_guide_11_0.w1 = 0.029534
curved_guide_11_0.h1 = 0.047514
curved_guide_11_0.w2 = 0.029534
curved_guide_11_0.h2 = 0.047514
curved_guide_11_0.l = 0.5
curved_guide_11_0.R0 = 0.990000
curved_guide_11_0.Qc = 0.021700
curved_guide_11_0.alpha = 3.100000
curved_guide_11_0.W = 0.003000
curved_guide_11_0.mleft = 3.000000
curved_guide_11_0.mright = 3.500000
curved_guide_11_0.mtop = 2.500000
curved_guide_11_0.mbottom = 2.500000
curved_guide_11_0.G = -9.82
curved_guide_11_0.set_AT(['7.57345916228e-10', '0', '0.500 + u + 6e-5'], RELATIVE="PREVIOUS")
curved_guide_11_0.set_ROTATED(['0', 'benderAngle', '0'], RELATIVE="PREVIOUS")

curved_guide_12_0 = EGCESE.add_component("curved_guide_12_0", "Guide_gravity")
curved_guide_12_0.w1 = 0.029534
curved_guide_12_0.h1 = 0.047514
curved_guide_12_0.w2 = 0.029534
curved_guide_12_0.h2 = 0.047514
curved_guide_12_0.l = 0.5
curved_guide_12_0.R0 = 0.990000
curved_guide_12_0.Qc = 0.021700
curved_guide_12_0.alpha = 3.100000
curved_guide_12_0.W = 0.003000
curved_guide_12_0.mleft = 3.000000
curved_guide_12_0.mright = 3.500000
curved_guide_12_0.mtop = 2.500000
curved_guide_12_0.mbottom = 2.500000
curved_guide_12_0.G = -9.82
curved_guide_12_0.set_AT(['7.57345916228e-10', '0', '0.500 + u + 6e-5'], RELATIVE="PREVIOUS")
curved_guide_12_0.set_ROTATED(['0', 'benderAngle', '0'], RELATIVE="PREVIOUS")

curved_guide_13_0 = EGCESE.add_component("curved_guide_13_0", "Guide_gravity")
curved_guide_13_0.w1 = 0.029534
curved_guide_13_0.h1 = 0.047514
curved_guide_13_0.w2 = 0.029534
curved_guide_13_0.h2 = 0.047514
curved_guide_13_0.l = 0.5
curved_guide_13_0.R0 = 0.990000
curved_guide_13_0.Qc = 0.021700
curved_guide_13_0.alpha = 3.100000
curved_guide_13_0.W = 0.003000
curved_guide_13_0.mleft = 3.000000
curved_guide_13_0.mright = 3.500000
curved_guide_13_0.mtop = 2.500000
curved_guide_13_0.mbottom = 2.500000
curved_guide_13_0.G = -9.82
curved_guide_13_0.set_AT(['7.57345916228e-10', '0', '0.500 + u + 6e-5'], RELATIVE="PREVIOUS")
curved_guide_13_0.set_ROTATED(['0', 'benderAngle', '0'], RELATIVE="PREVIOUS")

curved_guide_14_0 = EGCESE.add_component("curved_guide_14_0", "Guide_gravity")
curved_guide_14_0.w1 = 0.029534
curved_guide_14_0.h1 = 0.047514
curved_guide_14_0.w2 = 0.029534
curved_guide_14_0.h2 = 0.047514
curved_guide_14_0.l = 0.5
curved_guide_14_0.R0 = 0.990000
curved_guide_14_0.Qc = 0.021700
curved_guide_14_0.alpha = 3.100000
curved_guide_14_0.W = 0.003000
curved_guide_14_0.mleft = 3.000000
curved_guide_14_0.mright = 3.500000
curved_guide_14_0.mtop = 2.500000
curved_guide_14_0.mbottom = 2.500000
curved_guide_14_0.G = -9.82
curved_guide_14_0.set_AT(['7.57345916228e-10', '0', '0.500 + u + 6e-5'], RELATIVE="PREVIOUS")
curved_guide_14_0.set_ROTATED(['0', 'benderAngle', '0'], RELATIVE="PREVIOUS")

curved_guide_15_0 = EGCESE.add_component("curved_guide_15_0", "Guide_gravity")
curved_guide_15_0.w1 = 0.029534
curved_guide_15_0.h1 = 0.047514
curved_guide_15_0.w2 = 0.029534
curved_guide_15_0.h2 = 0.047514
curved_guide_15_0.l = 0.5
curved_guide_15_0.R0 = 0.990000
curved_guide_15_0.Qc = 0.021700
curved_guide_15_0.alpha = 3.100000
curved_guide_15_0.W = 0.003000
curved_guide_15_0.mleft = 3.000000
curved_guide_15_0.mright = 3.500000
curved_guide_15_0.mtop = 2.500000
curved_guide_15_0.mbottom = 2.500000
curved_guide_15_0.G = -9.82
curved_guide_15_0.set_AT(['7.57345916228e-10', '0', '0.500 + u + 6e-5'], RELATIVE="PREVIOUS")
curved_guide_15_0.set_ROTATED(['0', 'benderAngle', '0'], RELATIVE="PREVIOUS")

curved_guide_16_0 = EGCESE.add_component("curved_guide_16_0", "Guide_gravity")
curved_guide_16_0.w1 = 0.029534
curved_guide_16_0.h1 = 0.047514
curved_guide_16_0.w2 = 0.029534
curved_guide_16_0.h2 = 0.047514
curved_guide_16_0.l = 0.5
curved_guide_16_0.R0 = 0.990000
curved_guide_16_0.Qc = 0.021700
curved_guide_16_0.alpha = 3.100000
curved_guide_16_0.W = 0.003000
curved_guide_16_0.mleft = 3.000000
curved_guide_16_0.mright = 3.500000
curved_guide_16_0.mtop = 2.500000
curved_guide_16_0.mbottom = 2.500000
curved_guide_16_0.G = -9.82
curved_guide_16_0.set_AT(['7.57345916228e-10', '0', '0.500 + u + 6e-5'], RELATIVE="PREVIOUS")
curved_guide_16_0.set_ROTATED(['0', 'benderAngle', '0'], RELATIVE="PREVIOUS")

curved_guide_17_0 = EGCESE.add_component("curved_guide_17_0", "Guide_gravity")
curved_guide_17_0.w1 = 0.029534
curved_guide_17_0.h1 = 0.047514
curved_guide_17_0.w2 = 0.029534
curved_guide_17_0.h2 = 0.047514
curved_guide_17_0.l = 0.5
curved_guide_17_0.R0 = 0.990000
curved_guide_17_0.Qc = 0.021700
curved_guide_17_0.alpha = 3.100000
curved_guide_17_0.W = 0.003000
curved_guide_17_0.mleft = 3.000000
curved_guide_17_0.mright = 3.500000
curved_guide_17_0.mtop = 2.500000
curved_guide_17_0.mbottom = 2.500000
curved_guide_17_0.G = -9.82
curved_guide_17_0.set_AT(['7.57345916228e-10', '0', '0.500 + u + 6e-5'], RELATIVE="PREVIOUS")
curved_guide_17_0.set_ROTATED(['0', 'benderAngle', '0'], RELATIVE="PREVIOUS")

curved_guide_18_beforeChopper = EGCESE.add_component("curved_guide_18_beforeChopper", "Guide_gravity")
curved_guide_18_beforeChopper.w1 = 0.029534
curved_guide_18_beforeChopper.h1 = 0.047514
curved_guide_18_beforeChopper.w2 = 0.029534
curved_guide_18_beforeChopper.h2 = 0.047514
curved_guide_18_beforeChopper.l = 0.07
curved_guide_18_beforeChopper.R0 = 0.990000
curved_guide_18_beforeChopper.Qc = 0.021700
curved_guide_18_beforeChopper.alpha = 3.100000
curved_guide_18_beforeChopper.W = 0.003000
curved_guide_18_beforeChopper.mleft = 3.000000
curved_guide_18_beforeChopper.mright = 3.500000
curved_guide_18_beforeChopper.mtop = 2.500000
curved_guide_18_beforeChopper.mbottom = 2.500000
curved_guide_18_beforeChopper.G = -9.82
curved_guide_18_beforeChopper.set_AT(['7.57345916228e-10', '0', '0.500 + u + 6e-5'], RELATIVE="PREVIOUS")
curved_guide_18_beforeChopper.set_ROTATED(['0', 'benderAngle', '0'], RELATIVE="PREVIOUS")

L_monBeforeFOC2 = EGCESE.add_component("L_monBeforeFOC2", "L_monitor")
L_monBeforeFOC2.nL = 100
L_monBeforeFOC2.filename = "\"L_monBeforeFOC2.dat\""
L_monBeforeFOC2.xwidth = 0.2
L_monBeforeFOC2.yheight = 0.2
L_monBeforeFOC2.Lmin = "lambda_0/2.0"
L_monBeforeFOC2.Lmax = "lambda_1*2.0"
L_monBeforeFOC2.restore_neutron = 1
L_monBeforeFOC2.set_AT(['0', '0', ' 0.07+u'], RELATIVE="PREVIOUS")
L_monBeforeFOC2.set_ROTATED(['0', ' 0', ' 0'], RELATIVE="PREVIOUS")

ToFBeforeFOC2 = EGCESE.add_component("ToFBeforeFOC2", "TOF_monitor")
ToFBeforeFOC2.nt = 1000
ToFBeforeFOC2.filename = "\"ToFBeforeFOC2.dat\""
ToFBeforeFOC2.xwidth = 0.2
ToFBeforeFOC2.yheight = 0.2
ToFBeforeFOC2.tmax = 2e4
ToFBeforeFOC2.restore_neutron = 1
ToFBeforeFOC2.set_AT(['0', ' 0', ' u'], RELATIVE="PREVIOUS")

FOC2 = EGCESE.add_component("FOC2", "DiskChopper")
FOC2.theta_0 = "FOCopen2"
FOC2.radius = 0.35
FOC2.yheight = "0.047514+2*ChopTransBunker"
FOC2.nu = 14
FOC2.nslit = 1
FOC2.phase = "chopFrameOverlap2PhaseOffset"
FOC2.set_AT(['0', '0', ' 0.02'], RELATIVE="PREVIOUS")
FOC2.set_ROTATED(['0', '0', 'u'], RELATIVE="PREVIOUS")

ToFAfterFOC2 = EGCESE.add_component("ToFAfterFOC2", "TOF_monitor")
ToFAfterFOC2.nt = 1000
ToFAfterFOC2.filename = "\"ToFAfterFOC2.dat\""
ToFAfterFOC2.xwidth = 0.2
ToFAfterFOC2.yheight = 0.2
ToFAfterFOC2.tmax = 2e4
ToFAfterFOC2.restore_neutron = 1
ToFAfterFOC2.set_AT(['0', ' 0', ' u'], RELATIVE="PREVIOUS")

curved_guide_18_afterChopper = EGCESE.add_component("curved_guide_18_afterChopper", "Guide_gravity")
curved_guide_18_afterChopper.w1 = 0.029534
curved_guide_18_afterChopper.h1 = 0.047514
curved_guide_18_afterChopper.w2 = 0.029534
curved_guide_18_afterChopper.h2 = 0.047514
curved_guide_18_afterChopper.l = 0.39
curved_guide_18_afterChopper.R0 = 0.990000
curved_guide_18_afterChopper.Qc = 0.021700
curved_guide_18_afterChopper.alpha = 3.100000
curved_guide_18_afterChopper.W = 0.003000
curved_guide_18_afterChopper.mleft = 3.000000
curved_guide_18_afterChopper.mright = 3.500000
curved_guide_18_afterChopper.mtop = 2.500000
curved_guide_18_afterChopper.mbottom = 2.500000
curved_guide_18_afterChopper.G = -9.82
curved_guide_18_afterChopper.set_AT(['0', '0', '0.11'], RELATIVE="curved_guide_18_beforeChopper")
curved_guide_18_afterChopper.set_ROTATED(['0', '0', '0'], RELATIVE="curved_guide_18_beforeChopper")

curved_guide_19_0 = EGCESE.add_component("curved_guide_19_0", "Guide_gravity")
curved_guide_19_0.w1 = 0.029534
curved_guide_19_0.h1 = 0.047514
curved_guide_19_0.w2 = 0.029534
curved_guide_19_0.h2 = 0.047514
curved_guide_19_0.l = 0.5
curved_guide_19_0.R0 = 0.990000
curved_guide_19_0.Qc = 0.021700
curved_guide_19_0.alpha = 3.100000
curved_guide_19_0.W = 0.003000
curved_guide_19_0.mleft = 3.000000
curved_guide_19_0.mright = 3.500000
curved_guide_19_0.mtop = 2.500000
curved_guide_19_0.mbottom = 2.500000
curved_guide_19_0.G = -9.82
curved_guide_19_0.set_AT(['7.57345916228e-10', '0', '0.39+u'], RELATIVE="PREVIOUS")
curved_guide_19_0.set_ROTATED(['0', 'benderAngle', '0'], RELATIVE="PREVIOUS")

curved_guide_20_0 = EGCESE.add_component("curved_guide_20_0", "Guide_gravity")
curved_guide_20_0.w1 = 0.029534
curved_guide_20_0.h1 = 0.047514
curved_guide_20_0.w2 = 0.029534
curved_guide_20_0.h2 = 0.047514
curved_guide_20_0.l = 0.5
curved_guide_20_0.R0 = 0.990000
curved_guide_20_0.Qc = 0.021700
curved_guide_20_0.alpha = 3.100000
curved_guide_20_0.W = 0.003000
curved_guide_20_0.mleft = 3.000000
curved_guide_20_0.mright = 3.500000
curved_guide_20_0.mtop = 2.500000
curved_guide_20_0.mbottom = 2.500000
curved_guide_20_0.G = -9.82
curved_guide_20_0.set_AT(['7.57345916228e-10', '0', '0.500 + u + 6e-5'], RELATIVE="PREVIOUS")
curved_guide_20_0.set_ROTATED(['0', 'benderAngle', '0'], RELATIVE="PREVIOUS")

curved_guide_21_0 = EGCESE.add_component("curved_guide_21_0", "Guide_gravity")
curved_guide_21_0.w1 = 0.029534
curved_guide_21_0.h1 = 0.047514
curved_guide_21_0.w2 = 0.029534
curved_guide_21_0.h2 = 0.047514
curved_guide_21_0.l = 0.5
curved_guide_21_0.R0 = 0.990000
curved_guide_21_0.Qc = 0.021700
curved_guide_21_0.alpha = 3.100000
curved_guide_21_0.W = 0.003000
curved_guide_21_0.mleft = 3.000000
curved_guide_21_0.mright = 3.500000
curved_guide_21_0.mtop = 2.500000
curved_guide_21_0.mbottom = 2.500000
curved_guide_21_0.G = -9.82
curved_guide_21_0.set_AT(['7.57345916228e-10', '0', '0.500 + u + 6e-5'], RELATIVE="PREVIOUS")
curved_guide_21_0.set_ROTATED(['0', 'benderAngle', '0'], RELATIVE="PREVIOUS")

curved_guide_22_0 = EGCESE.add_component("curved_guide_22_0", "Guide_gravity")
curved_guide_22_0.w1 = 0.029534
curved_guide_22_0.h1 = 0.047514
curved_guide_22_0.w2 = 0.029534
curved_guide_22_0.h2 = 0.047514
curved_guide_22_0.l = 0.5
curved_guide_22_0.R0 = 0.990000
curved_guide_22_0.Qc = 0.021700
curved_guide_22_0.alpha = 3.100000
curved_guide_22_0.W = 0.003000
curved_guide_22_0.mleft = 3.000000
curved_guide_22_0.mright = 3.500000
curved_guide_22_0.mtop = 2.500000
curved_guide_22_0.mbottom = 2.500000
curved_guide_22_0.G = -9.82
curved_guide_22_0.set_AT(['7.57345916228e-10', '0', '0.500 + u + 6e-5'], RELATIVE="PREVIOUS")
curved_guide_22_0.set_ROTATED(['0', 'benderAngle', '0'], RELATIVE="PREVIOUS")

curved_guide_23_0 = EGCESE.add_component("curved_guide_23_0", "Guide_gravity")
curved_guide_23_0.w1 = 0.029534
curved_guide_23_0.h1 = 0.047514
curved_guide_23_0.w2 = 0.029534
curved_guide_23_0.h2 = 0.047514
curved_guide_23_0.l = 0.5
curved_guide_23_0.R0 = 0.990000
curved_guide_23_0.Qc = 0.021700
curved_guide_23_0.alpha = 3.100000
curved_guide_23_0.W = 0.003000
curved_guide_23_0.mleft = 3.000000
curved_guide_23_0.mright = 3.500000
curved_guide_23_0.mtop = 2.500000
curved_guide_23_0.mbottom = 2.500000
curved_guide_23_0.G = -9.82
curved_guide_23_0.set_AT(['7.57345916228e-10', '0', '0.500 + u + 6e-5'], RELATIVE="PREVIOUS")
curved_guide_23_0.set_ROTATED(['0', 'benderAngle', '0'], RELATIVE="PREVIOUS")

curved_guide_24_0 = EGCESE.add_component("curved_guide_24_0", "Guide_gravity")
curved_guide_24_0.w1 = 0.029534
curved_guide_24_0.h1 = 0.047514
curved_guide_24_0.w2 = 0.029534
curved_guide_24_0.h2 = 0.047514
curved_guide_24_0.l = 0.5
curved_guide_24_0.R0 = 0.990000
curved_guide_24_0.Qc = 0.021700
curved_guide_24_0.alpha = 3.100000
curved_guide_24_0.W = 0.003000
curved_guide_24_0.mleft = 3.000000
curved_guide_24_0.mright = 3.500000
curved_guide_24_0.mtop = 2.500000
curved_guide_24_0.mbottom = 2.500000
curved_guide_24_0.G = -9.82
curved_guide_24_0.set_AT(['7.57345916228e-10', '0', '0.500 + u + 6e-5'], RELATIVE="PREVIOUS")
curved_guide_24_0.set_ROTATED(['0', 'benderAngle', '0'], RELATIVE="PREVIOUS")

curved_guide_25_0 = EGCESE.add_component("curved_guide_25_0", "Guide_gravity")
curved_guide_25_0.w1 = 0.029534
curved_guide_25_0.h1 = 0.047514
curved_guide_25_0.w2 = 0.029534
curved_guide_25_0.h2 = 0.047514
curved_guide_25_0.l = 0.5
curved_guide_25_0.R0 = 0.990000
curved_guide_25_0.Qc = 0.021700
curved_guide_25_0.alpha = 3.100000
curved_guide_25_0.W = 0.003000
curved_guide_25_0.mleft = 3.000000
curved_guide_25_0.mright = 3.500000
curved_guide_25_0.mtop = 2.500000
curved_guide_25_0.mbottom = 2.500000
curved_guide_25_0.G = -9.82
curved_guide_25_0.set_AT(['7.57345916228e-10', '0', '0.500 + u + 6e-5'], RELATIVE="PREVIOUS")
curved_guide_25_0.set_ROTATED(['0', 'benderAngle', '0'], RELATIVE="PREVIOUS")

curved_guide_26_0 = EGCESE.add_component("curved_guide_26_0", "Guide_gravity")
curved_guide_26_0.w1 = 0.029534
curved_guide_26_0.h1 = 0.047514
curved_guide_26_0.w2 = 0.029534
curved_guide_26_0.h2 = 0.047514
curved_guide_26_0.l = 0.5
curved_guide_26_0.R0 = 0.990000
curved_guide_26_0.Qc = 0.021700
curved_guide_26_0.alpha = 3.100000
curved_guide_26_0.W = 0.003000
curved_guide_26_0.mleft = 3.000000
curved_guide_26_0.mright = 3.500000
curved_guide_26_0.mtop = 2.500000
curved_guide_26_0.mbottom = 2.500000
curved_guide_26_0.G = -9.82
curved_guide_26_0.set_AT(['7.57345916228e-10', '0', '0.500 + u + 6e-5'], RELATIVE="PREVIOUS")
curved_guide_26_0.set_ROTATED(['0', 'benderAngle', '0'], RELATIVE="PREVIOUS")

curved_guide_27_0 = EGCESE.add_component("curved_guide_27_0", "Guide_gravity")
curved_guide_27_0.w1 = 0.029534
curved_guide_27_0.h1 = 0.047514
curved_guide_27_0.w2 = 0.029534
curved_guide_27_0.h2 = 0.047514
curved_guide_27_0.l = 0.5
curved_guide_27_0.R0 = 0.990000
curved_guide_27_0.Qc = 0.021700
curved_guide_27_0.alpha = 3.100000
curved_guide_27_0.W = 0.003000
curved_guide_27_0.mleft = 3.000000
curved_guide_27_0.mright = 3.500000
curved_guide_27_0.mtop = 2.500000
curved_guide_27_0.mbottom = 2.500000
curved_guide_27_0.G = -9.82
curved_guide_27_0.set_AT(['7.57345916228e-10', '0', '0.500 + u + 6e-5'], RELATIVE="PREVIOUS")
curved_guide_27_0.set_ROTATED(['0', 'benderAngle', '0'], RELATIVE="PREVIOUS")

curved_guide_28_0 = EGCESE.add_component("curved_guide_28_0", "Guide_gravity")
curved_guide_28_0.w1 = 0.029534
curved_guide_28_0.h1 = 0.047514
curved_guide_28_0.w2 = 0.029534
curved_guide_28_0.h2 = 0.047514
curved_guide_28_0.l = 0.5
curved_guide_28_0.R0 = 0.990000
curved_guide_28_0.Qc = 0.021700
curved_guide_28_0.alpha = 3.100000
curved_guide_28_0.W = 0.003000
curved_guide_28_0.mleft = 3.000000
curved_guide_28_0.mright = 3.500000
curved_guide_28_0.mtop = 2.500000
curved_guide_28_0.mbottom = 2.500000
curved_guide_28_0.G = -9.82
curved_guide_28_0.set_AT(['7.57345916228e-10', '0', '0.500 + u + 6e-5'], RELATIVE="PREVIOUS")
curved_guide_28_0.set_ROTATED(['0', 'benderAngle', '0'], RELATIVE="PREVIOUS")

curved_guide_29_0 = EGCESE.add_component("curved_guide_29_0", "Guide_gravity")
curved_guide_29_0.w1 = 0.029534
curved_guide_29_0.h1 = 0.047514
curved_guide_29_0.w2 = 0.029534
curved_guide_29_0.h2 = 0.047514
curved_guide_29_0.l = 0.5
curved_guide_29_0.R0 = 0.990000
curved_guide_29_0.Qc = 0.021700
curved_guide_29_0.alpha = 3.100000
curved_guide_29_0.W = 0.003000
curved_guide_29_0.mleft = 3.000000
curved_guide_29_0.mright = 3.500000
curved_guide_29_0.mtop = 2.500000
curved_guide_29_0.mbottom = 2.500000
curved_guide_29_0.G = -9.82
curved_guide_29_0.set_AT(['7.57345916228e-10', '0', '0.500 + u + 6e-5'], RELATIVE="PREVIOUS")
curved_guide_29_0.set_ROTATED(['0', 'benderAngle', '0'], RELATIVE="PREVIOUS")

curved_guide_30_0 = EGCESE.add_component("curved_guide_30_0", "Guide_gravity")
curved_guide_30_0.w1 = 0.029534
curved_guide_30_0.h1 = 0.047514
curved_guide_30_0.w2 = 0.029534
curved_guide_30_0.h2 = 0.047514
curved_guide_30_0.l = 0.5
curved_guide_30_0.R0 = 0.990000
curved_guide_30_0.Qc = 0.021700
curved_guide_30_0.alpha = 3.100000
curved_guide_30_0.W = 0.003000
curved_guide_30_0.mleft = 3.000000
curved_guide_30_0.mright = 3.500000
curved_guide_30_0.mtop = 2.500000
curved_guide_30_0.mbottom = 2.500000
curved_guide_30_0.G = -9.82
curved_guide_30_0.set_AT(['7.57345916228e-10', '0', '0.500 + u + 6e-5'], RELATIVE="PREVIOUS")
curved_guide_30_0.set_ROTATED(['0', 'benderAngle', '0'], RELATIVE="PREVIOUS")

curved_guide_31_0 = EGCESE.add_component("curved_guide_31_0", "Guide_gravity")
curved_guide_31_0.w1 = 0.029534
curved_guide_31_0.h1 = 0.047514
curved_guide_31_0.w2 = 0.029534
curved_guide_31_0.h2 = 0.047514
curved_guide_31_0.l = 0.5
curved_guide_31_0.R0 = 0.990000
curved_guide_31_0.Qc = 0.021700
curved_guide_31_0.alpha = 3.100000
curved_guide_31_0.W = 0.003000
curved_guide_31_0.mleft = 3.000000
curved_guide_31_0.mright = 3.500000
curved_guide_31_0.mtop = 2.500000
curved_guide_31_0.mbottom = 2.500000
curved_guide_31_0.G = -9.82
curved_guide_31_0.set_AT(['7.57345916228e-10', '0', '0.500 + u + 6e-5'], RELATIVE="PREVIOUS")
curved_guide_31_0.set_ROTATED(['0', 'benderAngle', '0'], RELATIVE="PREVIOUS")

curved_guide_32_0 = EGCESE.add_component("curved_guide_32_0", "Guide_gravity")
curved_guide_32_0.w1 = 0.029534
curved_guide_32_0.h1 = 0.047514
curved_guide_32_0.w2 = 0.029534
curved_guide_32_0.h2 = 0.047514
curved_guide_32_0.l = 0.5
curved_guide_32_0.R0 = 0.990000
curved_guide_32_0.Qc = 0.021700
curved_guide_32_0.alpha = 3.100000
curved_guide_32_0.W = 0.003000
curved_guide_32_0.mleft = 3.000000
curved_guide_32_0.mright = 3.500000
curved_guide_32_0.mtop = 2.500000
curved_guide_32_0.mbottom = 2.500000
curved_guide_32_0.G = -9.82
curved_guide_32_0.set_AT(['7.57345916228e-10', '0', '0.500 + u + 6e-5'], RELATIVE="PREVIOUS")
curved_guide_32_0.set_ROTATED(['0', 'benderAngle', '0'], RELATIVE="PREVIOUS")

curved_guide_33_0 = EGCESE.add_component("curved_guide_33_0", "Guide_gravity")
curved_guide_33_0.w1 = 0.029534
curved_guide_33_0.h1 = 0.047514
curved_guide_33_0.w2 = 0.029534
curved_guide_33_0.h2 = 0.047514
curved_guide_33_0.l = 0.5
curved_guide_33_0.R0 = 0.990000
curved_guide_33_0.Qc = 0.021700
curved_guide_33_0.alpha = 3.100000
curved_guide_33_0.W = 0.003000
curved_guide_33_0.mleft = 3.000000
curved_guide_33_0.mright = 3.500000
curved_guide_33_0.mtop = 2.500000
curved_guide_33_0.mbottom = 2.500000
curved_guide_33_0.G = -9.82
curved_guide_33_0.set_AT(['7.57345916228e-10', '0', '0.500 + u + 6e-5'], RELATIVE="PREVIOUS")
curved_guide_33_0.set_ROTATED(['0', 'benderAngle', '0'], RELATIVE="PREVIOUS")

curved_guide_34_0 = EGCESE.add_component("curved_guide_34_0", "Guide_gravity")
curved_guide_34_0.w1 = 0.029534
curved_guide_34_0.h1 = 0.047514
curved_guide_34_0.w2 = 0.029534
curved_guide_34_0.h2 = 0.047514
curved_guide_34_0.l = 0.5
curved_guide_34_0.R0 = 0.990000
curved_guide_34_0.Qc = 0.021700
curved_guide_34_0.alpha = 3.100000
curved_guide_34_0.W = 0.003000
curved_guide_34_0.mleft = 3.000000
curved_guide_34_0.mright = 3.500000
curved_guide_34_0.mtop = 2.500000
curved_guide_34_0.mbottom = 2.500000
curved_guide_34_0.G = -9.82
curved_guide_34_0.set_AT(['7.57345916228e-10', '0', '0.500 + u + 6e-5'], RELATIVE="PREVIOUS")
curved_guide_34_0.set_ROTATED(['0', 'benderAngle', '0'], RELATIVE="PREVIOUS")

curved_guide_35_0 = EGCESE.add_component("curved_guide_35_0", "Guide_gravity")
curved_guide_35_0.w1 = 0.029534
curved_guide_35_0.h1 = 0.047514
curved_guide_35_0.w2 = 0.029534
curved_guide_35_0.h2 = 0.047514
curved_guide_35_0.l = 0.5
curved_guide_35_0.R0 = 0.990000
curved_guide_35_0.Qc = 0.021700
curved_guide_35_0.alpha = 3.100000
curved_guide_35_0.W = 0.003000
curved_guide_35_0.mleft = 3.000000
curved_guide_35_0.mright = 3.500000
curved_guide_35_0.mtop = 2.500000
curved_guide_35_0.mbottom = 2.500000
curved_guide_35_0.G = -9.82
curved_guide_35_0.set_AT(['7.57345916228e-10', '0', '0.500 + u + 6e-5'], RELATIVE="PREVIOUS")
curved_guide_35_0.set_ROTATED(['0', 'benderAngle', '0'], RELATIVE="PREVIOUS")

curved_guide_36_0 = EGCESE.add_component("curved_guide_36_0", "Guide_gravity")
curved_guide_36_0.w1 = 0.029534
curved_guide_36_0.h1 = 0.047514
curved_guide_36_0.w2 = 0.029534
curved_guide_36_0.h2 = 0.047514
curved_guide_36_0.l = 0.495689131828
curved_guide_36_0.R0 = 0.990000
curved_guide_36_0.Qc = 0.021700
curved_guide_36_0.alpha = 3.100000
curved_guide_36_0.W = 0.003000
curved_guide_36_0.mleft = 3.000000
curved_guide_36_0.mright = 3.500000
curved_guide_36_0.mtop = 2.500000
curved_guide_36_0.mbottom = 2.500000
curved_guide_36_0.G = -9.82
curved_guide_36_0.set_AT(['7.57345916228e-10', '0', '0.500 + u + 6e-5'], RELATIVE="PREVIOUS")
curved_guide_36_0.set_ROTATED(['0', 'benderAngle', '0'], RELATIVE="PREVIOUS")

EndOfelement_4 = EGCESE.add_component("EndOfelement_4", "Arm")
EndOfelement_4.set_AT(['7.57345916228e-10', '0', '0.495689132 + u'], RELATIVE="PREVIOUS")

Div2d_AfterBender = EGCESE.add_component("Div2d_AfterBender", "Divergence_monitor")
Div2d_AfterBender.nh = 200
Div2d_AfterBender.nv = 200
Div2d_AfterBender.filename = "\"Div2d_AfterBender.dat\""
Div2d_AfterBender.xwidth = 0.1
Div2d_AfterBender.yheight = 0.1
Div2d_AfterBender.maxdiv_h = 2.5
Div2d_AfterBender.maxdiv_v = 1.5
Div2d_AfterBender.restore_neutron = 1
Div2d_AfterBender.set_AT(['0', ' 0', 'u'], RELATIVE="PREVIOUS")

ToFAfterBender = EGCESE.add_component("ToFAfterBender", "TOF_monitor")
ToFAfterBender.nt = 500
ToFAfterBender.filename = "\"ToFAfterBender.dat\""
ToFAfterBender.xwidth = 0.2
ToFAfterBender.yheight = 0.2
ToFAfterBender.tmax = 8e4
ToFAfterBender.restore_neutron = 1
ToFAfterBender.set_AT(['0', ' 0', 'u'], RELATIVE="PREVIOUS")

elliptical_guide_gravity3 = EGCESE.add_component("elliptical_guide_gravity3", "Elliptic_guide_gravity")
elliptical_guide_gravity3.l = 24.928800
elliptical_guide_gravity3.xwidth = 0.060000
elliptical_guide_gravity3.yheight = 0.090000
elliptical_guide_gravity3.linxw = 3.709727
elliptical_guide_gravity3.loutxw = 28.638527
elliptical_guide_gravity3.linyh = 4.423828
elliptical_guide_gravity3.loutyh = 29.352628
elliptical_guide_gravity3.dimensionsAt = "\"mid\""
elliptical_guide_gravity3.R0 = 0.990000
elliptical_guide_gravity3.Qc = 0.021700
elliptical_guide_gravity3.alpha = 3.100000
elliptical_guide_gravity3.seglength = C_elementLength3S
elliptical_guide_gravity3.W=0.003000
elliptical_guide_gravity3.mvaluesright = C_mValues3horizontalS
elliptical_guide_gravity3.mvaluesleft = C_mValues3horizontalS
elliptical_guide_gravity3.mvaluestop = C_mValues3verticalS
elliptical_guide_gravity3.mvaluesbottom = C_mValues3verticalS
elliptical_guide_gravity3.nSegments = C_elementLength3S.vector
elliptical_guide_gravity3.set_AT(['0', '0', ' u'], RELATIVE="EndOfelement_4")
elliptical_guide_gravity3.set_ROTATED(['0', '0', '0'], RELATIVE="EndOfelement_4")

EndOfelement_3 = EGCESE.add_component("EndOfelement_3", "Arm")
EndOfelement_3.set_AT(['0', '0', '24.928800+u'], RELATIVE="PREVIOUS")

Div2d_BeforeStraight = EGCESE.add_component("Div2d_BeforeStraight", "Divergence_monitor")
Div2d_BeforeStraight.nh = 200
Div2d_BeforeStraight.nv = 200
Div2d_BeforeStraight.filename = "\"Div2d_BeforeStraight.dat\""
Div2d_BeforeStraight.xwidth = 0.1
Div2d_BeforeStraight.yheight = 0.1
Div2d_BeforeStraight.maxdiv_h = 1
Div2d_BeforeStraight.maxdiv_v = 1
Div2d_BeforeStraight.restore_neutron = 1
Div2d_BeforeStraight.set_AT(['0', ' 0', 'u'], RELATIVE="PREVIOUS")

straight_guide_2_1 = EGCESE.add_component("straight_guide_2_1", "Guide_gravity")
straight_guide_2_1.w1 = 0.060000
straight_guide_2_1.h1 = 0.090000
straight_guide_2_1.w2 = 0.060000
straight_guide_2_1.h2 = 0.090000
straight_guide_2_1.l = "chopBWPos-startXposition_straight-BW_chopGap/2"
straight_guide_2_1.R0 = 0.990000
straight_guide_2_1.Qc = 0.021700
straight_guide_2_1.alpha = 3.100000
straight_guide_2_1.W = 0.003000
straight_guide_2_1.mleft = 1.500000
straight_guide_2_1.mright = 1.500000
straight_guide_2_1.mtop = 1.000000
straight_guide_2_1.mbottom = 1.000000
straight_guide_2_1.G = -9.82
straight_guide_2_1.set_AT(['0', '0', ' u'], RELATIVE="PREVIOUS")
straight_guide_2_1.set_ROTATED(['0', '0', '0'], RELATIVE="PREVIOUS")

L_monBeforeBWC = EGCESE.add_component("L_monBeforeBWC", "L_monitor")
L_monBeforeBWC.nL = 100
L_monBeforeBWC.filename = "\"L_monBeforeBWC.dat\""
L_monBeforeBWC.xwidth = 0.2
L_monBeforeBWC.yheight = 0.2
L_monBeforeBWC.Lmin = "lambda_0/2.0"
L_monBeforeBWC.Lmax = "lambda_1*2.0"
L_monBeforeBWC.restore_neutron = 1
L_monBeforeBWC.set_AT(['0', ' 0', ' chopBWPos-startXposition_straight-BW_chopGap/2+u'], RELATIVE="PREVIOUS")

ToFBeforeBWC = EGCESE.add_component("ToFBeforeBWC", "TOF_monitor")
ToFBeforeBWC.nt = 300
ToFBeforeBWC.filename = "\"ToFBeforeBWC.dat\""
ToFBeforeBWC.xwidth = 0.2
ToFBeforeBWC.yheight = 0.2
ToFBeforeBWC.tmax = "3.5*72.0*1e6/v_0"
ToFBeforeBWC.restore_neutron = 1
ToFBeforeBWC.set_AT(['0', ' 0', ' u'], RELATIVE="PREVIOUS")

BWC1 = EGCESE.add_component("BWC1", "DiskChopper")
BWC1.theta_0 = "BWopen"
BWC1.radius = 0.35
BWC1.yheight = "0.090+2*ChopTransE2"
BWC1.nu = 14
BWC1.nslit = 1
BWC1.delay = "chopBWOffset"
BWC1.set_AT(['0', ' 0', ' BW_chopGap/2+u'], RELATIVE="PREVIOUS")

BWC2 = EGCESE.add_component("BWC2", "DiskChopper")
BWC2.theta_0 = "BWopen"
BWC2.radius = 0.35
BWC2.yheight = "0.090+2*ChopTransE2"
BWC2.nu = -14
BWC2.nslit = 1
BWC2.delay = "chopBWOffset"
BWC2.set_AT(['0', ' 0', ' u'], RELATIVE="PREVIOUS")

ToFAfterBWC = EGCESE.add_component("ToFAfterBWC", "TOF_monitor")
ToFAfterBWC.nt = 300
ToFAfterBWC.filename = "\"ToFAfterBWC.dat\""
ToFAfterBWC.xwidth = 0.2
ToFAfterBWC.yheight = 0.2
ToFAfterBWC.tmax = "3.5*72.0*1.0e6/v_0"
ToFAfterBWC.restore_neutron = 1
ToFAfterBWC.set_AT(['0', ' 0', ' u'], RELATIVE="PREVIOUS")

L_monAfterBWC = EGCESE.add_component("L_monAfterBWC", "L_monitor")
L_monAfterBWC.nL = 100
L_monAfterBWC.filename = "\"L_monAfterBWC.dat\""
L_monAfterBWC.xwidth = 0.2
L_monAfterBWC.yheight = 0.2
L_monAfterBWC.Lmin = "lambda_0/2.0"
L_monAfterBWC.Lmax = "lambda_1*2.0"
L_monAfterBWC.restore_neutron = 1
L_monAfterBWC.set_AT(['0', ' 0', ' u'], RELATIVE="PREVIOUS")

straight_guide_2_2 = EGCESE.add_component("straight_guide_2_2", "Guide_gravity")
straight_guide_2_2.w1 = 0.060000
straight_guide_2_2.h1 = 0.090000
straight_guide_2_2.w2 = 0.060000
straight_guide_2_2.h2 = 0.090000
straight_guide_2_2.l = "length2-chopBWPos+startXposition_straight-BW_chopGap/2"
straight_guide_2_2.R0 = 0.990000
straight_guide_2_2.Qc = 0.021700
straight_guide_2_2.alpha = 3.100000
straight_guide_2_2.W = 0.003000
straight_guide_2_2.mleft = 1.500000
straight_guide_2_2.mright = 1.500000
straight_guide_2_2.mtop = 1.000000
straight_guide_2_2.mbottom = 1.000000
straight_guide_2_2.G = -9.82
straight_guide_2_2.set_AT(['0', '0', ' BW_chopGap/2'], RELATIVE="PREVIOUS")
straight_guide_2_2.set_ROTATED(['0', '0', '0'], RELATIVE="PREVIOUS")

EndOfelement_2 = EGCESE.add_component("EndOfelement_2", "Arm")
EndOfelement_2.set_AT(['0', '0', 'length2-chopBWPos+startXposition_straight-BW_chopGap/2 + u'], RELATIVE="straight_guide_2_2")

elliptical_guide_gravity1_1 = EGCESE.add_component("elliptical_guide_gravity1_1", "Elliptic_guide_gravity")
elliptical_guide_gravity1_1.l = "length1-DivSlit3Pos-DivSlit3Gap/2.0+sample_dist"
elliptical_guide_gravity1_1.xwidth = "2*smallaxis_x1"
elliptical_guide_gravity1_1.yheight = "2*smallaxis_y1"
elliptical_guide_gravity1_1.linxw = "Linx1"
elliptical_guide_gravity1_1.loutxw = "Loutx1+DivSlit3Pos+DivSlit3Gap/2.0-sample_dist"
elliptical_guide_gravity1_1.linyh = "Liny1"
elliptical_guide_gravity1_1.loutyh = "Louty1+DivSlit3Pos+DivSlit3Gap/2.0-sample_dist"
elliptical_guide_gravity1_1.dimensionsAt = "\"mid\""
elliptical_guide_gravity1_1.R0 = 0.990000
elliptical_guide_gravity1_1.Qc = 0.021700
elliptical_guide_gravity1_1.alpha = 3.100000
elliptical_guide_gravity1_1.seglength = C_elementLength1_part_1
elliptical_guide_gravity1_1.W=0.003000
elliptical_guide_gravity1_1.mvaluesright = C_mValues1horizontal_part_1
elliptical_guide_gravity1_1.mvaluesleft = C_mValues1horizontal_part_1
elliptical_guide_gravity1_1.mvaluestop = C_mValues1vertical_part_1
elliptical_guide_gravity1_1.mvaluesbottom = C_mValues1vertical_part_1
elliptical_guide_gravity1_1.nSegments = C_elementLength1_part_1.vector
elliptical_guide_gravity1_1.set_AT(['0', '0', ' u'], RELATIVE="EndOfelement_2")
elliptical_guide_gravity1_1.set_ROTATED(['0', '0', '0'], RELATIVE="PREVIOUS")

DiwJaw3 = EGCESE.add_component("DiwJaw3", "Slit")
DiwJaw3.xwidth = "DivSlit3_width"
DiwJaw3.yheight = 1
DiwJaw3.set_AT(['0', '0', ' 2*u+length1-(DivSlit3Pos-sample_dist)'], RELATIVE="EndOfelement_2")

elliptical_guide_gravity1_2 = EGCESE.add_component("elliptical_guide_gravity1_2", "Elliptic_guide_gravity")
elliptical_guide_gravity1_2.l = "DivSlit3Pos-DivSlit2Gap/2.0-DivSlit3Gap/2.0-DivSlit2Pos"
elliptical_guide_gravity1_2.xwidth = "2*smallaxis_x1"
elliptical_guide_gravity1_2.yheight = "2*smallaxis_y1"
elliptical_guide_gravity1_2.linxw = "Linx1+length1-(DivSlit3Pos-DivSlit3Gap/2.0-sample_dist)"
elliptical_guide_gravity1_2.loutxw = "Loutx1+DivSlit2Pos+DivSlit2Gap/2.0-sample_dist"
elliptical_guide_gravity1_2.linyh = "Liny1+length1-(DivSlit3Pos-DivSlit3Gap/2.0-sample_dist)"
elliptical_guide_gravity1_2.loutyh = "Louty1+DivSlit2Pos+DivSlit2Gap/2.0-sample_dist"
elliptical_guide_gravity1_2.dimensionsAt = "\"mid\""
elliptical_guide_gravity1_2.R0 = 0.990000
elliptical_guide_gravity1_2.Qc = 0.021700
elliptical_guide_gravity1_2.alpha = 3.100000
elliptical_guide_gravity1_2.seglength = C_elementLength1_part_2
elliptical_guide_gravity1_2.W=0.003000
elliptical_guide_gravity1_2.mvaluesright = C_mValues1horizontal_part_2
elliptical_guide_gravity1_2.mvaluesleft = C_mValues1horizontal_part_2
elliptical_guide_gravity1_2.mvaluestop = C_mValues1vertical_part_2
elliptical_guide_gravity1_2.mvaluesbottom = C_mValues1vertical_part_2
elliptical_guide_gravity1_2.nSegments = C_elementLength1_part_2.vector

elliptical_guide_gravity1_2.set_AT(['0', '0', ' 3*u+length1-(DivSlit3Pos-DivSlit3Gap/2.0-sample_dist)'], RELATIVE="EndOfelement_2")
elliptical_guide_gravity1_2.set_ROTATED(['0', '0', '0'], RELATIVE="PREVIOUS")

DiwJaw2 = EGCESE.add_component("DiwJaw2", "Slit")
DiwJaw2.xwidth = "DivSlit2_width"
DiwJaw2.yheight = 1
DiwJaw2.set_AT(['0', '0', ' u+length1-(DivSlit2Pos-sample_dist)'], RELATIVE="EndOfelement_2")

elliptical_guide_gravity1_3 = EGCESE.add_component("elliptical_guide_gravity1_3", "Elliptic_guide_gravity")
elliptical_guide_gravity1_3.l = "DivSlit2Pos-DivSlit1Gap/2.0-DivSlit2Gap/2.0-DivSlit1Pos"
elliptical_guide_gravity1_3.xwidth = "2*smallaxis_x1"
elliptical_guide_gravity1_3.yheight = "2*smallaxis_y1"
elliptical_guide_gravity1_3.linxw = "Linx1+length1-(DivSlit2Pos-DivSlit2Gap/2.0-sample_dist)"
elliptical_guide_gravity1_3.loutxw = "Loutx1+DivSlit1Pos+DivSlit1Gap/2.0-sample_dist"
elliptical_guide_gravity1_3.linyh = "Liny1+length1-(DivSlit2Pos-DivSlit2Gap/2.0-sample_dist)"
elliptical_guide_gravity1_3.loutyh = "Louty1+DivSlit1Pos+DivSlit1Gap/2.0-sample_dist"
elliptical_guide_gravity1_3.dimensionsAt = "\"mid\""
elliptical_guide_gravity1_3.R0 = 0.990000
elliptical_guide_gravity1_3.Qc = 0.021700
elliptical_guide_gravity1_3.alpha = 3.100000
elliptical_guide_gravity1_3.seglength = C_elementLength1_part_3
elliptical_guide_gravity1_3.W=0.003000
elliptical_guide_gravity1_3.mvaluesright = C_mValues1horizontal_part_3
elliptical_guide_gravity1_3.mvaluesleft = C_mValues1horizontal_part_3
elliptical_guide_gravity1_3.mvaluestop = C_mValues1vertical_part_3
elliptical_guide_gravity1_3.mvaluesbottom = C_mValues1vertical_part_3
elliptical_guide_gravity1_3.nSegments = C_elementLength1_part_3.vector
elliptical_guide_gravity1_3.set_AT(['0', '0', ' 4*u+length1-(DivSlit2Pos-DivSlit2Gap/2.0-sample_dist)'], RELATIVE="EndOfelement_2")
elliptical_guide_gravity1_3.set_ROTATED(['0', '0', '0'], RELATIVE="PREVIOUS")

DiwJaw1 = EGCESE.add_component("DiwJaw1", "Slit")
DiwJaw1.xwidth = "DivSlit1_width"
DiwJaw1.yheight = 1
DiwJaw1.set_AT(['0', '0', ' 5*u+length1-(DivSlit1Pos-sample_dist)'], RELATIVE="EndOfelement_2")

elliptical_guide_gravity1_4 = EGCESE.add_component("elliptical_guide_gravity1_4", "Elliptic_guide_gravity")
elliptical_guide_gravity1_4.l = "DivSlit1Pos-DivSlit1Gap/2.0-sample_dist"
elliptical_guide_gravity1_4.xwidth = "2*smallaxis_x1"
elliptical_guide_gravity1_4.yheight = "2*smallaxis_y1"
elliptical_guide_gravity1_4.linxw = "Linx1+length1-(DivSlit1Pos-DivSlit1Gap/2.0-sample_dist)"
elliptical_guide_gravity1_4.loutxw = "Loutx1"
elliptical_guide_gravity1_4.linyh = "Liny1+length1-(DivSlit1Pos-DivSlit1Gap/2.0-sample_dist)"
elliptical_guide_gravity1_4.loutyh = "Louty1"
elliptical_guide_gravity1_4.dimensionsAt = "\"mid\""
elliptical_guide_gravity1_4.R0 = 0.990000
elliptical_guide_gravity1_4.Qc = 0.021700
elliptical_guide_gravity1_4.alpha = 3.100000
elliptical_guide_gravity1_4.seglength = C_elementLength1_part_4
elliptical_guide_gravity1_4.W=0.003000
elliptical_guide_gravity1_4.mvaluesright = C_mValues1horizontal_part_4
elliptical_guide_gravity1_4.mvaluesleft = C_mValues1horizontal_part_4
elliptical_guide_gravity1_4.mvaluestop = C_mValues1vertical_part_4
elliptical_guide_gravity1_4.mvaluesbottom = C_mValues1vertical_part_4
elliptical_guide_gravity1_4.nSegments = C_elementLength1_part_4.vector
elliptical_guide_gravity1_4.set_AT(['0', '0', ' 6*u+length1-(DivSlit1Pos-DivSlit1Gap/2.0-sample_dist)'], RELATIVE="EndOfelement_2")
elliptical_guide_gravity1_4.set_ROTATED(['0', '0', '0'], RELATIVE="PREVIOUS")

EndOfelement_1 = EGCESE.add_component("EndOfelement_1", "Arm")
EndOfelement_1.set_AT(['0', '0', 'DivSlit1Pos-DivSlit1Gap/2.0-sample_dist +u'], RELATIVE="PREVIOUS")

VirtualOutput = EGCESE.add_component("VirtualOutput", "Virtual_output")
VirtualOutput.filename = "\"VirtualOutput_endOfGuide.dat\""
VirtualOutput.set_WHEN("makeVirtualSource==1")
VirtualOutput.set_AT(['0', ' 0', 'u'], RELATIVE="PREVIOUS")

DiwJaw0 = EGCESE.add_component("DiwJaw0", "Slit")
DiwJaw0.xwidth = "DivSlit0_width"
DiwJaw0.yheight = 1
DiwJaw0.set_AT(['0', '0', ' 7*u+length1+DivSlit0Gap/2.0'], RELATIVE="EndOfelement_2")

Lmon_guide_end = EGCESE.add_component("Lmon_guide_end", "L_monitor")
Lmon_guide_end.nL = 300
Lmon_guide_end.filename = "\"Lmon_guide_end\""
Lmon_guide_end.xwidth = 0.027704
Lmon_guide_end.yheight = 0.027704
Lmon_guide_end.Lmin = 0.100000
Lmon_guide_end.Lmax = 8.000000
Lmon_guide_end.restore_neutron = 1
Lmon_guide_end.set_AT(['0', ' 0', 'u'], RELATIVE="PREVIOUS")

Div2d_sample_B = EGCESE.add_component("Div2d_sample_B", "Divergence_monitor")
Div2d_sample_B.nh = 200
Div2d_sample_B.nv = 200
Div2d_sample_B.filename = "\"Div2d_sample_B\""
Div2d_sample_B.xwidth = "sampleSizeX"
Div2d_sample_B.yheight = "sampleSizeY"
Div2d_sample_B.maxdiv_h = 0.750000
Div2d_sample_B.maxdiv_v = 0.750000
Div2d_sample_B.restore_neutron = 1
Div2d_sample_B.append_EXTEND("x_div = RAD2DEG*atan2(vx,vz);")
Div2d_sample_B.append_EXTEND("y_div = RAD2DEG*atan2(vy,vz);")
Div2d_sample_B.append_EXTEND("if (SCATTERED) flag=1; else flag=0;")
Div2d_sample_B.set_AT(['0', ' 0', '0.580000'], RELATIVE="EndOfelement_1")

Div2d_sample = EGCESE.add_component("Div2d_sample", "Divergence_monitor")
Div2d_sample.nh = 100
Div2d_sample.nv = 100
Div2d_sample.filename = "\"Div2d_sample\""
Div2d_sample.xwidth = "sampleSizeX"
Div2d_sample.yheight = "sampleSizeY"
Div2d_sample.maxdiv_h = 2.250000
Div2d_sample.maxdiv_v = 2.250000
Div2d_sample.restore_neutron = 1
Div2d_sample.set_AT(['0', ' 0', 'u'], RELATIVE="PREVIOUS")

PSD_sample_large = EGCESE.add_component("PSD_sample_large", "PSD_monitor")
PSD_sample_large.nx = 60
PSD_sample_large.ny = 60
PSD_sample_large.filename = "\"PSD_sample_large\""
PSD_sample_large.xwidth = "6*sampleSizeX"
PSD_sample_large.yheight = "6*sampleSizeY"
PSD_sample_large.restore_neutron = 1
PSD_sample_large.set_AT(['0', ' 0', 'u'], RELATIVE="PREVIOUS")

PSD_sample_small = EGCESE.add_component("PSD_sample_small", "PSD_monitor")
PSD_sample_small.nx = 20
PSD_sample_small.ny = 20
PSD_sample_small.filename = "\"PSD_sample_small\""
PSD_sample_small.xwidth = "sampleSizeX"
PSD_sample_small.yheight = "sampleSizeY"
PSD_sample_small.restore_neutron = 1
PSD_sample_small.set_AT(['0', ' 0', 'u'], RELATIVE="PREVIOUS")
