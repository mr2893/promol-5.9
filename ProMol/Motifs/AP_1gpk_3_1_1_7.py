'''
FUNC:AP_1gpk_3_1_1_7
PDB:1gpk
EC:3.1.1.7
RESI:ser,glu,his
LOCI:a-200,327,440;
'''
cmd.select('ser1', 'n. CB&r. ser w. %s of n. CB&r. glu'%(d*11.16))
cmd.select('ser2', 'n. CB&r. ser w. %s of n. CG&r. glu'%(d*11.13))
cmd.select('ser3', 'n. CB&r. ser w. %s of n. CD&r. glu'%(d*9.96))
cmd.select('ser4', 'n. CB&r. ser w. %s of n. OE1&r. glu'%(d*9.11))
cmd.select('ser5', 'n. CB&r. ser w. %s of n. OE2&r. glu'%(d*10.07))
cmd.select('ser6', 'n. OG&r. ser w. %s of n. CB&r. glu'%(d*10.68))
cmd.select('ser7', 'n. OG&r. ser w. %s of n. CG&r. glu'%(d*10.87))
cmd.select('ser8', 'n. OG&r. ser w. %s of n. CD&r. glu'%(d*9.86))
cmd.select('ser9', 'n. OG&r. ser w. %s of n. OE1&r. glu'%(d*8.96))
cmd.select('ser10', 'n. OG&r. ser w. %s of n. OE2&r. glu'%(d*10.17))
cmd.select('ser11', 'n. CB&r. ser w. %s of n. CB&r. his'%(d*8.76))
cmd.select('ser12', 'n. CB&r. ser w. %s of n. CG&r. his'%(d*7.33))
cmd.select('ser13', 'n. CB&r. ser w. %s of n. ND1&r. his'%(d*7.00))
cmd.select('ser14', 'n. CB&r. ser w. %s of n. CD2&r. his'%(d*6.44))
cmd.select('ser15', 'n. CB&r. ser w. %s of n. CE1&r. his'%(d*5.85))
cmd.select('ser16', 'n. CB&r. ser w. %s of n. NE2&r. his'%(d*5.38))
cmd.select('ser17', 'n. OG&r. ser w. %s of n. CB&r. his'%(d*8.37))
cmd.select('ser18', 'n. OG&r. ser w. %s of n. CG&r. his'%(d*6.91))
cmd.select('ser19', 'n. OG&r. ser w. %s of n. ND1&r. his'%(d*6.67))
cmd.select('ser20', 'n. OG&r. ser w. %s of n. CD2&r. his'%(d*5.87))
cmd.select('ser21', 'n. OG&r. ser w. %s of n. CE1&r. his'%(d*5.45))
cmd.select('ser22', 'n. OG&r. ser w. %s of n. NE2&r. his'%(d*4.74))
cmd.select('ser',' br. ser1&br. ser2&br. ser3&br. ser4&br. ser5&br. ser6&br. ser7&br. ser8&br. ser9&br. ser10&br. ser11&br. ser12&br. ser13&br. ser14&br. ser15&br. ser16&br. ser17&br. ser18&br. ser19&br. ser20&br. ser21&br. ser22')
cmd.delete('ser1')
cmd.delete('ser2')
cmd.delete('ser3')
cmd.delete('ser4')
cmd.delete('ser5')
cmd.delete('ser6')
cmd.delete('ser7')
cmd.delete('ser8')
cmd.delete('ser9')
cmd.delete('ser10')
cmd.delete('ser11')
cmd.delete('ser12')
cmd.delete('ser13')
cmd.delete('ser14')
cmd.delete('ser15')
cmd.delete('ser16')
cmd.delete('ser17')
cmd.delete('ser18')
cmd.delete('ser19')
cmd.delete('ser20')
cmd.delete('ser21')
cmd.delete('ser22')
cmd.select('glu1', 'n. CB&r. glu w. %s of n. CB&ser'%(d*11.16))
cmd.select('glu2', 'n. CB&r. glu w. %s of n. OG&ser'%(d*10.68))
cmd.select('glu3', 'n. CG&r. glu w. %s of n. CB&ser'%(d*11.13))
cmd.select('glu4', 'n. CG&r. glu w. %s of n. OG&ser'%(d*10.87))
cmd.select('glu5', 'n. CD&r. glu w. %s of n. CB&ser'%(d*9.96))
cmd.select('glu6', 'n. CD&r. glu w. %s of n. OG&ser'%(d*9.86))
cmd.select('glu7', 'n. OE1&r. glu w. %s of n. CB&ser'%(d*9.11))
cmd.select('glu8', 'n. OE1&r. glu w. %s of n. OG&ser'%(d*8.96))
cmd.select('glu9', 'n. OE2&r. glu w. %s of n. CB&ser'%(d*10.07))
cmd.select('glu10', 'n. OE2&r. glu w. %s of n. OG&ser'%(d*10.17))
cmd.select('glu11', 'n. CB&r. glu w. %s of n. CB&r. his'%(d*6.98))
cmd.select('glu12', 'n. CB&r. glu w. %s of n. CG&r. his'%(d*7.15))
cmd.select('glu13', 'n. CB&r. glu w. %s of n. ND1&r. his'%(d*6.50))
cmd.select('glu14', 'n. CB&r. glu w. %s of n. CD2&r. his'%(d*8.26))
cmd.select('glu15', 'n. CB&r. glu w. %s of n. CE1&r. his'%(d*7.37))
cmd.select('glu16', 'n. CB&r. glu w. %s of n. NE2&r. his'%(d*8.35))
cmd.select('glu17', 'n. CG&r. glu w. %s of n. CB&r. his'%(d*7.55))
cmd.select('glu18', 'n. CG&r. glu w. %s of n. CG&r. his'%(d*7.60))
cmd.select('glu19', 'n. CG&r. glu w. %s of n. ND1&r. his'%(d*6.72))
cmd.select('glu20', 'n. CG&r. glu w. %s of n. CD2&r. his'%(d*8.76))
cmd.select('glu21', 'n. CG&r. glu w. %s of n. CE1&r. his'%(d*7.55))
cmd.select('glu22', 'n. CG&r. glu w. %s of n. NE2&r. his'%(d*8.70))
cmd.select('glu23', 'n. CD&r. glu w. %s of n. CB&r. his'%(d*6.86))
cmd.select('glu24', 'n. CD&r. glu w. %s of n. CG&r. his'%(d*6.73))
cmd.select('glu25', 'n. CD&r. glu w. %s of n. ND1&r. his'%(d*5.73))
cmd.select('glu26', 'n. CD&r. glu w. %s of n. CD2&r. his'%(d*7.87))
cmd.select('glu27', 'n. CD&r. glu w. %s of n. CE1&r. his'%(d*6.54))
cmd.select('glu28', 'n. CD&r. glu w. %s of n. NE2&r. his'%(d*7.75))
cmd.select('glu29', 'n. OE1&r. glu w. %s of n. CB&r. his'%(d*5.65))
cmd.select('glu30', 'n. OE1&r. glu w. %s of n. CG&r. his'%(d*5.49))
cmd.select('glu31', 'n. OE1&r. glu w. %s of n. ND1&r. his'%(d*4.56))
cmd.select('glu32', 'n. OE1&r. glu w. %s of n. CD2&r. his'%(d*6.66))
cmd.select('glu33', 'n. OE1&r. glu w. %s of n. CE1&r. his'%(d*5.55))
cmd.select('glu34', 'n. OE1&r. glu w. %s of n. NE2&r. his'%(d*6.67))
cmd.select('glu35', 'n. OE2&r. glu w. %s of n. CB&r. his'%(d*7.76))
cmd.select('glu36', 'n. OE2&r. glu w. %s of n. CG&r. his'%(d*7.52))
cmd.select('glu37', 'n. OE2&r. glu w. %s of n. ND1&r. his'%(d*6.42))
cmd.select('glu38', 'n. OE2&r. glu w. %s of n. CD2&r. his'%(d*8.59))
cmd.select('glu39', 'n. OE2&r. glu w. %s of n. CE1&r. his'%(d*7.06))
cmd.select('glu40', 'n. OE2&r. glu w. %s of n. NE2&r. his'%(d*8.33))
cmd.select('glu',' br. glu1&br. glu2&br. glu3&br. glu4&br. glu5&br. glu6&br. glu7&br. glu8&br. glu9&br. glu10&br. glu11&br. glu12&br. glu13&br. glu14&br. glu15&br. glu16&br. glu17&br. glu18&br. glu19&br. glu20&br. glu21&br. glu22&br. glu23&br. glu24&br. glu25&br. glu26&br. glu27&br. glu28&br. glu29&br. glu30&br. glu31&br. glu32&br. glu33&br. glu34&br. glu35&br. glu36&br. glu37&br. glu38&br. glu39&br. glu40')
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
cmd.delete('glu16')
cmd.delete('glu17')
cmd.delete('glu18')
cmd.delete('glu19')
cmd.delete('glu20')
cmd.delete('glu21')
cmd.delete('glu22')
cmd.delete('glu23')
cmd.delete('glu24')
cmd.delete('glu25')
cmd.delete('glu26')
cmd.delete('glu27')
cmd.delete('glu28')
cmd.delete('glu29')
cmd.delete('glu30')
cmd.delete('glu31')
cmd.delete('glu32')
cmd.delete('glu33')
cmd.delete('glu34')
cmd.delete('glu35')
cmd.delete('glu36')
cmd.delete('glu37')
cmd.delete('glu38')
cmd.delete('glu39')
cmd.delete('glu40')
cmd.select('his1', 'n. CB&r. his w. %s of n. CB&ser'%(d*8.76))
cmd.select('his2', 'n. CB&r. his w. %s of n. OG&ser'%(d*8.37))
cmd.select('his3', 'n. CG&r. his w. %s of n. CB&ser'%(d*7.33))
cmd.select('his4', 'n. CG&r. his w. %s of n. OG&ser'%(d*6.91))
cmd.select('his5', 'n. ND1&r. his w. %s of n. CB&ser'%(d*7.00))
cmd.select('his6', 'n. ND1&r. his w. %s of n. OG&ser'%(d*6.67))
cmd.select('his7', 'n. CD2&r. his w. %s of n. CB&ser'%(d*6.44))
cmd.select('his8', 'n. CD2&r. his w. %s of n. OG&ser'%(d*5.87))
cmd.select('his9', 'n. CE1&r. his w. %s of n. CB&ser'%(d*5.85))
cmd.select('his10', 'n. CE1&r. his w. %s of n. OG&ser'%(d*5.45))
cmd.select('his11', 'n. NE2&r. his w. %s of n. CB&ser'%(d*5.38))
cmd.select('his12', 'n. NE2&r. his w. %s of n. OG&ser'%(d*4.74))
cmd.select('his13', 'n. CB&r. his w. %s of n. CB&glu'%(d*6.98))
cmd.select('his14', 'n. CB&r. his w. %s of n. CG&glu'%(d*7.55))
cmd.select('his15', 'n. CB&r. his w. %s of n. CD&glu'%(d*6.86))
cmd.select('his16', 'n. CB&r. his w. %s of n. OE1&glu'%(d*5.65))
cmd.select('his17', 'n. CB&r. his w. %s of n. OE2&glu'%(d*7.76))
cmd.select('his18', 'n. CG&r. his w. %s of n. CB&glu'%(d*7.15))
cmd.select('his19', 'n. CG&r. his w. %s of n. CG&glu'%(d*7.60))
cmd.select('his20', 'n. CG&r. his w. %s of n. CD&glu'%(d*6.73))
cmd.select('his21', 'n. CG&r. his w. %s of n. OE1&glu'%(d*5.49))
cmd.select('his22', 'n. CG&r. his w. %s of n. OE2&glu'%(d*7.52))
cmd.select('his23', 'n. ND1&r. his w. %s of n. CB&glu'%(d*6.50))
cmd.select('his24', 'n. ND1&r. his w. %s of n. CG&glu'%(d*6.72))
cmd.select('his25', 'n. ND1&r. his w. %s of n. CD&glu'%(d*5.73))
cmd.select('his26', 'n. ND1&r. his w. %s of n. OE1&glu'%(d*4.56))
cmd.select('his27', 'n. ND1&r. his w. %s of n. OE2&glu'%(d*6.42))
cmd.select('his28', 'n. CD2&r. his w. %s of n. CB&glu'%(d*8.26))
cmd.select('his29', 'n. CD2&r. his w. %s of n. CG&glu'%(d*8.76))
cmd.select('his30', 'n. CD2&r. his w. %s of n. CD&glu'%(d*7.87))
cmd.select('his31', 'n. CD2&r. his w. %s of n. OE1&glu'%(d*6.66))
cmd.select('his32', 'n. CD2&r. his w. %s of n. OE2&glu'%(d*8.59))
cmd.select('his33', 'n. CE1&r. his w. %s of n. CB&glu'%(d*7.37))
cmd.select('his34', 'n. CE1&r. his w. %s of n. CG&glu'%(d*7.55))
cmd.select('his35', 'n. CE1&r. his w. %s of n. CD&glu'%(d*6.54))
cmd.select('his36', 'n. CE1&r. his w. %s of n. OE1&glu'%(d*5.55))
cmd.select('his37', 'n. CE1&r. his w. %s of n. OE2&glu'%(d*7.06))
cmd.select('his38', 'n. NE2&r. his w. %s of n. CB&glu'%(d*8.35))
cmd.select('his39', 'n. NE2&r. his w. %s of n. CG&glu'%(d*8.70))
cmd.select('his40', 'n. NE2&r. his w. %s of n. CD&glu'%(d*7.75))
cmd.select('his41', 'n. NE2&r. his w. %s of n. OE1&glu'%(d*6.67))
cmd.select('his42', 'n. NE2&r. his w. %s of n. OE2&glu'%(d*8.33))
cmd.select('his',' br. his1&br. his2&br. his3&br. his4&br. his5&br. his6&br. his7&br. his8&br. his9&br. his10&br. his11&br. his12&br. his13&br. his14&br. his15&br. his16&br. his17&br. his18&br. his19&br. his20&br. his21&br. his22&br. his23&br. his24&br. his25&br. his26&br. his27&br. his28&br. his29&br. his30&br. his31&br. his32&br. his33&br. his34&br. his35&br. his36&br. his37&br. his38&br. his39&br. his40&br. his41&br. his42')
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
cmd.delete('his19')
cmd.delete('his20')
cmd.delete('his21')
cmd.delete('his22')
cmd.delete('his23')
cmd.delete('his24')
cmd.delete('his25')
cmd.delete('his26')
cmd.delete('his27')
cmd.delete('his28')
cmd.delete('his29')
cmd.delete('his30')
cmd.delete('his31')
cmd.delete('his32')
cmd.delete('his33')
cmd.delete('his34')
cmd.delete('his35')
cmd.delete('his36')
cmd.delete('his37')
cmd.delete('his38')
cmd.delete('his39')
cmd.delete('his40')
cmd.delete('his41')
cmd.delete('his42')
cmd.select('AP_1gpk_3_1_1_7', 'ser|glu|his')
cmd.delete('ser')
cmd.delete('glu')
cmd.delete('his')
