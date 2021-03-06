'''
FUNC:A_1ca3_4_2_1_1
PDB:1ca3
EC:4.2.1.1
RESI:glu,thr
LOCI:a-106,199;
'''
cmd.select('thr1', 'n. CB&r. thr w. %s of n. CB&r. glu'%(d*7.09))
cmd.select('thr2', 'n. CB&r. thr w. %s of n. CG&r. glu'%(d*6.86))
cmd.select('thr3', 'n. CB&r. thr w. %s of n. CD&r. glu'%(d*5.54))
cmd.select('thr4', 'n. CB&r. thr w. %s of n. OE1&r. glu'%(d*4.82))
cmd.select('thr5', 'n. CB&r. thr w. %s of n. OE2&r. glu'%(d*5.81))
cmd.select('thr6', 'n. OG1&r. thr w. %s of n. CB&r. glu'%(d*7.20))
cmd.select('thr7', 'n. OG1&r. thr w. %s of n. CG&r. glu'%(d*6.62))
cmd.select('thr8', 'n. OG1&r. thr w. %s of n. CD&r. glu'%(d*5.21))
cmd.select('thr9', 'n. OG1&r. thr w. %s of n. OE1&r. glu'%(d*4.29))
cmd.select('thr10', 'n. OG1&r. thr w. %s of n. OE2&r. glu'%(d*5.57))
cmd.select('thr11', 'n. CG2&r. thr w. %s of n. CB&r. glu'%(d*6.91))
cmd.select('thr12', 'n. CG2&r. thr w. %s of n. CG&r. glu'%(d*7.06))
cmd.select('thr13', 'n. CG2&r. thr w. %s of n. CD&r. glu'%(d*6.06))
cmd.select('thr14', 'n. CG2&r. thr w. %s of n. OE1&r. glu'%(d*5.21))
cmd.select('thr15', 'n. CG2&r. thr w. %s of n. OE2&r. glu'%(d*6.69))
cmd.select('thr',' br. thr1&br. thr2&br. thr3&br. thr4&br. thr5&br. thr6&br. thr7&br. thr8&br. thr9&br. thr10&br. thr11&br. thr12&br. thr13&br. thr14&br. thr15')
cmd.delete('thr1')
cmd.delete('thr2')
cmd.delete('thr3')
cmd.delete('thr4')
cmd.delete('thr5')
cmd.delete('thr6')
cmd.delete('thr7')
cmd.delete('thr8')
cmd.delete('thr9')
cmd.delete('thr10')
cmd.delete('thr11')
cmd.delete('thr12')
cmd.delete('thr13')
cmd.delete('thr14')
cmd.delete('thr15')
cmd.select('glu1', 'n. CB&r. glu w. %s of n. CB&thr'%(d*7.09))
cmd.select('glu2', 'n. CB&r. glu w. %s of n. OG1&thr'%(d*7.20))
cmd.select('glu3', 'n. CB&r. glu w. %s of n. CG2&thr'%(d*6.91))
cmd.select('glu4', 'n. CG&r. glu w. %s of n. CB&thr'%(d*6.86))
cmd.select('glu5', 'n. CG&r. glu w. %s of n. OG1&thr'%(d*6.62))
cmd.select('glu6', 'n. CG&r. glu w. %s of n. CG2&thr'%(d*7.06))
cmd.select('glu7', 'n. CD&r. glu w. %s of n. CB&thr'%(d*5.54))
cmd.select('glu8', 'n. CD&r. glu w. %s of n. OG1&thr'%(d*5.21))
cmd.select('glu9', 'n. CD&r. glu w. %s of n. CG2&thr'%(d*6.06))
cmd.select('glu10', 'n. OE1&r. glu w. %s of n. CB&thr'%(d*4.82))
cmd.select('glu11', 'n. OE1&r. glu w. %s of n. OG1&thr'%(d*4.29))
cmd.select('glu12', 'n. OE1&r. glu w. %s of n. CG2&thr'%(d*5.21))
cmd.select('glu13', 'n. OE2&r. glu w. %s of n. CB&thr'%(d*5.81))
cmd.select('glu14', 'n. OE2&r. glu w. %s of n. OG1&thr'%(d*5.57))
cmd.select('glu15', 'n. OE2&r. glu w. %s of n. CG2&thr'%(d*6.69))
cmd.select('glu',' br. glu1&br. glu2&br. glu3&br. glu4&br. glu5&br. glu6&br. glu7&br. glu8&br. glu9&br. glu10&br. glu11&br. glu12&br. glu13&br. glu14&br. glu15')
cmd.delete('glu1')
cmd.delete('glu2')
cmd.delete('glu3')
cmd.delete('glu4')
cmd.delete('glu5')
cmd.delete('glu6')
cmd.delete('glu7')
cmd.delete('glu8')
cmd.delete('glu9')
cmd.delete('glu10')
cmd.delete('glu11')
cmd.delete('glu12')
cmd.delete('glu13')
cmd.delete('glu14')
cmd.delete('glu15')
cmd.select('A_1ca3_4_2_1_1', 'thr|glu')
cmd.delete('thr')
cmd.delete('glu')
