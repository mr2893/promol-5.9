'''
FUNC:Jfa_1d8h_3_1_3_33
PDB:1d8h
EC:3.1.3.33
RESI:arg,glu,lys,arg
LOCI:a-393,433,456,458;
'''
jesstemp0 ='n.  ne '
jesstemp1 ='r. arg'
cmd.select('jessatom0', '(('+jesstemp0+')&('+jesstemp1+'))')
jesstemp2 ='n.  nh1'
jesstemp3 ='n.  nh2'
jesstemp4 ='r. arg'
jesstemp5 ='jessatom0 x. %s'%(2.323000+(d*0.300000))
jesstemp6 ='br. jessatom0'
cmd.select('jessatom1', '((('+jesstemp2+')|('+jesstemp3+'))&('+jesstemp4+')&('+jesstemp5+')&('+jesstemp6+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(2.323000+(d*0.300000)))
jesstemp7 ='n.  nh2'
jesstemp8 ='n.  nh1'
jesstemp9 ='jessatom0 x. %s'%(2.353300+(d*0.300000))
jesstemp10 ='br. jessatom0'
jesstemp11 ='jessatom1 x. %s'%(2.363400+(d*0.300000))
cmd.select('jessatom2', '((('+jesstemp7+')|('+jesstemp8+'))&('+jesstemp4+')&('+jesstemp9+')&('+jesstemp10+')&('+jesstemp11+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(2.353300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.363400+(d*0.300000)))
jesstemp12 ='n.  cd '
jesstemp13 ='r. glu'
jesstemp14 ='r. asp'
jesstemp15 ='jessatom0 x. %s'%(6.918500+(d*0.300000))
jesstemp16 ='jessatom1 x. %s'%(6.231700+(d*0.300000))
jesstemp17 ='jessatom2 x. %s'%(5.161100+(d*0.300000))
cmd.select('jessatom3', '(((('+jesstemp12+')&('+jesstemp13+'))|(('+jesstemp12+')&('+jesstemp14+')))&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(6.918500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(6.231700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(5.161100+(d*0.300000)))
jesstemp18 ='n.  oe1'
jesstemp19 ='n.  oe2'
jesstemp20 ='n.  od1'
jesstemp21 ='n.  od2'
jesstemp22 ='jessatom0 x. %s'%(6.322600+(d*0.300000))
jesstemp23 ='jessatom1 x. %s'%(5.292400+(d*0.300000))
jesstemp24 ='jessatom2 x. %s'%(4.454100+(d*0.300000))
jesstemp25 ='jessatom3 x. %s'%(1.282700+(d*0.300000))
jesstemp26 ='br. jessatom3'
cmd.select('jessatom4', '((((('+jesstemp18+')|('+jesstemp19+'))&('+jesstemp13+'))|((('+jesstemp20+')|('+jesstemp21+'))&('+jesstemp14+')))&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(6.322600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(5.292400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(4.454100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.282700+(d*0.300000)))
jesstemp27 ='n.  oe2'
jesstemp28 ='n.  oe1'
jesstemp29 ='n.  od2'
jesstemp30 ='n.  od1'
jesstemp31 ='jessatom0 x. %s'%(7.847700+(d*0.300000))
jesstemp32 ='jessatom1 x. %s'%(7.292200+(d*0.300000))
jesstemp33 ='jessatom2 x. %s'%(5.959000+(d*0.300000))
jesstemp34 ='jessatom3 x. %s'%(1.252400+(d*0.300000))
jesstemp35 ='br. jessatom3'
jesstemp36 ='jessatom4 x. %s'%(2.272500+(d*0.300000))
cmd.select('jessatom5', '((((('+jesstemp27+')|('+jesstemp28+'))&('+jesstemp13+'))|((('+jesstemp29+')|('+jesstemp30+'))&('+jesstemp14+')))&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(7.847700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(7.292200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(5.959000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(1.252400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.272500+(d*0.300000)))
jesstemp37 ='r. lys'
jesstemp38 ='jessatom0 x. %s'%(6.706400+(d*0.300000))
jesstemp39 ='jessatom1 x. %s'%(5.878200+(d*0.300000))
jesstemp40 ='jessatom2 x. %s'%(6.898300+(d*0.300000))
jesstemp41 ='jessatom3 x. %s'%(11.271600+(d*0.300000))
jesstemp42 ='jessatom4 x. %s'%(10.140400+(d*0.300000))
jesstemp43 ='jessatom5 x. %s'%(12.089700+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp12+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(6.706400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(5.878200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(6.898300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(11.271600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(10.140400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(12.089700+(d*0.300000)))
jesstemp44 ='n.  ce '
jesstemp45 ='jessatom0 x. %s'%(6.575100+(d*0.300000))
jesstemp46 ='jessatom1 x. %s'%(5.272200+(d*0.300000))
jesstemp47 ='jessatom2 x. %s'%(6.393300+(d*0.300000))
jesstemp48 ='jessatom3 x. %s'%(10.291900+(d*0.300000))
jesstemp49 ='jessatom4 x. %s'%(9.100100+(d*0.300000))
jesstemp50 ='jessatom5 x. %s'%(11.099900+(d*0.300000))
jesstemp51 ='jessatom6 x. %s'%(1.525100+(d*0.300000))
jesstemp52 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp44+')&('+jesstemp37+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+')&('+jesstemp49+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(6.575100+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(5.272200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(6.393300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(10.291900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(9.100100+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(11.099900+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.525100+(d*0.300000)))
jesstemp53 ='n.  nz '
jesstemp54 ='jessatom0 x. %s'%(6.938700+(d*0.300000))
jesstemp55 ='jessatom1 x. %s'%(5.686300+(d*0.300000))
jesstemp56 ='jessatom2 x. %s'%(6.292300+(d*0.300000))
jesstemp57 ='jessatom3 x. %s'%(9.958600+(d*0.300000))
jesstemp58 ='jessatom4 x. %s'%(8.776900+(d*0.300000))
jesstemp59 ='jessatom5 x. %s'%(10.635300+(d*0.300000))
jesstemp60 ='jessatom6 x. %s'%(2.444200+(d*0.300000))
jesstemp61 ='br. jessatom6'
jesstemp62 ='jessatom7 x. %s'%(1.515000+(d*0.300000))
cmd.select('jessatom8', '(('+jesstemp53+')&('+jesstemp37+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+')&('+jesstemp59+')&('+jesstemp60+')&('+jesstemp61+')&('+jesstemp62+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(6.938700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(5.686300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(6.292300+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(9.958600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(8.776900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(10.635300+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.444200+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(1.515000+(d*0.300000)))
jesstemp63 ='jessatom0 x. %s'%(10.150500+(d*0.300000))
jesstemp64 ='jessatom1 x. %s'%(8.494100+(d*0.300000))
jesstemp65 ='jessatom2 x. %s'%(8.908200+(d*0.300000))
jesstemp66 ='jessatom3 x. %s'%(11.009000+(d*0.300000))
jesstemp67 ='jessatom4 x. %s'%(9.807100+(d*0.300000))
jesstemp68 ='jessatom5 x. %s'%(11.463500+(d*0.300000))
jesstemp69 ='jessatom6 x. %s'%(5.938800+(d*0.300000))
jesstemp70 ='jessatom7 x. %s'%(4.848000+(d*0.300000))
jesstemp71 ='jessatom8 x. %s'%(3.817800+(d*0.300000))
cmd.select('jessatom9', '(('+jesstemp0+')&('+jesstemp4+')&('+jesstemp63+')&('+jesstemp64+')&('+jesstemp65+')&('+jesstemp66+')&('+jesstemp67+')&('+jesstemp68+')&('+jesstemp69+')&('+jesstemp70+')&('+jesstemp71+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom9 x. %s)'%(10.150500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom9 x. %s)'%(8.494100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom9 x. %s)'%(8.908200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom9 x. %s)'%(11.009000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom9 x. %s)'%(9.807100+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom9 x. %s)'%(11.463500+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom9 x. %s)'%(5.938800+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom9 x. %s)'%(4.848000+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom9 x. %s)'%(3.817800+(d*0.300000)))
jesstemp72 ='jessatom0 x. %s'%(8.504200+(d*0.300000))
jesstemp73 ='jessatom1 x. %s'%(6.857900+(d*0.300000))
jesstemp74 ='jessatom2 x. %s'%(6.969000+(d*0.300000))
jesstemp75 ='jessatom3 x. %s'%(8.817300+(d*0.300000))
jesstemp76 ='jessatom4 x. %s'%(7.645700+(d*0.300000))
jesstemp77 ='jessatom5 x. %s'%(9.261700+(d*0.300000))
jesstemp78 ='jessatom6 x. %s'%(5.847900+(d*0.300000))
jesstemp79 ='jessatom7 x. %s'%(4.595500+(d*0.300000))
jesstemp80 ='jessatom8 x. %s'%(3.434000+(d*0.300000))
jesstemp81 ='jessatom9 x. %s'%(2.232100+(d*0.300000))
jesstemp82 ='br. jessatom9'
cmd.select('jessatom10', '((('+jesstemp2+')|('+jesstemp3+'))&('+jesstemp4+')&('+jesstemp72+')&('+jesstemp73+')&('+jesstemp74+')&('+jesstemp75+')&('+jesstemp76+')&('+jesstemp77+')&('+jesstemp78+')&('+jesstemp79+')&('+jesstemp80+')&('+jesstemp81+')&('+jesstemp82+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom10 x. %s)'%(8.504200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom10 x. %s)'%(6.857900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom10 x. %s)'%(6.969000+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom10 x. %s)'%(8.817300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom10 x. %s)'%(7.645700+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom10 x. %s)'%(9.261700+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom10 x. %s)'%(5.847900+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom10 x. %s)'%(4.595500+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom10 x. %s)'%(3.434000+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom10 x. %s)'%(2.232100+(d*0.300000)))
jesstemp83 ='jessatom0 x. %s'%(8.251700+(d*0.300000))
jesstemp84 ='jessatom1 x. %s'%(6.393300+(d*0.300000))
jesstemp85 ='jessatom2 x. %s'%(7.251800+(d*0.300000))
jesstemp86 ='jessatom3 x. %s'%(9.635400+(d*0.300000))
jesstemp87 ='jessatom4 x. %s'%(8.372900+(d*0.300000))
jesstemp88 ='jessatom5 x. %s'%(10.312100+(d*0.300000))
jesstemp89 ='jessatom6 x. %s'%(4.595500+(d*0.300000))
jesstemp90 ='jessatom7 x. %s'%(3.171400+(d*0.300000))
jesstemp91 ='jessatom8 x. %s'%(2.676500+(d*0.300000))
jesstemp92 ='jessatom9 x. %s'%(2.444200+(d*0.300000))
jesstemp93 ='br. jessatom9'
jesstemp94 ='jessatom10 x. %s'%(2.272500+(d*0.300000))
cmd.select('jessatom11', '((('+jesstemp7+')|('+jesstemp8+'))&('+jesstemp4+')&('+jesstemp83+')&('+jesstemp84+')&('+jesstemp85+')&('+jesstemp86+')&('+jesstemp87+')&('+jesstemp88+')&('+jesstemp89+')&('+jesstemp90+')&('+jesstemp91+')&('+jesstemp92+')&('+jesstemp93+')&('+jesstemp94+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom11 x. %s)'%(8.251700+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom11 x. %s)'%(6.393300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom11 x. %s)'%(7.251800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom11 x. %s)'%(9.635400+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom11 x. %s)'%(8.372900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom11 x. %s)'%(10.312100+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom11 x. %s)'%(4.595500+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom11 x. %s)'%(3.171400+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom11 x. %s)'%(2.676500+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom11 x. %s)'%(2.444200+(d*0.300000)))
cmd.select('jessatom10', 'jessatom10 & (jessatom11 x. %s)'%(2.272500+(d*0.300000)))
cmd.select('Jfa_1d8h_3_1_3_33', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9|br. jessatom10|br. jessatom11')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
cmd.delete('jessatom9')
cmd.delete('jessatom10')
cmd.delete('jessatom11')
