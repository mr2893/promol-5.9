'''
FUNC:A_1zym_2_7_3_9
PDB:1zym
EC:2.7.3.9
RESI:thr,his
LOCI:a-168,189;
'''
cmd.select('his1', 'n. CB&r. his w. %s of n. CB&r. thr'%(d*8.80))
cmd.select('his2', 'n. CB&r. his w. %s of n. OG1&r. thr'%(d*8.32))
cmd.select('his3', 'n. CB&r. his w. %s of n. CG2&r. thr'%(d*7.92))
cmd.select('his4', 'n. CG&r. his w. %s of n. CB&r. thr'%(d*7.45))
cmd.select('his5', 'n. CG&r. his w. %s of n. OG1&r. thr'%(d*6.86))
cmd.select('his6', 'n. CG&r. his w. %s of n. CG2&r. thr'%(d*6.75))
cmd.select('his7', 'n. ND1&r. his w. %s of n. CB&r. thr'%(d*7.40))
cmd.select('his8', 'n. ND1&r. his w. %s of n. OG1&r. thr'%(d*6.58))
cmd.select('his9', 'n. ND1&r. his w. %s of n. CG2&r. thr'%(d*7.06))
cmd.select('his10', 'n. CD2&r. his w. %s of n. CB&r. thr'%(d*6.32))
cmd.select('his11', 'n. CD2&r. his w. %s of n. OG1&r. thr'%(d*5.85))
cmd.select('his12', 'n. CD2&r. his w. %s of n. CG2&r. thr'%(d*5.52))
cmd.select('his13', 'n. CE1&r. his w. %s of n. CB&r. thr'%(d*6.28))
cmd.select('his14', 'n. CE1&r. his w. %s of n. OG1&r. thr'%(d*5.33))
cmd.select('his15', 'n. CE1&r. his w. %s of n. CG2&r. thr'%(d*6.21))
cmd.select('his16', 'n. NE2&r. his w. %s of n. CB&r. thr'%(d*5.43))
cmd.select('his17', 'n. NE2&r. his w. %s of n. OG1&r. thr'%(d*4.68))
cmd.select('his18', 'n. NE2&r. his w. %s of n. CG2&r. thr'%(d*5.10))
cmd.select('his',' br. his1&br. his2&br. his3&br. his4&br. his5&br. his6&br. his7&br. his8&br. his9&br. his10&br. his11&br. his12&br. his13&br. his14&br. his15&br. his16&br. his17&br. his18')
cmd.delete('his1')
cmd.delete('his2')
cmd.delete('his3')
cmd.delete('his4')
cmd.delete('his5')
cmd.delete('his6')
cmd.delete('his7')
cmd.delete('his8')
cmd.delete('his9')
cmd.delete('his10')
cmd.delete('his11')
cmd.delete('his12')
cmd.delete('his13')
cmd.delete('his14')
cmd.delete('his15')
cmd.delete('his16')
cmd.delete('his17')
cmd.delete('his18')
cmd.select('thr1', 'n. CB&r. thr w. %s of n. CB&his'%(d*8.80))
cmd.select('thr2', 'n. CB&r. thr w. %s of n. CG&his'%(d*7.45))
cmd.select('thr3', 'n. CB&r. thr w. %s of n. ND1&his'%(d*7.40))
cmd.select('thr4', 'n. CB&r. thr w. %s of n. CD2&his'%(d*6.32))
cmd.select('thr5', 'n. CB&r. thr w. %s of n. CE1&his'%(d*6.28))
cmd.select('thr6', 'n. CB&r. thr w. %s of n. NE2&his'%(d*5.43))
cmd.select('thr7', 'n. OG1&r. thr w. %s of n. CB&his'%(d*8.32))
cmd.select('thr8', 'n. OG1&r. thr w. %s of n. CG&his'%(d*6.86))
cmd.select('thr9', 'n. OG1&r. thr w. %s of n. ND1&his'%(d*6.58))
cmd.select('thr10', 'n. OG1&r. thr w. %s of n. CD2&his'%(d*5.85))
cmd.select('thr11', 'n. OG1&r. thr w. %s of n. CE1&his'%(d*5.33))
cmd.select('thr12', 'n. OG1&r. thr w. %s of n. NE2&his'%(d*4.68))
cmd.select('thr13', 'n. CG2&r. thr w. %s of n. CB&his'%(d*7.92))
cmd.select('thr14', 'n. CG2&r. thr w. %s of n. CG&his'%(d*6.75))
cmd.select('thr15', 'n. CG2&r. thr w. %s of n. ND1&his'%(d*7.06))
cmd.select('thr16', 'n. CG2&r. thr w. %s of n. CD2&his'%(d*5.52))
cmd.select('thr17', 'n. CG2&r. thr w. %s of n. CE1&his'%(d*6.21))
cmd.select('thr18', 'n. CG2&r. thr w. %s of n. NE2&his'%(d*5.10))
cmd.select('thr',' br. thr1&br. thr2&br. thr3&br. thr4&br. thr5&br. thr6&br. thr7&br. thr8&br. thr9&br. thr10&br. thr11&br. thr12&br. thr13&br. thr14&br. thr15&br. thr16&br. thr17&br. thr18')
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
cmd.delete('thr16')
cmd.delete('thr17')
cmd.delete('thr18')
cmd.select('A_1zym_2_7_3_9', 'his|thr')
cmd.delete('his')
cmd.delete('thr')
