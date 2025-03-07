#! /usr/bin/python

import sys
import numpy as np

def solve(s: str) -> (int, int):
    # create character matrix
    M = np.array([[c for c in l] for l in s.split()])
    P = np.array(list("XMAS"))
    # first: search for word "XMAS" in the char matrix for every possible way and direction
    first = 0
    # first = np.sum([np.all(np.roll(M, i, axis=0)[:-len(P), :] == P, axis=1).sum() +
    #                np.all(np.roll(M, i, axis=1)[:, :-len(P)] == P, axis=0).sum() for i in range(len(M))])

    second = np.nan

    return first, second


def main():
    global s
    r1, r2 = solve(s)
    print(f"Answears:\t for the first star: {r1}\n   \t\tfor the second star: {r2}")

s="""
SAMMSSSSXSAMXMSMASMMSMSSMMSSXMASMAMMAMSSMSMSAXSSXMXMSASXMSAMXSMMXAMXMMSMSSMXSAMXMMASMSMSMMMAXAAXXASXMMXMSSXMASMMSMXAMSMMMMMAMXSASAMXMMXSAMXM
SAAXAASAASXAAAAAMAAXMAAAMSAAAXAXMAXMSASAASAXAMAMXMSMMAXMAXAMXXAASMSMMAAXXAASASXSXSAMXSAMXAXMSMSMSMMASAMXMSXXAAMSAMMMSMMMAAMAMAXAMXSAMXMAMMAM
SMMMMSMMMMMSMSXSSSSMMMMMMMMSMMASMXXAMXSXMMMMSAMXAMAAMMMAMSSMMSMMSAAXMSSSSMXMAAXSAMXSAMMMMSXXAAAAAAMMMSSMAMMSSMMSASXMAAMSSXSASMMXMASASMAMMMAM
SAAXXMASAXAXMMMXAAXASAXXAMXXXXMMASMXMASAMXXAMSXSSSSSMAXAMXXAAAAAMXMMAAAAXXXMMSAMXMMMMMSAAMXSMSMSMSMMAXXMAXMAMAASXMASXSMAMXSASMSSMASXMXSXSSSS
SSMSSXASXMXSASAMMMMMAAXSAMXXMASMAMMAMXXXMMMMSMXAAMAAXXSSSMSMMSAXSAXASXMMMMXXSXMSAXAMAMMMSMASAXAMAMAMXSXXSAMASMMSASMMAMMSSMMAMAAMMASXMMMAMAAS
XAXXAMXSMXXSAXXSASMSMAMXAMXMMASMXMMSSSMAXMASMMMMMMSMMMAMAMAAXXXSXMMMMAMXMXMMMAASASXMMMXMAMAMAMAMASMMSMMAXMMASAMSMMXMSMAAAXMAMMMSMXXAMAMAMMMM
MSMAMMMMAXMMMMSMASAAXAMSSMSXMASMSMAAAASMMSMSAXMASAAAAMASASMSMASMMXAASAMXAAAAMMMMAAMXXSMSXMASXXASAMAXAAMAMXMASAMXSMXSXMMSSMMMMSAMMSSMMXSAXMAS
SAAXXAAXMXMAMMAMAMMMMXXAXAXXMASAAMMMSXMXAAMMMMMAMXSSXSASASAAMXMAMSMMMMMSSXXSXXXMSMSXMAMSAMXMASMMMSMSXXMASMMASAMASMMMXMAMAMSMMMAMAMMASAMMSAMS
SMSMXSSSMXSASAMMMSAXASMSMSMSMMMXMXXXXMMMMMXAAMMAXMMMXMAMMMXMSASAMXSMSXAAXMAMMSXMASMXAMXMAMXSAMXAAMXSXASASXMAMAMAXAASXMASAMAAXSMMAXSAMASAMAMX
MMAMAAAAAMSAMXXMASAMXSAMAMMAAMAAMMMXMASMSMMSSXXAXSMSSSSXMASXSMMASAMSAMMXSAAMASAXMASXSSMXASAMXSXMXXAMSXMASXMAMSMMSSMSAMAMAMSAMXAXMXMMSAMASMMS
ASASMMSMMMMSMXMXASXXXMAMAMSXSMSMSAAAAXSAAXAXMXMSMSAAMAMXMAMMXMSMMASAMMSXSMXSASAMXAXXAAMSMMMSMMASMMMXAXMMMXMXXMAMAAASAMXSMMXMXSMMSSSXSMSAXMAS
MMMSXAAXAMXAMASMASAXSSSMSXMAAAMAMXSMSMMMMMMXMXAXAMMMMAMXMAXAAMAXMXMMXAXXMAMMMMAAMMSMMMMAAAAAMMAMXAMASMSMMXAMXSAMMMMMASAAXAXSASAMAAXAMAMXMMAM
XSSSMSSSSSSMSASMSMMMMAMAXAXSMMMSMAMAXAMAMASAAMSMSMSXSASASMSSMSSSXAAXMXSMMAMAASXMXMAXXAXXXMXSMMASMMMAXMAAMMSAMSAMXSXMAMXSMSSMASAMMXMAMAMXAMAS
XSXMAMXAMAAAMMMXAAMSXMMSMMMMAMAXMAMMSSMASASMMMAAAXXASAXAXMAAAAMMXAMXMASAMASMXMXMAXXSSSSMXSAXASXSAXMSSMSXSAAXAXAXMSAMXSXMAXAMASXMXMSASASMMSAS
SMMMSMMMMSMMMSMSXSMMAMXXAMASMMMSSXSAAXXXMAMXASXSMSMMMSMXMASMMMAAMSMSMAMAMXXXSXASMSMMMAAAAMMSAMAMXMAAAXAMMMMMSAMMXMAMAXMSMSAMXXAXXASASXMAXMAS
MAAAAAASAXAAXAAXAXMSMMASAMASXMXMASMMMSAMMXMSASAMAXAAAMXSAXXXXMMXMXAXAMXMMSMAXSMXMAAAMXMMMSMSMMMMMSMXSMMSSSXAAAAXMSMMXMASAMMMMMSMMMMAMXMAMMAM
SSMSXSMMSMSMSMSMXMAXXMXSAMAXMAMXXXXXAAMSSMAMAMMMSMSMMMAXMASXMSSMSMMMXSAXAAMXMXXASMSMSAMSMAASAMXAAXMXXAXAAMMXSSMMMAMASMAMAMSMSAAAXXMXMMSMAMAS
XMAXXAXAXMAASXMMSMMMMSMSXMASMSXSXSSMMSXAXMAMAMAMAMXMXMXMMAMAAAMAAAXAASAMSSXSMXSXSXAASMSASMSMAXSMSSMAMMMMXMMXAXAXSAMASMXMASAAMSSMMSMXMAAXMSAS
SMAXSXMASAMMMAMAMAMXAAASASXMAXAXAAXAXAMXXSASASASXSASASAAMASMMMSSXXMMMSXAMMMAMAMAMMMMSXSASXXXSMXAXXMAMAXXASAMMMMMSAMASMXSMSMSMAMASASAMXMSMMAS
XMMMAXMASMXAXAMAXAMMSSSSXMAMAMMMSMSXMMSMMMXSXSASMSASAMSAMXSXAAXMXSASXSMAAASAMMSAMXSAMAMAMAMMAMXSMSXMXXMXMSAMXAAMXAMASAMXASAAMAXMSASXSAMAMMAM
SAMMMXMASXSASXSSSMSAXMAXAXAMXSXAMXSMAAAMASXMAMMMXMAMXMMMSMXXMMSAASAMASASMMSAMASASXMASMMMMSMAMMAXAXASXXSAAMAMSXSMMXMXXASXSMSMSMSAMAMAMMSMSMMS
SAXMXAMXSMMXAXXAAAAMXAAMMSSSXMMMSAMXMMSSMSAXAMXSXMMSMMMASAXXMMMMMSSMSMMXAASXMASXMASAMAAAAXXSXMMSSMMMAASMMSMMSAAASXMMSAMMXAXMAXMAMAMAMXAASAMX
SXMMSASASXXMASMSMMMSMMSSXAXMAMMMMXSAMXAMXSMMXSXAXMASASMASXSMMAXMAMAMXMSSMMMAMASXXAMXSSMMXSSMAAAAAXXMMMMXMAMAMMMMMAAXMMMSSMMSSXSSSMSASXMMSAMX
SAMXAAMASXMAXSAAXMAMXAAMMSMSAMAASASASMXSAMXMASXXMMXXAMMAXAXAXMSMMSAMAMMMAXSXMAXAMAMXXMXMASAMMMXSMMMXMMMXXAMAAAXXSMMMSXXXMAAXMAXAAAXMMXXXSAMX
SMMAMMMMMAMSMMMSSMXSMMSSMXAMMSSMSASMMMAMASASAMXASXSMMMMSXSXSAMXAXSASMSASAMXAMSMXAAXMASAMXMASAMXMXAAXXAXMSMSMSMSASAMASMSMSMMSMSMSMMMAXASASAMX
SMSMSAXSXXMAXAAMAMAAAXAXAMAMMXMAMXMMAMXXAXXXAMMXMAAMAXXXAMAMAXMXMMAMXXASXASXMAAMSXSAAMMSXSAMXSSSSSSMSXSAAXAXAMXMSAMASXSAAAXXAMXMASMSXAXAMAMM
XAASMMXAXSSSSMXSAMXSSMMMMMSXAAMXMAMMASAXSSMSAMMAMSMSASXMAMASMMMSSMMMSMAXXMXMMMSMMASMXMSAMMXMXSAAAXXXAAMXMSXSMMAXSXMASAXAMSMXSSXSASAMMSMMMSMM
MMMSMXSMXMAMXMAMXSAMMMXAXSAMMXMAXAMSAXMMMAMMMMMMMXAMXXXMMMMSAAAAAAXAXMXMSMSXAXAAMAMMMMMASXSSXMMMMMMMMSMMXSAAXSSMSXSMMMMSXXAMXAASAMAXMAAAAMAX
ASXMMAMXAMAMAMAMAMXSASAXXAMXXAASXMMMMXSAMAMXSAXMAMXMSSSXSAAMMMMXSMMMSXAAAASXSMSXMAMAAASXMAAMMSXXXAAAXXASAMXMMAMXXAAMAMMMMMAXMMMMXMAMMASMXSAM
MAAAMMXSASASXSMSSMMSASMXMAXXMMMMMXAMXASASMSMSASMMXAMMAAASMSSMSMXMXXAXMSSMXMAXAMXMMXSXMSAMMMMAMXSXSXSSXXMAMAXMSSMMMMMAXAAAXSMAXASXMXXXMAMXXXA
SSSMXAXAAAMAAAAAAAXMXMASMSMSMAAASXSSMMSMMXAAMAMAMSSMMMMMMMAAAAMMMAMMMXMAXXMAMAMMXSAMASXXMAMMXSAMMMXMMMSMSMSSXAAXXXASXSSSSSXAXMAXASAMXXAXMAMS
MXMAMXMMXMSSSMMSMMMMMMAXXAAAXSMMMAAMAXMASMMMMAMXMAMXSMXMASMMMMMAMASAAMSAMSMMSMMSAMASMXMASMMSMMMMAMMXAAXAAAXAMMSAMXMXAMAAMMMSMMSSMMAMXMMAASMM
SSMMSSMXAXAAAMXMASAMXSSMSMSMXMXSMMMMSMMMAAXASMSSMAMMMAASXSXMXSMMXASMSXMASAMAMXAMASASAASMMSASASMSSSMMXMMSMSMSAXXAXAMMSMMMMAAAAXAAMMAMAASMMXAS
AAAAAAAMMMMSMMAMXXASAXAAMAMMASAMXXAAAASMSSMASAAMSMSMMSMSMMMMASASMAXXXMASMXMASMXSAMAMMXSMAMXSAMAAMAASAMXXXXXASAXAMXXAMASMSMSSSMSSMSMSXMXMASAA
MSMMSXMXMAMAMMASXMMMXSMXMAMMAMAMSXMSSMMMAMMXMMMMSMAXXAMXXAAMSMAMAMSMMSMMMXSAMMAMXMAMMXXMAMAMAMMMSSMMXMASMXMMMXSSMXMXMXMAXAXMAMXXAAAXMSSMMMSM
XMXXXMMAMXXAXSASASAAXMAMSXSMASAMXAXAXXXMAXXSASXAMSMMXASXMSMSAMAMXXAAAAAAMMMMSMXMMMMSXMXSAMASAMAXMAMMMMAMMXMXMAXAAAMSAMMMMSMMMSAMMMXMAXAASAMX
MSMMSASMSSMMMMASAMMSMAMXSMXMAXXSSXMASXSSSSMAAAMXXASAXXMAAAXSXSASXSSSMSSMSXAASXMASAMXAMASMSMSASXSSMMAXMSXSAXAXXSMMMAAAMXXMXAXXMASXMASXSSMMASX
AAAAXMASAXAAAMMMMXXAAXMASMMMSSXMASMXMAAAASAMXMMMSASMSMAMMSXMASAMXAAAMXMASMMMSAMAXAXXAMASXSAMASAMXXSMSAMASXSMSAMXAXMSXMAXMMXMXXAMXMASAMAASXMX
SMSMMXMAXSMMXXSAMMSMSSMAXAMAAXXXAXMAMXMMMMMSAXAXMMMAAAXMAMAMAMXMMMMMMXMAXAAAXAMMSSMSSMXSAMXMAMAXAXSXSAMAMAAAAAMAXSXMMXSAASMMSMASXMASASXMMMAS
XXMMAAXSAMMSAMMASAXSAMMSSMMMSSMMMMSMMAMSXMXSXSMSAMMSSSMMXXMMSSMSXSMXMAMXXSMXMAMAAAXAXXAMXMAMXSSMMSXAXAMXMSMMMSMXSMAXAAMMAMAAASAMAMXSMMAMXMAM
SAMXSXMMASAMAMSAMMSMMSAMAMXMXMAAAAAMXMMSAMMSAXAXXMMAMAAXXXSAMAAXAXAASXMMXMAMSSMMSSMMSMXMAXAMASXASXMMMMMXMXAMXAMSAXXMMSXMXSMXMMMXMXMXASAMMMSS
MAMMXAXSAMXXSMMASMSAAMMSAMAAAMSSSSXSASXSAMAMMMMMSXMASAMMMMMASMMMMMSMSAAXAMAMAXAAAMAASAMSMSMSMSMSAMXAAXAXXSMXXAXSAMXSMXXSAMASXASAMXAMAMXSXAXX
SAMASMMMASXSAMXSXASMMXASAMASMXAMMXMMMSASMMXSXAXAMASAMAMAXASMMMXAXMXXSMMMMSSMMSXMMMSMMXMAMAAAMMMXXSSSXMXXASAAMSMMAMXAAMXMASASAAXAMMSAAMAMMMMM
SXMMSAAXSAMAMXMXMMMMSMASMMXAMMMMXMMSAMXMMXAAXASASAMASXSMSXSMAMSASMMMMAMXXAXXXXMXXAMMSMSXSMSMSAMXXMAMSXSSMMMMXXAMXSXMMAASAMXSMSSMMAMSMMAMAAAA
MMSASMMMXMASXSAXAXAASMMMMMMAMSSSMAXAXXMASXMMMMSAMASAMAAAXAMMAMMAAXMXMAMMMMSMSAMXMASAAMMXMXAAXMSMXMAMMMMAAAMMASAMAXMXSSMSASXXAXAXSXMAXSMSSSSS
XAMASXMASXAXXXSSXMMMSAMXAXSAMSAASMMSXXMSAMXAAAMXMXSXMSMXMMSXSAASXXSASASMAMXAXAMXXXMMMMSAMSSSSMAASMXMAAMXSMSMASAMXXAMXXMSXMMMSMXMXAMXMSAMXAMX
XSMXMAMAMAMMXMASMAMASMMMMXMASMSMMMAMMAMMMAMSSXMXSAMAAXMSMXAAMXMMMXSASAXXAMMSMSSMSMAASAXAXAAXAXXSMMASXSSMAAAMXSXMAMSMMSXMSAAXXAMSSSMMSMMSXMAM
SMSMSMMASAMAMXAMMAMXXAXSMMSMSAXMXMASMAMSSSMMMASMMASAMXAAMMMXMAAAXMMXMMSXMSXMXAAAAMXMMSSMMMXSMMSMMXMSXAAXMXXSAMAMMMMAAXAASXXMMSMAAAXMAAMXASMS
SASMAXMAXAXSAMSSSMSMSMMSAMAAMAMXMMMSXMSXAAMASAMAXAMAMASASXXASMSSSXMXAAMAAAXMMSXSSXSXAAMAXAAMXMXAASXMMSMMXAMXASAXMASMMXMMMSSXAXMMSMSSSSMSAMAM
MAMSXSMSMSAMXSXAAXAMAAMXXXMSMSMMXMMMAXAMSMMAMASXSSSMMAMAAASMSAXXAASMMASMMMXSAMXAAASMMMSAMMMSAMMAMXASAXSAMSAXAMMSSMSASAAAAXMMSXXMAMMAAXMAMMAM
MAMSXMAAAXXMMXXMMSMXSXXXMASMMAAAAXSMSMMAMAMXXMMAAAAXMASMMMMMMXSMSMXAMAAXAXAMASMMMMMAXXXMASAAAXMXSMSMSMMMMXAMSAMXAAMAMXSMSMXMASXSSSMMMMASASXS
XMMMMMAMMMMAASASAXMAMSMXAMXASXSMSMMAXSMASAMMSSMMMSMMMMXMAXXXAAXXAXSXMMXSXSMMXMXXSXSSMSMMMMMSMMMAAXXAXXMASMXMXAXSMMMSMMXAXXXXMAXXMAMXMXAMXAAM
MXAXAASXSAXXXAMMXSMASAMASMSMMAAMXAMMMAMASAMAAXAMAMAMXAAMSMSMMSSXMMMMMSAMAMAMMMXAXAAXAMXAAXMAMAMMSAMAMMSASASAXXXMASAAAMMXMASMSSSXSXMAMMXMAMXM
ASMSSMAMMMMSAMXSXSMXSAMMXAAXMSMMSMMXXXMASMMMXSAMXSMSSSXSAMAAXAXAMXMAAMASXSAMASASMMMMXMASXSSMSMSXMAMXMAMMSMMXMSMMAMMXAMXAAAXXAAXASXSMMSMASMMM
XAAAAMAXAMAMXXAXXXXASMMXMSMMXAAXMXSAMXSAMASXMXMXXMAMXAMSASMSMSSMMASMSSXMXSASXMAMXXAAXSXMAXMASXMASXMSMMXAMXXAMAAMSSSSSSXSSXMMMSMMSASAASXXMASM
SMAMXSMMMXXSAMMSMSMXMXXAXMASMSMMMAMASAAASAMMMAMSMMMMMMMSAMAXMAAASXSAAMAMXSMMMMSMMSASAMAMAMMAMAMXMAXXAAMSSMSMSXSXAAAAAAXMMMMSMAAXMAMMMSAXXXAM
XXSXMAAMSMMAXSMAAAAXSMSMXSAMAAMAMAMXMMMXMAMAXAXAAASASAAMMMAMMSSMMMMMMXXSAMXXMAMAAAXMASAMASMMXMMSMSMSXMXAAXXXAXMXMMMMMMMMAAXAXMSMMXMXMMMMASMS
SMMASMAMAAXMMAXMSMMXAAAAAMASXSSSSMSAAXSXMAMSMMSMSMSAMMSSSMSSXMMMAASAMXSMMMXMMSSMMSXMAXXXXSASXSMSAAASXMMSMMMMSSMAXAAXXAASMMSMXMAAXAXMXAXXXMXS
SASAMXAMMXMXXXAMXASXMMMSMSXMAMAAAMXAMXAMMSXXAASAXMMXMXAAXAXMXAASXSSXXXAAAAAXMAMAMXAMSSXSMMAMAAAMSMMMASAMMXSAMAXMASXSXMXMXAAXASXSMMSMSMSMXAAS
SXMASMMSSSSMSMMMMMMMAAAXAMXMXMMMSMMSMSMXXMAXMMMAMAAXMMMSMXMASMMXXAMAMMSMMSSMMASAMXAMAAASAMAMSMMMXSMXXMASAAAASXMXAMAMXSAMMXMSXSAXMXAAAAAMXMAS
MMSAMAMAAXSASXAAASAMMMXSAMXMAXXAAAAAAAXXXMSMSMMMMMASAAMXXMMMMMSMMMMMAAXAXAMMSASASMSMMMMMASXXXMXMSAXSAMSMMMSAMXAAMMAMASASAMMMMMXMMSMSMSMSXMAS
XAMXSAMMXMMXMASXSSXSXMASXXAXMXMXSSMMSMSXAAAAAXXMASAAMSSXAXASAAAAAMAXXSSXMASASXSAMAAAXAASAMXMAMAMSAMMAMXAXXXASMSMSMSMXMXMMXAAXMAMMAAAXAAXAMAS
MXSASXMAXMASMXMMMMAAXAMXMSSSSXSAAAXXMAMXXMMSMXAXMMXSXMAMASXSMMSSMSMSSXMXMXMMSAMAMMMMMAXMASXMAMAMMMMSMMSMMSSMAAAAAXXAXMASXSMSMSASXMSMSXXSMMAS
AAMASXMASMAXSAMXASMMMMSAMSAAAAMXSMMXMAMMMMXXMSMSXMAXAAAMXMMXMXAAAAMMAAXXSAMXMMMASASMXXMAXMASXSMSMMASAAAXMAMXMMMSMSMMMSMSASMAXMAMMAMXXMMMXAXS
SMMMMAMASMMMMMSSMSAAXAXMMMMMMSAMXAXXMAAAAMXSAAAXAMSSMMMMAXMASMMMSSSSSSMAMXSAXXSMXAXXXXXSAMXAAXAAXMASMSMSMMXAXAMAMXAXAXMXAXMMSMAMSMASMMAASXMX
MXSASAMMSAASAMXAASMMMMMSAAAAXMXASMMMSSSSSXMMSMXMAMAAMAXSSSMAMAXXAAAXAAMSMMSASMMMMSMMXSAXAXSMMMSMSMMSAAASXSMSMMXASMSMMSAMXMMAAMAMAMASASMMAMMX
MASXSASAXMMSASXSMSXSMAASMSSSSMMXXXMXAAMXMMAMXSMMAMSSMXMAAXMASMMMMMMMXMAXAMMAMXAAAMAAMAAMSMMAXAAXAAXMXMXMAMMMAAXSXMASXAAAAXMASMAMMXAMXMMMAASM
MXMMMAMMMMXXAMAMAXASAMXSAMXXAAMXMXMSMSMAMSMSAMXSAMAAMXSMSSSMSAXXAAMAMXASMMMMMSMMXXMXSMXMAXSAMSSMXAMXAMAMXMAMMMMMASAMMMSSMXXXMMASXMMSSXXMSMAA
XAAAMAMMXSXMXMXMAMMSAMXMAXXSXMMMAAXMAMMAMAAMAXAMAMSMMAXXAAAXXMAXSMMAMSXSASXAASAASXSMSXSAMMMMXMMMAAXXASAMAMAMAAAMAMASAAXAXMMAMMXXAMXAMAXAMXXM
XXMMMMXMASAMXXAXXXXSMMASMMMMMSAMMSSMXMSXSMXMSMMSSMAMMMSMMSMMMMXMAMSMMMASAMXMXSMMXAAAMAMXXSAMXSASMMSXASASMSSSSSSSMSMMMSXAAXAAMASMMMMASMASMMSS
MSSSMSSMMSXMASMSMAXSXSXXAMXAASAXSAMXAAXXMXMAXAXAAMAMXMAXAAMMMAASAMASAMXMMMSSMMXSMAMMMSMMMXAMAMAMAAXMMMMMMAMXAAAMAAXMAXMMMASXSASAMXSXXXAAAAAA
XSAAMAAAXMXMAMAAXXXSXMMSMMXMXSAMXMMSAMSXSXMASXMMSMSSSXSMASXAMSXSASAXMXXMAAXAAAAXMSAXXMAMXSXMXMMMMMMMXAXAMAMMAMASXMMSAXMASAMXMMSXMAAMMMSSMMSS
XMAMMSSMMMAMAMSMSMAMAMXASMXMAMXMAAMXMASXSXMASXASAMMAMAXXAMMSXMASAMXSMSMSAMSSMMSSMMAXSMSAASXSXAAXAAXXAASMXSMMXXASAMAMMMXAAAMXSAMXMMXSAAAXMAMX
MAXMAXAXXMAXAXAAXAASAMMMSXMXSXAMXSXAMASAMAMASXMMASMAMMMMMSAXAMAMMMMSAAAXMXMAMAAAAMXMXAMMSMAMSSMSMSMAAXXMAMAAXMASAMSSXMMSSSMAMASMSAMMMSSXMXAM
ASAMXSMMSSSSSSMSMSAMXSAXMASAMXSMXMXXMASASAMXMASXXMMAMMAAMMASXMAXXAAMXMMMSXXAMMSSMMAAMXMSAMAMMMAMAMASXMSMAMAMXSXSXMASAAAAAAMXSAMAMASMXAXAMSAS
MMASAXAXAAAXMAXXXAMXASXXSAMASAMMAMMXMXSASXSXSAMMSMSMSSSSSMAMXXAXMMSSSSSXMMSMMAMAASXSMXMXASMSAMXMAMMAXMAMASASAMAMMMASXMMXSAMXMAXMXXMAAMSMMAXM
AXAMASMMMMMMSMMSAMXMXSAXMXSAMXSMAXSMMMSMXMAAMMXAAAAAMAMAMMMXMMMSAAAAXAMAXAAAMXSSMMXAXSMSMMXMMMXMXXMMMSSSMXMMAXXMAMASAXAMXAXSASMXMSAXAMAMMMSM
MMMMXAXXMAMMXXAXAMSMMMXXXXMAMASXMXXAXAXMAXXXMAMSMSMSMMMASASAAAAMMMMSMMSSMSSSMXMASXSMMAMAXMASAMSMSMSXMAMXAMSSSXSMSSXSAMSSSMMSAMXAAXMMXSXMAXAX
XAXAMMXMAAMMMMMSAMAXXAMMSXSAMXSAMSSSMSASMSMAMAXMAMAXXXSMSASMSMSSXMAXAXMAMAXAMXXAXMAXAASMMSAXMMAAAAMXMASAMXMAMAMAASAMXMAAAXAMAMMMXXSAXSASXSMS
SXSMSMAMSXMAAAXMASMSMASAAXSMSMMMMAAXAMMXAAMAMMSMAMSXMAXAMAMAXAAMAXAMMSMSMMMXMMMAXSSMSASMAMMXSXMXMSMXSAMAXAMAMAMXMSXMAMMSMMXSAMXSAXMASMAMMAXX
SAXXAMXXAASXSXSAASXSAMMMSMSAAMASMMMMMMAMXMSAXSAMAMXMSASXMSMMMMMSXMMSXMAMMXMSAMMSAMXAMAXMSMSASXSXXXAXMASXMASXXAXXMXMMAMXMXSXXASAMMSAXSMMMSSMM
MAMXMAMXSXMXXXAMXXXMAMMMXAMSMSASAMXAAMMMAMMAMSAMXSXASASAAXXXAXXXXSAAXMAMAAASAAAXMASXMMMMASMAMAAAMMMMSMMMMASASMSMMAASMSMMAMXXSMXMAMXMXASAAAAX
MSMSMSMAXMSXSAXMASMSAMXAMXMXXMASAMSSXMASXSMMMMMMXMMXMAMMXMSMMMMMMMMMXSAMSSXSMMMXAMXAAXMSMSMSMAMMAAAAXAAXMASAMXAAXSMMXAAMSSXXMASMSMAMMXMMXXMM
MAAAAAMXMAAAXMMXSAASASMMSMMMXSASAXMXSMXXAAXMASASMXMSMAMXAMMMSAMAAMSSMSAXAMMXAAXSSMSSMXXAXSAMMAMXSXXXSSMSMMSXMSMMMXAXMMMMXAMXMAMAASXXMSSSMSXA
MMSMSMSSMMMSMAAXAXXXAMXAAAAAAMASAMMAMMMMSMMSXSASASMAMAMSMXAASASXMSAAASXMASMXSMXXXAMAMXSMSMMMSASAXMSMAMMXMAMAXSAMSSXMAAASXMMSMSMSMMXAXXAAASXS
SMXXAMAMXAMXXMASXMXSAMMXSSMMSMMMAXMAXAXXAAMXAMAMMASASAXAMSMXSXMASMXMMMSXXAAXMMSSMSMAMAAMAAAASASXMAAMAMSMSAXXMMAMAAXSSMXSAMXAAAAAMMSSMMMMMMAM
AMMSMMSSSSSMSXMAXAAAXXXXMAXAAASXXASMSMXSSMMMMMAXXMSMSXXAMAMMSAMXMAAXASXSAMMMXAAAAASAMXSMXXMMMAMAMSMSAMXAXMMSASMMMSMMASASAMSMSMSMSAAAAMSMXMSM
MAMXAXAAMMAAMMMAMMMMSXMSMAMMSMMXMAXMAAAMAMSSSSXSMXMASASMMASAMXSXXMXMXSAXSXMAMMMSSMXXXMMMMASXMAMXMXAMXSMSMAAMMMAAXAXSAMXSAMSAMAAXMMSSMMAMAMAM
SAMXAMMMMSMAMASXMXMXSAAAMASAAAXSXMSSMSMMAMAAXMASAMMAMMAXSXMMXSAMMMSMMMAMXMASXMXAMXXMSMAASAMASMSMAMMMMXAAMMMSMMSMMMXMSSMSXMMAMSMSXXAMXXMXMSAS
SASMSMAAMMSXSMSAMXSAMMSMSMSMSSMMMXAXXMASMMMSMMMMSASASXMMSMSAXMASXAAAAXMASXMAMXMMMMSAAMXMASXAXMAMXASAMXSMSXSAMXASAXXAAMXMMSSMMMAMMXXXMMSAMSAS
MAMAXMXMMAMXMASAMAMASAMXMMMXXMASAMMSMSAMMXMAMXXAXXSASXXASASMXSAMMSSSMSMAMXSMSMAXAAMSSMSXAMMXSSXMSASMSAMXXMSAXSASMSMMMSAAMASMAMAMMSMSMAMAXMAM
SSMSMMASMSMSSMXAMMSAMASXMASMSSMMSSXXASASAMXSSSMXSMMAMMMXMAMAAMAXAMXXXSMMSASXAMSMMXXMXAXMMMAMAAAMXAXAMASXXAXAMMAMXMASXXXSMAXMASMAMAAAMASXMMMM
SAAXAMAXMXAAMXSAMXMASXMMXAMAAASAMXMAMMAXXMAMAAXMMAMXMASAMAMMMSSMSSSMMSAAMASMXMMXSXSMMMMXASMMMMSAMMMMMMMAMSMSMMAMSSSMASXMMSXSAMXAXMSMSXSASASM
SMMMSMSSMMMMSMASXXSAMXMMSMSMXMAMSAMSAMXMMMXMSMMSSMMXSASASASXXAAAAXAMXMMMMSMMXAMXMAMXAMXMMXXAXXAMAAASASMXMAAAAMMSAXAXXSAAXAASASXMSAMXMASAMASX
XSAAXAAAAXMAMMAMXMMMMAXAAAAXMAAXSASXAXMMXSXAAMXXAAAXMXMASAXAMSSMXSMXXXXXXMASMMMXMAMSSXXAMMSMMSMXSXSSXSXASMSMSSSMMSMASMMMMMMMAAAMAMSSSMMSMSMM
SAMSSMSXMMMASMMSAXAAXSMSXXMSMMMXMXMMAMXMAMMSMSMSSMMSXSMMMXMXMMMAASMXSASMSMAMAASXSMMXAAMMMAAXAAXXXXAMAMMXMMXAAXAAXXXMAMAXXSXMMMAMXSAAAXAXXMAS
SAMXAXMASASMSAASMMMXSXAMSSSXMAMMMXMXMAAMAMXXAXAAMAMXAMMXAAXAMXSMASAAMXMAMMXSSMSMXSAMXMSAMSXXXMSMMSMMASAAMSMMMSSMMMMSMSMMMMAXXMSMSMMSMMXMAMAM
SXMMMMMASASAMMMSMSSSMMXMAXSASXMAXXSAMSXMASXMSXMSSSMMAMAMAMSMSAMAMMMMSMMSMMAXXXMAXAMAAXSAMAMMSXSAAXXAAXXXMAXXAXAAASAAXAXAAMMMSXAXXXAAMAAXAMXM
XMXXXAMAMAMAMXXMAAMAAMSMXMMMMMSMSMSAMMMMSMMAMAAMAMXXMAAXXXAAMXMASXMAAMAAAMMSMMSSMSXMMXMXMASAAASMMMSMSSSXASMMXXXMSASMSSSSXSAAMSSSMMSSMSXMXSSS
SAMMSSMSSXSXMMSMMMSSMMAAAMAXMXAAAASXMMAXAAMAMMXMAMSMSMMMMMMXMASASAMXSMMSXMMXAMAMXMXMMSMMSASMMXMMMAAAXAMMMMAMMMSMMMAMAAAASXMMXAXAXXMAMMMSMAAS
AXAAXASAMXMAMAMMMMMMMSXXMXAMXMMXMXMMXXSSXSMSSSMMAMAAAASMXSXXXAMMSAMXXMMXASXSMMMSASASAXMAMASXXAAASXMSMAMAASAMAAAAMXSMMMMMMMASMMMMMMXMMXAAMMMM
MXSSSSMMSASAMASAAAAXMASASXSSSMXMSMSAXXXSAXAMAAXMASMSMMMAAAMMMMSMXAXASXASXMASAAXMXSAMMSSSMXMASXMMSMXMAASXMSXMMMSMMAMAAXAXAXMSASASAMAASMSMSASX
XXMAXMAXAASMSXXMSXSXMAXXMAXAXXAAAAMSSMAMSMMXSXMAASXXMXSMSMXAAMAMSSMASMMMAMAMAMXSAMXMMAMAMXAMXAXAXMASXMSXXMASMXMMMAXMSSXSSSXSAMXSASXSMAXXSASM
SAMXMSMMMAMXMXMXMMXAMAXMMSMAMSSSMSMAXMAMXMMMXAAMXSXXXAXXAXMSMSAMAAMMMAXSXSASAMAMASXXMSSMSASXSSMMMSASASXXMMAXMASAMMSMMMMMAMXMMMXSXMMAMMMXMXMA
SSSXMAMSMASASMMMAAXAMSSMAMMAMMAAXXMAXSXSAMAAXAMXXMASMSMSMSXAXSMMMSMSMSMAASASMMXSAMXSSMMXSAAASMAXAMXSMXMMMMMSMSMSAAAMAAAXASXMASMMMSSSMSSXMMMS
SAXAMAMXMMSAXAASMMSSMAAMAMMSSMSMMMMXXAAMMSMSSSSXXMAAAAAXASMMMMMSSXXMAAXMAMMMXSMMXXAXAAMAMMMSMSSMMMAMXSMMAAMAMAAAMSMSSSMSASASASAXAAXMAMAXMASA
MMMMSMSMMMMXMSAMAAAXMSSMMXAXXMMAMSASMMMMMAMXAAAMSMSMSSSMAMSAASASASAMSMMXXXMASAAASMSSSMMASAXMAAXSMMXSAMAMAMMASXSMXXAMAMMXMSXMASXMMMAMAMMASMSX
ASAMAAAMMAAXXAASMMMXAMXMAMSSMXSAMMASXAXMSASMMMMMXAXXAAXMXMXXXSMMAMXMXAMXSAMXXXMAXAAXAXXASASMMMXAXAMXXSAMXSSXXMAAXMXMSMSAMMXSXMXAXMSXSSXAMMMM
AXAMMSXSAMXMMSXMMAXASMSMMXAAAXSASMAMXXMASXMASAXAMXMMSMSXMASMXSXMMMMASASAMXXSMSSSMMMMXXSASAMMSSSSMMSMMSXSAMAMMSSMMXXAXASASAAMAMSSMXAAMMMXSAAM
MMSMAMAXASXMAMXAMXSXXAXASASMMMSAMMSSSMSMSASMMSSSSMXAMXMMSAMXAMAMMMSAMSAMXMASXAAXMAXSAXSAMXMXAAAXXAAAAXAMMSAAXAAAXSMMMMMMAAMMAXMASMMXMAXAMMSS
XAXMMMASMMXXSAMXMAAXMMMAMMXAMXMMMMMAMAAAMAMXAMMAAMMMMAAXMASMMXSMAAMAMMMSSSMSMMSMSAXMMMMAMSSSMMMMMMSSMMMMMSMSSMSMMXAAAXAXMASXMMSXMXSASMMMSSMM
MMSAXMASAAXXMMAMMSSXAAMSSMSSMAMMMSAAMSMSMSSMMSMSMMAMSSSXSAMMMAXSMXMSMXXAASAXAXAMMMMMAAMAMAAAMXAAXMAXAAMAXMAAXMAMXSSMSMXSXASASXSXAAMAMAAXMMAX
XASAMAASMMMMXSAMMMMMSXMXAAAMMXMXAAMXMAXAAAAASXXAXMAMAAXAAMMSMAMASMAMXXMMSMXSXMASAMASXSSSSMSMMXSMMMASXMSMSMMMMMAMXXAXMXMMMMSAMAXXMXXAXSMSXMXM
MMSSMMMXASXSASXSAAMXXMXSMMMSMSMMMSMSMXSMSMSXMMSSSSSMSSMSMMAXMMSAMMAMASAMXMAMAMXMAXMSAAAAAXMASMAMXMAXMAAAXXMASXMSMSSMMASAAMMMMMMXSAMSAXXXAMMS
MAMXXXMSXMAMASASXSMMMMMAMAXXMAAAAAAXXAMMXXMAAXAAMAAAXMAAAMXSAAMMMMASAAMXMMSSMSMSSMAXMMMMMMSAASAMSMSSMSMSMMMAMAXAASAXXAXXXMAXAAAAMAXXASASMMAX
MSSSMAMXSMXMXMAMAXXAASMMMASMSSSMSMSMMASASASMMMMSMSMXMMSXSMMMMXSXSSXMMSSXXAMAAXMAXMXMMXXASAMXMMXMXAXXXXXXAMMSMMSMSXMMMSSMSSMSSSSXMSMMAMMAXMMS
XAAAMMMAXXXSSMSMMMMSMMASXSXMAMAAAAAXXSMAMAXXAAXMAXXMXXMAMXAAMMXAMXMASAAXSASMMMMASMSMSASAMAMSXMMSMMMMMMASXMAXXXAMXMXXXMAXXAAXXMAMMAMMXMXMXXAM
MMSMMSAMXMMXSAAXMAXXXMAMXMXMASMMMSMXSAMSMSMSSMSMAMXAMAXMASXSSMMMMASMMMSMSASXSXMASMAAXASMSMMXAMXAAAXMAMAXASASMXMXSAMXXSXMSSMXSXXMSMSSSMASAMMS
XAAXXMAXAMMAMMMXSMSAMMSSSMASMSXXXAAXXMMAAMAAXAXASMMSAMSMMMMAAAAXXXSXAXAAMAMAMAMXSMMSMMMMAMSSMMSSSMSXSSMSXMASMXSAMSMMMMAAMXMAMMMXAXSAXSAMASAA
MMSSMSMSMSXXSASXMAMXMAXAXMASMXMMSMMMSSSMSMMMMMMMMAXAXXAXAMMSSSMMMXMXMSMSMXMMSAMAXAXMXAASMSXASAAMMXSMXAASAMAXAAMMXAMAAMSSMAMASAAMMXMMMMXSAMXS
MXAAXAAAAMMMMASXMSMSMXSAAMASXMAMAAMSAMXMXXXMMAAASXMSMSXSXXMAMAAXSXMAMAMAMMMXMASXSAMMSSXXXXXMMMSSMAMAMMMSAMAMMMSSSMSMXMAAMXSSXASXMASXSAMXASAM
XMASMMSMSMAAMAMMAMAAAXXAAMASAASXSSMMXXAMAMXMMSSMSSMAAXASMSMASMMMMAMSSMSAMAMSSMMXAMAMXMASXXAXAXXXMMSAXMASAMXXXXAAAASAMXSSMMSAMXMXSASASMASXMAS
MXMAMXAXAXXSSXSASMSMMMAMMMMSASXMAMAXSMMXAAMAAXXMMAMMMMMMAXSAMAMASXMMAMSMSSSMAAAMXSAMMXMAMXMSSSMMMASASMASXMAMMMMSMMMMMAMXAXMASMSXMASAMMMAXMAM
AAXXSSMSMXSAMAXMXAAAASAMAXXSXMMMMSXMXASXSSXMMSAMSSMMXSAMSMAMSSMAAMMSAMXXAMAMSMMMASASMXMSXSXAXAAAXMMMMMMMMXXAXXAXXAAAMXXSMMSAAASAMXMXXXXMXMAS
SASMXAAMMMAAMMMMMSMMMMASXSMXAMXXAXMXMMMAMXMMXSAMAMAAAMAMXAMXAXMMMXASASXMMSMMMXXMASAMXXXMASMMSMMMMAAAXASAMXXSXMMSSSXSAXAASAMSSMSXMASMMMMXASMS
MASASMXMAXSSMXAXAMMXSSMMAMMSMMXMMMAMAXMXMAMSAMXMXSXMAXAMMSXMASXMXMASAMMXAAAAMSMMMMASMSMMXMAXXXAMXSMMMMSASMMMXXAAMMAAAXSAMXMAMXMAMXSAAMASMSAM
MAMMXXAMMXXAMSSXMSMAXAXSMSMAAXMASASMSXMASAMMMMSAMXXMMSXSAXXSXSASAAMMAMSMSSSSSXMAMXAMMAMXMSSMSMMSAMAXSASAMAAXMMMSSMSMSMMAMXMSMSMSMMMMMSAMMSMS
MMMMMSSSSMSAMAXAAXMSSMMMAAMMXXAMXAMAMASASMSXSASMMMXXAAXMMSAMAMAMXMXMASAAMAAMAMXASMSMSASAAAMSXAAMASAMMXMAMSMSAMMAXXXAAXSAMAXASAAAAAAXXMASASXX
AMAXMAAAAMSAMASMMMMMAAAMSMSMMSSMMSMMMAMASAXAMMSAAAMMMMSXMMAMXMMMSMMXXMASMMMMSAMSAMXAXAXXMMSAMMMMXMMMSXSSMMMAMXMSSXMXMAXMMMSXXMSMMMSSXSAMXSMM
ASASMMMSMMSAMXSAXXXXMMMXAAXAXAAAAXAXMMMXMMMXMASXMMSAASXMSSMSMSAAAXAXSAMXXAMAXAMXASMMMAMXMXXMSXSXAAAXXMAMXXMASMMMMAXAXMXSAMXXMXAXXMXMASXSMSXA
XMASAXXAXXSAMXSXMAMSASXXAMSMMSSMMMAMXMMAMXMXMXMAMASXSXAAMAAAAXMMMSSMSAMXSXSAMAMSASAXXMAXMAMXAASXSMMXMASMMXMAMAAAXXSMSMAMAMAASAAAMSMSXSAMXMMX
XMXSAMSSSMXXMAXAMAASAMMXXMAXAAXXSAMMAXSMSAMASAXAMXSMMMSSSMMMSMMSAAMAMXMASMMMSXMMASXMMSMSASXMMXMAMXXMSAMAXSMMSMSXSAMXAMMSMMMXAAAMSAASAMMMASMM
XXAMAMAAAMXXMSSXMXMMSMMMMSASMXSASAASXMXMAASAMMXSAMXAAAMMXXSAMASAMXSSMSMAMXAAAMXMXMMMAAAMXXAMXMMAMMMMAAXXMMAASXMMSASXMXMAMSSSMXSXMMMMAMASMSAS
SMXSMMXSAMMAAXMASMAXAXAAXXXXAAAAXXMXXXMAXMMXSXAMAXMSMSXSXMMAMXMMMMAAASMMMSXSMXMAMAAMMMSMASMMAMMAXAAXSSMSMXMXMASASAMMSAMMAMAAXAMAMXSSXMASXSAM
MAXMMAMXAAMMSMSAMSMMMSSSSSSMSMMSMSMSSSSXSAMXAMSSMSAMAMMMASXSMSXXXAMMMMASAAMXAXSAMMMXAAAMXXASASMMSXXMAXAAAXMAMMMMMAMAMXSMAMXMMSXMMAAMMMASXMAM
MSMMAMMMMMXAAXMMXAXAXXAAAAXAMXXAXAAAAXAASAMXMAMAAMAMAMASMMAXAMXMAMXAXXAMMSAMXMSASXXSMSMSXMMMASXAAASMMMSMSMSASXASAMMSSSXMASMSMMASMMSSSMMSMXAA
AAAXXMASXSMSSSSMSXSMMMMMMMMSMMMMSXMMSMSMXMXXXSXMXMXMXSXMXXXMAMXMASMSSMSSXMXSXASAMMXAMXMXXAXMXMMMMXMAMXXAXAXAXMAXAASXMMASXMXXASAMMXAAXAMXASMS
SSSMSMASAAAXMMMASMSASASMSMAMAMMXSMMXXAMXAMSMMMXMASXMAMMMMMMSXMXSAAAAAMAMXXAMMMMAMXMMMSASMSMSMMASXMSMMAMMMMMMMSMSSMMASMMMMMSMMMMMSMMSSSMSMMAA
MAAAXMAMMMMMAAMMMASASASAAMASAMAAMASAMSSSXSAAAXASXSAMXSAAAAMMMAAMAMMMSMASMMXSAASAMAAXXMAMMAAAASASAAAAMASAAAAAAAXXAASAMXAAAAAAAXAAAXAAMAMXAMXM
MSMMMMMSAMXSSMSXMMMXMXMMMSMSMSXXSSMXSAMXSSMSMSMSASMMSSMSSSXAXMXSXMASMXMSXXASXMSXMAMSAMXMSXSSXMSSMMMASMSXSSSMSSSSSMMMSXSSSSSSMSMSSSMXSSMSMMAX
""".strip()

if __name__=="__main__":
    main()
