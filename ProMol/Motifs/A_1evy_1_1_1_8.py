'''
FUNC:A_1evy_1_1_1_8
PDB:1evy
EC:1.1.1.8
RESI:lys,thr
LOCI:a-210,267;
'''
cmd.select('lys1', 'n. CB&r. lys w. %s of n. CB&r. thr'%(d*6.39))
cmd.select('lys2', 'n. CB&r. lys w. %s of n. OG1&r. thr'%(d*6.48))
cmd.select('lys3', 'n. CB&r. lys w. %s of n. CG2&r. thr'%(d*6.42))
cmd.select('lys4', 'n. CG&r. lys w. %s of n. CB&r. thr'%(d*6.50))
cmd.select('lys5', 'n. CG&r. lys w. %s of n. OG1&r. thr'%(d*6.24))
cmd.select('lys6', 'n. CG&r. lys w. %s of n. CG2&r. thr'%(d*6.32))
cmd.select('lys7', 'n. CD&r. lys w. %s of n. CB&r. thr'%(d*6.05))
cmd.select('lys8', 'n. CD&r. lys w. %s of n. OG1&r. thr'%(d*5.34))
cmd.select('lys9', 'n. CD&r. lys w. %s of n. CG2&r. thr'%(d*6.19))
cmd.select('lys10', 'n. CE&r. lys w. %s of n. CB&r. thr'%(d*6.65))
cmd.select('lys11', 'n. CE&r. lys w. %s of n. OG1&r. thr'%(d*5.76))
cmd.select('lys12', 'n. CE&r. lys w. %s of n. CG2&r. thr'%(d*6.54))
cmd.select('lys13', 'n. NZ&r. lys w. %s of n. CB&r. thr'%(d*6.55))
cmd.select('lys14', 'n. NZ&r. lys w. %s of n. OG1&r. thr'%(d*5.35))
cmd.select('lys15', 'n. NZ&r. lys w. %s of n. CG2&r. thr'%(d*6.68))
cmd.select('lys',' br. lys1&br. lys2&br. lys3&br. lys4&br. lys5&br. lys6&br. lys7&br. lys8&br. lys9&br. lys10&br. lys11&br. lys12&br. lys13&br. lys14&br. lys15')
cmd.delete('lys1')
cmd.delete('lys2')
cmd.delete('lys3')
cmd.delete('lys4')
cmd.delete('lys5')
cmd.delete('lys6')
cmd.delete('lys7')
cmd.delete('lys8')
cmd.delete('lys9')
cmd.delete('lys10')
cmd.delete('lys11')
cmd.delete('lys12')
cmd.delete('lys13')
cmd.delete('lys14')
cmd.delete('lys15')
cmd.select('thr1', 'n. CB&r. thr w. %s of n. CB&lys'%(d*6.39))
cmd.select('thr2', 'n. CB&r. thr w. %s of n. CG&lys'%(d*6.50))
cmd.select('thr3', 'n. CB&r. thr w. %s of n. CD&lys'%(d*6.05))
cmd.select('thr4', 'n. CB&r. thr w. %s of n. CE&lys'%(d*6.65))
cmd.select('thr5', 'n. CB&r. thr w. %s of n. NZ&lys'%(d*6.55))
cmd.select('thr6', 'n. OG1&r. thr w. %s of n. CB&lys'%(d*6.48))
cmd.select('thr7', 'n. OG1&r. thr w. %s of n. CG&lys'%(d*6.24))
cmd.select('thr8', 'n. OG1&r. thr w. %s of n. CD&lys'%(d*5.34))
cmd.select('thr9', 'n. OG1&r. thr w. %s of n. CE&lys'%(d*5.76))
cmd.select('thr10', 'n. OG1&r. thr w. %s of n. NZ&lys'%(d*5.35))
cmd.select('thr11', 'n. CG2&r. thr w. %s of n. CB&lys'%(d*6.42))
cmd.select('thr12', 'n. CG2&r. thr w. %s of n. CG&lys'%(d*6.32))
cmd.select('thr13', 'n. CG2&r. thr w. %s of n. CD&lys'%(d*6.19))
cmd.select('thr14', 'n. CG2&r. thr w. %s of n. CE&lys'%(d*6.54))
cmd.select('thr15', 'n. CG2&r. thr w. %s of n. NZ&lys'%(d*6.68))
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
cmd.select('A_1evy_1_1_1_8', 'lys|thr')
cmd.delete('lys')
cmd.delete('thr')
