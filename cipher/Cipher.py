
class Cipher:
    def __init__(self, text: str):


        self.text = text

        self.rus_alphabet_upper = ["А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З",
                             "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р",
                             "С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ",
                             "Ъ", "Ы", "Ь", "Э", "Ю", "Я"]

        self.rus_alphabet_lower = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з",
                                   "и", "й", "к", "л", "м", "н", "о", "п", "р",
                                   "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ",
                                   "ъ", "ы", "ь", "э", "ю", "я"]

        self.table_methods = {
            1: self.str_table_1,
            2: self.str_table_2,
            3: self.str_table_3,
            4: self.str_table_4,
            5: self.str_table_5,
            6: self.str_table_6,
            7: self.str_table_7,
            8: self.str_table_8,
            9: self.str_table_9,
            10: self.str_table_10,
            11: self.str_table_11,
            12: self.str_table_12,
            13: self.str_table_13,
            14: self.str_table_14,
            15: self.str_table_15,
            16: self.str_table_16,
            17: self.str_table_17,
            18: self.str_table_18,
            19: self.str_table_19,
            20: self.str_table_20,
            21: self.str_table_21,
            22: self.str_table_22,
            23: self.str_table_23,
            24: self.str_table_24,
            25: self.str_table_25,
            26: self.str_table_26,
            27: self.str_table_27,
            28: self.str_table_28,
            29: self.str_table_29,
            30: self.str_table_30,
            31: self.str_table_31,
            32: self.str_table_32,
            33: self.str_table_33,
            34: self.str_table_34,
            35: self.str_table_35,
            36: self.str_table_36,
            37: self.str_table_37,
            38: self.str_table_38,
            39: self.str_table_39,
            40: self.str_table_40,
            41: self.str_table_41,
            42: self.str_table_42,
            43: self.str_table_43,
            44: self.str_table_44,
            45: self.str_table_45,
            46: self.str_table_46,
            47: self.str_table_47,
            48: self.str_table_48,
            49: self.str_table_49,
            50: self.str_table_50,

        }

        self.digital_length_map = {
            "0": "ax",
            "1": "bl",
            "2": "cq",
            "3": "dm",
            "4": "en",
            "5": "fo",
            "6": "gp",
            "7": "hr",
            "8": "is",
            "9": "jt"
        }

        self.dict_space_positions = {
            "0": "fJk",
            "1": "QhT",
            "2": "ZxB",
            "3": "mAv",
            "4": "DlR",
            "5": "gPf",
            "6": "NsE",
            "7": "tWY",
            "8": "CqM",
            "9": "Vuz",
        }

    def count_rus_chars(self):

        text = self.text
        return sum(1 for char in text if char in self.rus_alphabet_upper + self.rus_alphabet_lower)

    def encode_length(self, length: int, digit_map: dict) -> str:
        return ''.join(digit_map[d] for d in str(length))

    def encode_space_positions(self, space_positions: list[str]) -> str:

        encoded = []

        for pos in space_positions:
            for digit in str(pos):
                encoded.append(self.dict_space_positions[digit])
        return ''.join(encoded)

    def encrypt_text(self, char, rus_cipher):

        if char in self.rus_alphabet_lower:
            index = self.rus_alphabet_lower.index(char)
            return rus_cipher[index].lower()

        elif char in self.rus_alphabet_upper:
            index = self.rus_alphabet_upper.index(char)
            return rus_cipher[index].upper()

        else:
            return char

    def str_table_1(self, char):

        rus_cipher = ["E", "B", "2", "Y", "X", "R", "A", "O", "S",
                      "Z", "I", "K", "N", "L", "U", "T", "3", "F",
                      "P", "4", "M", "5", "J", "C", "6", "D", "7",
                      "8", "G", "9", "Q", "1", "W"]

        return self.encrypt_text(char, rus_cipher)

    def str_table_2(self, char):

        rus_cipher = ["M2", "1Y", "XR", "C0", "6Z", "V7", "8A", "WJ",
                      "N4", "LA", "Q6", "Z0", "3C", "YT", "F9", "K1",
                      "SD", "B3", "PJ", "R2", "D6", "GQ", "HE", "X8",
                      "Z9", "5K", "2M", "JX", "U4", "LT", "AV", "OE",
                      "0W"]

        return self.encrypt_text(char, rus_cipher)


    def str_table_3(self, char):

        rus_cipher = ["IPM", "T59", "X5T", "H2G", "QKT", "AZ8", "1PA",
                      "DSS", "1CN", "BV0", "N4V", "5LZ", "37W", "IP3",
                      "690", "DIF", "W1U", "QZM", "0C8", "K5X", "EDT",
                      "LBT", "H7O", "15J", "LCU", "X6K", "R52", "Y2I",
                      "0FP", "T3R", "2RH", "C6K", "7RH"]

        return self.encrypt_text(char, rus_cipher)


    def str_table_4(self, char):

        rus_cipher = ["BN0Q", "9JNI", "S7C1", "A071", "J16M", "BOXJ",
                      "CLQU", "Y1YW", "T7F5", "4ZTU", "575Y", "WEWT",
                      "JFGQ", "DBE4", "ADX0", "K5MD", "IBTF", "QR4E",
                      "W7W1", "G8BW", "FDKL", "0LHO", "2Y07", "JCHN",
                      "JVKB", "1K50", "GKLW", "RAC7", "GQB9", "LPCU",
                      "689T", "Q3A6", "CRMQ"]

        return self.encrypt_text(char, rus_cipher)


    def str_table_5(self, char):

        rus_cipher = ["XISZU", "WRHTC", "OF6NQ", "RD648", "9CJON", "WCVW3",
                      "R3D5X", "KEZ14", "SN6NO", "I7KC8", "FEE7X", "LGVQP",
                      "XW9CB", "UEPX9", "GAMW1", "WKV5F", "SDV2D", "DCPX9",
                      "E1MWU", "QWL7I", "6I7VA", "X6WOV", "AGIP9", "KVSUK",
                      "42TZW", "4NDNE", "0B6F2", "EEFHM", "JVGMP", "XIFRC",
                      "G6FPK", "WVZZO", "8YO6A"]

        return self.encrypt_text(char, rus_cipher)

    def str_table_6(self, char):

        rus_cipher = ["IDLQ5V", "5CLCZZ", "THG77K", "20CQPG", "HNR399",
                      "JPX46D", "GVPODT", "WTXKQ5", "DMFA8H", "S0RFA5",
                      "4ONA26", "ZK7EZ0", "TH6XBE", "6STU3Z", "J976GK",
                      "KUYX89", "6282FP", "ZTIGDY", "WMAZFX", "P3Y8DZ",
                      "XDVGJ4", "1RLV4P", "HZMBLH", "N1U3TH", "L77LDK",
                      "ECL21U", "2SXHGV", "943FLP", "5H5XUI", "RA4CPT",
                      "FPUS2U", "KVI8LO", "1ZTZ7Y"]

        return self.encrypt_text(char, rus_cipher)


    def str_table_7(self, char):

        rus_cipher = ["F8B9MFZ", "UZGLA96", "OH915T8", "7QWGEK2", "FA5TJQB",
                      "Y86LA7X", "KTMATDV", "BR3XYJO", "1AZTSEH", "9DBM5RS",
                      "WM7SGFO", "R32SS27", "Q237GB5", "6M8Q6W2", "CF2CVQT",
                      "U4IG10X", "JOCC9NP", "PNS0T50", "KTGLWOK", "6J9UF4B",
                      "BAEKQ15", "UH47NA8", "PO3RQFK", "9985BKP", "F7N0RIK",
                      "DXSBUBA", "1BMM5FY", "7FOE99P", "XFZRJED", "0CH9CIK",
                      "KMOW5D8", "ZX5GON1", "EZML938"]

        return self.encrypt_text(char, rus_cipher)

    def str_table_8(self, char):

        rus_cipher = ["X73H3SRO", "P3KFMOSN", "O6ATYS6Q", "7Q8CZRSG",
                      "P7UA7D3Z", "Q3LOJGSI", "GN9TBWCO", "EUL51IB3",
                      "JWJ8I0OG", "1LYYL2LZ", "MC4GQOH6", "XR4IXHK0",
                      "YJH92WNN", "LB8EE3MT", "XB288B32", "PMMDH5B0",
                      "044SAK4I", "ZG1NMZCI", "HFI1AK2I", "ZW5ZMRID",
                      "26HHPBLK", "9Z3K36IF", "R6GHA1ZJ", "VBOEQUIL",
                      "X2UWE21I", "QZXNXAW6", "DH8N2JIK", "CXVYNNPX",
                      "M3Q5YY1I", "JPMCHNX8", "5D27D4PR", "PCT0T2VU",
                      "O1UL4KT6"]

        return self.encrypt_text(char, rus_cipher)

    def str_table_9(self, char):

        rus_cipher = ["UTPK9IFBO", "WXJFV6Z4Q", "008PPGU5S", "6QGXOGKG4",
                      "VZHHTCDKK", "OBO0ZTE9O", "68P7ZSQQE", "229BELTQ7",
                      "J7HUMA0D5", "YGSJFM9LG", "DMW0RPPKD", "E68CMM97U",
                      "R8S9LTEMG", "PD5DM373D", "56APXA7HA", "Q817M2BEI",
                      "W8P68VRIC", "M3BNJN4OR", "YN47O18QN", "SQJ3P3CLO",
                      "XB7L1G6XQ", "7WJ78OV8L", "GSQ1ASU5Z", "UOIP3X14J",
                      "FWSRT7IVN", "C148UAHUL", "95FOKOQXR", "HWNANAHXL",
                      "B6DAQ84O9", "MXQJCJVXK", "QV1X9K9UX", "AK8D6P01W",
                      "JIYTKS2SH"]

        return self.encrypt_text(char, rus_cipher)

    def str_table_10(self, char):

        rus_cipher = ["7J9T3WFGQX", "R5PNOZDKYH", "VBG3XQ04AU", "XQJEMTL56D",
                      "H8Y4ZARCTU", "L3MKGU2SJV", "QZKPYH7D81", "YJL7RU4X2A",
                      "N5WXYDKCBT", "SPT9ERGAQM", "O7KLZ2BYHX", "G91PQVMTSU",
                      "ZQAJUY6LRC", "E5BGYK7JMU", "M3XWRTDVYA", "JLUF7QNBX5",
                      "DKYT1OMXCJ", "UQXL9NGH25", "TAXK3VYWJM", "QJMYOBCFRT",
                      "PNR78KJGVX", "W3DQFZLMUY", "B8YXMGRKZH", "F2UOEKNLWS",
                      "C7RMAJYHXD", "86PXNKYVBJ", "Y5OJCUZKQM", "TZG41FURNL",
                      "XVUAJQMT9K", "0DRYEFLBWC", "S4LQPJMHGY", "KNXZJTYRU5",
                      "LMCOTQJW9P"]

        return self.encrypt_text(char, rus_cipher)


    def str_table_11(self, char):

        rus_cipher = ["UL7ZVRTFXG", "J92MKLHD0B", "TYXGAPFZVR",
                      "K57WOMDUQJ", "FCXGZ49LPA", "R1EVT9XDJM",
                      "3JQYKHULXT", "MWXKPD7JUG", "BQZ5TXRY0L",
                      "GDFKYVJXCN", "98LUFCZOWT", "AHYZTGJ34X",
                      "EQN53XUY7R", "PUCXGQRZJL", "YVMH64KNJP",
                      "L5KYFXZRMN", "XGJZ29HOCU", "RWMT3PZVGJ",
                      "ZLBVUG9EXF", "HJYM2BVCXW", "TBQ9PXJLCM",
                      "NYXVWRA7LZ", "61KUCXJGYH", "DRVX9HQJUE",
                      "OZ74YJBNKT", "WVGEXA53UR", "KQY1TMBJHX",
                      "XF9LTPYGVU", "MJPHZU6XYQ", "CYTJK3BZRU",
                      "D5VXTJ8MHA", "RNJQVWHU6Y", "SBKZYOA8GM"]

        return self.encrypt_text(char, rus_cipher)

    def str_table_12(self, char):

        rus_cipher = ["RPLTGU3XJQ", "W9KXFYMHP8", "TYL3BVRMCU",
                      "JQBZK6WN7Y", "X8UDZVPGHR", "FHAYMRK29X",
                      "GMXUTCVB1J", "PYQK34NWUL", "ZXMHRKFJQ8",
                      "NBYDWZ7TGJ", "UBGYX5MKLR", "AJWLRTVUZK",
                      "MWYXVGJQU9", "CQPRUXTAZY", "LJYXZMFQWV",
                      "D7ZRMXQ2GH", "VKF8JQYX6R", "YGBNRXJPTW",
                      "KTXWJY8U9R", "XEWTMZRLUG", "OVKPYJBQXL",
                      "QWYXZRGTLP", "HBJXTPYARU", "T4WRXZJMGB",
                      "J9KXZRLMVY", "MXYUJQBGWT", "RUXLPWBTGM",
                      "ZPYKLXJWTV", "EDXTRUFGWQ", "LBYWVJXZGP",
                      "C8KWXMPUJL", "GWZJLKXTPQ", "NVRJXZWGMB"]

        return self.encrypt_text(char, rus_cipher)

    def str_table_13(self, char):

        rus_cipher = ["D7PKT1JXAG", "XCBRV9KLUG", "9LJTACUMWG",
                      "FYKZ8UQBXM", "QP7YVKCLTZ", "WJXAGQHMBY",
                      "KTCXPV9JYA", "ZVGQYBTRKX", "UMYJZBKLXR",
                      "LRTZKGBXPU", "N9KVJXTCMP", "HGFQJBXKPY",
                      "OVYMXJGRZC", "TKJPQ9UGMY", "BXYVRLKMPJ",
                      "YJXAGTPKLZ", "MRGKPYXJUZ", "AFQJZKYPVX",
                      "CVTKUPJXRY", "LUBXKMGYJT", "ZPJXAMYRGK",
                      "RKGZYXJMUT", "T9YKPXUGJC", "JMQZKYVRPX",
                      "WXGLYTMKJP", "PNJXUAKLMG", "KTYPMXBGJU",
                      "QMGYXAJKVP", "YGXPLTJUKR", "AXJMKZVQYU",
                      "BJTCYKXGRP", "ZKPVYJXATG", "XRTYBKGJZV"]

        return self.encrypt_text(char, rus_cipher)


    def str_table_14(self, char):

        rus_cipher = ['8H1ZO7TABM', 'MPCQRPLL73', 'N5YV35EY9Y', 'QEGGRZ9WD7', 'C1ILZWCJGH',
                      'GQZK5J7BFT', '58E9I9O7ZU', 'D7YRS7PM5B', 'ZW59BPJX72', '6DY7XTNYUQ',
                      'T7EMDCWHW3', 'MP04ZC4O0L', 'H4AL73KZ1B', 'CR49NZQXMG', 'XKWPVEXE3U',
                      'T8FWWK1FXT', '0D65IUKL9D', 'INZ2AKG0CG', '3UBMTB19HV', 'RG7E5HL3I7',
                      '9YF2WSBNQ8', '3EM4JWBSAE', 'NJPHGV3M7R', 'HYG8IPD0JQ', 'TOWO7HMG8M',
                      'KH95QF8Z9W', 'B3FN9XX38N', 'CV8U09A6DK', 'K3RQAGUDME', 'EM6FAYO57U',
                      '2VZPV6B75Y', 'UV5TR3XVVR', 'OEXY2HL8SM']

        return self.encrypt_text(char, rus_cipher)

    def str_table_15(self, char):

        rus_cipher = ["ZKPXVGUMJT", "QGYZKJXUMP", "MKJXZUVRAG",
                      "MXRTJPZYGK", "YXTJUKRMGZ", "LZJPGUXKTM",
                      "GTUPJYMLKZ", "UBJPZMYKVX", "JTXPYZMKUG",
                      "KPGXJZATVU", "FLTRJXMZPY", "RGTZMKJLYP",
                      "JMKPYTZRAX", "XTPMZKJYUV", "PQZUXTYGRK",
                      "ZUVKYPGMTJ", "FJTYXKZLUR", "QUZKPGYTXJ",
                      "MGPXZUJYRV", "RYXKTPMLZG", "LYRPTXGMZU",
                      "GXLTMKYPZU", "ABXZJTYKPV", "WXYAKTPRMJ",
                      "QAJTZYPGMX", "JUGYRMZKLT", "KLGJXMYTZU",
                      "TKYPUJMXVG", "PVZTYMKJXG", "VMZJGRXTUL",
                      "UZJKTGXPYM", "ZXYUJRVKGA", "YVGRKPTUZX"]

        return self.encrypt_text(char, rus_cipher)

    def str_table_16(self, char):

        rus_cipher = ["5VX8YZ0AB3", "KL2MN5PQ8S", "Y7ZA0CD3FG",
                      "2JK5NO8QR0", "3LM6PP9RS2", "4MN7QR0UWH",
                      "5NP8ST1VXG", "6OR9TU2WYL", "7PS0UV3XZS",
                      "8QT1VW4YAE", "9RU2WX5ZBV", "0SV3XY6ACM",
                      "1TW4YZ7BDD", "2UX5ZA8CER", "3VY6AB9DFU",
                      "4WZ7BC0EGK", "5XA8CD1FHF", "6YB9DE2GIN",
                      "7ZC0EF3HJI", "8AD1FG4IKO", "9BE2GH5JLA",
                      "0CF3HI6KMP", "1DG4IJ7LNQ", "2EH5JK8MOX",
                      "3FI6KL9NPJ", "4GJ7LM0OQM", "5HK8MN1PRV",
                      "6IL9NO2QSB", "7JM0OP3RTS", "8KN1PQ4SUT",
                      "9LO2QR5TVE", "0MP3RS6UWM", "1NQ4ST7VXW"]

        return self.encrypt_text(char, rus_cipher)

    def str_table_17(self, char):

        rus_cipher = ["DB7F8B3897", "A3AD96671A", "CDE7F2E98E",
                      "A58A7057CD", "16D7D62569", "8E9A23E477",
                      "2E4F08AC1A", "514E2F1CC2", "649A3D6CD0",
                      "C7C291134A", "E230260C08", "895D1377C0",
                      "BF00A68974", "A2E70EFFC9", "C63AE0EBCA",
                      "2563059187", "E30E52D14E", "99D7DF572F",
                      "3B28C24261", "957D159241", "3D779D5767",
                      "E270061E61", "7BEA870B0A", "70F4088E9D",
                      "49B78208B2", "576266CE1A", "0416C15FA7",
                      "6D080F969D", "48EBC47C39", "E478F0D8A9",
                      "717B8A446A", "8368C56AD0", "FD486E7449"]

        return self.encrypt_text(char, rus_cipher)

    def str_table_18(self, char):

        rus_cipher = ["B861E106D2", "9C9639A05D", "B23A95F8C6",
                      "B573E2E457", "20F78A20A0", "4A4046C73B",
                      "BEB517B50E", "574DB99C6A", "3AD6B5000B",
                      "1584B8EBF1", "3D02C822BB", "0565432917",
                      "CA92C5A48A", "7872EFCB8D", "164EBB0CDD",
                      "680CFBF4A9", "018E024C8D", "5EAAB775BE",
                      "AB889A79F7", "D3CAB0D1E4", "7AD56A3E94",
                      "6F1ACFB3E6", "B0FBEBCC4E", "7277F884C4",
                      "BE284DBE4D", "29AFDA7170", "4B764DF095",
                      "D88D398C0A", "2756592D28", "449557DED0",
                      "1F76E548B2", "4F84095A08", "D7E4246373"]

        return self.encrypt_text(char, rus_cipher)


    def str_table_19(self, char):

        rus_cipher = ["FAB47F472A", "2F71C848BC", "5CE2EBE55E",
                      "B4DBECE38A", "F3030499C3", "60AA36ACF5",
                      "1175C353B2", "9BB91B9BB5", "C6CC1B3EBD",
                      "3EEAEBD6EF", "2C560BF7F0", "06BE711915",
                      "B21AD27B18", "22171D2640", "5B19C90E8A",
                      "F9EAF5C154", "D35D048BBA", "93E3AA842D",
                      "42F009C8BA", "58598ED063", "9C876BCDFC",
                      "8716B55635", "CB0ADEF465", "6055726169",
                      "A5A7604079", "279ED4429C", "FCC3C64FC0",
                      "9394F4AE26", "0988E8E0EE", "C74A4AB9EF",
                      "984CB4D175", "29BB370282", "779751AB43"]

        return self.encrypt_text(char, rus_cipher)

    def str_table_20(self, char):

        rus_cipher = ["7A0AB9C187", "E6B48B2352", "D0D24FA748",
                      "FD8385A7C7", "979538C407", "CD7F89FC95",
                      "3B1D7C4644", "BD7C1207D3", "7E15ED20E4",
                      "5B72503A82", "700352F79D", "8FCD3B1C01",
                      "016F36012C", "CC2AC8950C", "7610EBA2DA",
                      "E02800038C", "36CA27E8F8", "D8B32E4360",
                      "AF071DB7A4", "423F529DF0", "FD35C6BDFC",
                      "618CC76C34", "536A67868D", "00E7515E7D",
                      "926B168CD6", "7896636FBD", "ECDD43C5FE",
                      "7940B202CB", "16779049A8", "8142A33696",
                      "069538816E", "7291233B38", "7F61B37EFD"]

        return self.encrypt_text(char, rus_cipher)

    def str_table_21(self, char):

        rus_cipher = ["540CF3750B", "BF7D48A055", "0D9A010393",
                      "9F7A98C147", "55E56A7A34", "D03D33E328",
                      "AB1DAF1805", "DEBF012715", "31C7BFADF0",
                      "BCA8663417", "1707A68220", "9E02D8C798",
                      "7675E76AE8", "36A2B81A3C", "EE21A05486",
                      "1D20C20010", "F0ED45E32B", "60E4FECAFA",
                      "79BECC5625", "AAC952E62B", "11479BDC3F",
                      "0F1D47BBBF", "96296938DD", "0432D14AE0",
                      "D19B3A0121", "B0161B7AB4", "17FC3546E3",
                      "7117F68613", "2B347E59BF", "0FE88C18E5",
                      "02D6E7B957", "CB297EAEF5", "3C2F2ABD2A"]

        return self.encrypt_text(char, rus_cipher)


    def str_table_22(self, char):

        rus_cipher = ["1B03ED4E4A", "4248304659", "BAD546F62F",
                      "B9D7C8909B", "32F17E9C03", "1EC95A289D",
                      "62C451A92E", "4068DD3A32", "869C2BB764",
                      "B41CE5D0D6", "F8E1395D26", "4F520F961B",
                      "4519AE82C5", "86A172CF2F", "28324AE68E",
                      "D844A00A9E", "D9BC33AD4B", "A8D36C37FA",
                      "5B4CA0A308", "0891D3761A", "6E23B1F9BD",
                      "E8FF16B218", "2F299EEDF6", "2792FD8FE9",
                      "CC5E9AD46A", "F031390E76", "3AC9AF06EE",
                      "BE0FCB34F6", "0A7336AB97", "D4D4074E16",
                      "8D6DAB00C4", "4B13808769", "F1CD383A7C"]

        return self.encrypt_text(char, rus_cipher)


    def str_table_23(self, char):

        rus_cipher = ["45BCEB2F34", "7CADB15052", "B6639CA4A1",
                      "3AFA4182CB", "F324AC9E64", "2EC93A06E5",
                      "86E784E607", "7FD776335E", "009075A8B1",
                      "17F89EA025", "D503FDD2CD", "25C3EAD32D",
                      "8F337C917D", "01913E1711", "7351799827",
                      "494399DE43", "E49DE03FFF", "6D04CA1D1B",
                      "5AC01EF059", "A027AAF391", "48553945AB",
                      "C95887F94D", "5B37ECCF5A", "DEF93AC927",
                      "92991A1377", "95B0FD5482", "302A7F3E91",
                      "6167BAC2AC", "1DEF8485F1", "6AD76A7F3C",
                      "86C0C53F19", "BF467AA8A6", "9E6F448055"]

        return self.encrypt_text(char, rus_cipher)


    def str_table_24(self, char):

        rus_cipher = ["9E46F56A7A", "B7AD11BCE9", "C89632218C",
                      "A9AB227D2E", "521B78E22D", "4ACE0486B3",
                      "DD44EC82FB", "69E91D008A", "654437D443",
                      "65C683912C", "B2FFF019E3", "66A9EE50A1",
                      "7A7FE483ED", "7154C29E96", "2235F4599C",
                      "9EE570090D", "475A58D905", "1D6AFF6E1B",
                      "921399AC77", "CB83678E54", "0C4D061E68",
                      "7CD90B2B78", "FAB969B322", "D1A161D11B",
                      "92A7587547", "89306C105E", "C7C5F63070",
                      "DA50BD71AB", "AD89147EF1", "83F671BC78",
                      "748BD3F458", "0C1E215D02", "C246DC8006"]

        return self.encrypt_text(char, rus_cipher)

    def str_table_25(self, char):

        rus_cipher = ["B5077B18E3", "9B3847256D", "DABDD414EC",
                      "353D3076FC", "77127A4FC3", "41BB5C2ADF",
                      "26CC247F81", "9FB10EAE13", "BCA351E6A3",
                      "672486A6C0", "2A81042AC5", "1C321EF4D1",
                      "AC22914CCB", "11F18E9C8D", "60E6A27B41",
                      "C7EB75612A", "46D3F9F096", "05588BC8E6",
                      "65B65DC1BE", "5508C6A1DC", "A759295F48",
                      "A3C2305A08", "83A40EFA1F", "9C4525DF38",
                      "A4BBC1D4E7", "5DB50AC3FE", "5E6D3C008A",
                      "90F932A49D", "695A587697", "F0AAB54FFA",
                      "4DF3EDEFC9", "A30B1AF376", "162151EC95"]

        return self.encrypt_text(char, rus_cipher)

    def str_table_26(self, char):

        rus_cipher = ["D29AE14A15", "9BFDAF97C4", "529138FBC0",
                      "B7FF51E48B", "9DCDDBACD2", "0B9DC38F70",
                      "D6361F8678", "6C9597E901", "DBC50D7507",
                      "5EC17A22C0", "4911015F2C", "0147FB007D",
                      "F4D06403F0", "4E03D3E83A", "4C53768D6D",
                      "BDC5DD7D2D", "160F3766CF", "79604CB8CA",
                      "B30970D1CE", "1044B95509", "BB2E8DCC26",
                      "91B3F6E152", "1B2AE3868E", "7929649805",
                      "52508C79C0", "B86549F7D9", "9CF792F8CA",
                      "6D00DC98C3", "6CC432F514", "7B4B5FB879",
                      "870CB94AE9", "5ED3B51DFD", "5C2FA4DA1A"]

        return self.encrypt_text(char, rus_cipher)

    def str_table_27(self, char):

        rus_cipher = ["904B6501B7", "13655434F7", "0ADCFDBE17",
                      "21A9C05E2F", "7630703034", "413E00C388",
                      "5B43ABD106", "BED5E36868", "518FFAB238",
                      "AE76FF7F06", "0F87780A8D", "04A58D9916",
                      "D37073DAFE", "E411EFFC48", "6DF2C7DD95",
                      "580E981892", "C7474FF97C", "B930F4A170",
                      "15C50F3557", "17FA5BCCF1", "3DC40EEBE8",
                      "65F212F343", "5E1EE0E5B2", "5DE79D86D4",
                      "9618B55965", "5AE08D3CCA", "A0A66C2786",
                      "883F8B04A7", "4319B8D2E0", "1D5546437E",
                      "5B5399E0BB", "29176183F8", "3AF3130F43"]

        return self.encrypt_text(char, rus_cipher)

    def str_table_28(self, char):

        rus_cipher = ["304D6F42E6", "08C70C5C53", "7016F88153",
                      "7EE8BE084F", "A7FD827168", "2852FB10B3",
                      "704F836BF0", "1D154ACDF9", "6177AEFCBB",
                      "E549D4797C", "BAFC7D32E3", "160814947A",
                      "26C6B322F7", "E9074AD33C", "C6CE86DC45",
                      "8530B7008E", "B1E795DF80", "37747D5977",
                      "7A276A0B27", "8BDB7BF486", "DBA7112CAA",
                      "896C23F87E", "4344A1B488", "680F2E603A",
                      "665E913D24", "04D55C40D9", "00BC1D7ACC",
                      "7014E4A04B", "3D6CF4DB79", "3B5DABD3A9",
                      "0D79E0E2D8", "4ABD1DAB13", "6CB52BA8F0"]

        return self.encrypt_text(char, rus_cipher)

    def str_table_29(self, char):

        rus_cipher = ["D5B050FD70", "963BFE773F", "ECBBCDCAF5",
                      "68B2EBD8E1", "0697D86D52", "F8E9468175",
                      "E88A6C1A3A", "F7FE4E5E0C", "73E9B7515F",
                      "E89FD00E96", "879884F113", "3B4A82B095",
                      "C0B8A3406F", "13B6F646BE", "D46F6E66BD",
                      "A83E516617", "5E5413E32F", "80EF8C5D29",
                      "09573C5273", "76A3D090B9", "D5316EE45A",
                      "7F4C7A3E39", "4DFC9975B0", "C6E6840D4D",
                      "25952246BE", "6CA48181F0", "4606C0BE7F",
                      "F27506B852", "96964C7943", "BB683A0D29",
                      "DF3D4E310B", "DC77C7E05A", "FFDE48507A"]

        return self.encrypt_text(char, rus_cipher)

    def str_table_30(self, char):

        rus_cipher = ["6DAAA01AD3", "F1E649D0DF", "314C963144",
                      "28B77EFE3D", "760DE8B80B", "371275CED2",
                      "2191070B77", "1D6F696730", "FA10047CF2",
                      "746467A254", "67B8D65366", "FB779D039C",
                      "2E42CC420C", "A3BF288038", "F34DF3E755",
                      "3BC5FD2B94", "B9C18DEF2E", "87E6F7E7A4",
                      "706860E577", "F5F7BB8AEE", "4B9344AA4B",
                      "B482505490", "458140AEC3", "D64C77373B",
                      "BF82219D98", "C3723545D7", "5B0A887F3E",
                      "440FD4964E", "F27E29364F", "105F950744",
                      "75C8E1422B", "BA093642D3", "A536EE95FC"]

        return self.encrypt_text(char, rus_cipher)

    def str_table_31(self, char):

        rus_cipher = ["CFF74D2BB5", "04FCE0A414", "AC1A80AF7E",
                      "FC77EE288E", "A44A6D2B2D", "74F8D26B8E",
                      "2F4F715B8F", "9E81C07039", "9B12AF47F6",
                      "654D1FEB09", "C8420C2B54", "C409B36040",
                      "B04D22E0CF", "8FE394349A", "1EAB569E79",
                      "F7BA7B23D8", "EACA766369", "D040C25404",
                      "174D3F675A", "F5076ED7A9", "E4DE3EE812",
                      "E2A6401C79", "51FAC7D6F1", "5D21D6D57A",
                      "79708A5A93", "FF300D4766", "AB85E6C421",
                      "2093F14DF5", "0C46F8405E", "A878A29B43",
                      "08ADEB9022", "9C796A8B67", "B53735B7D0"]

        return self.encrypt_text(char, rus_cipher)

    def str_table_32(self, char):

        rus_cipher = ['YJLOCUCJ75', 'DV1T8LNA6T', '9VQNWBYKGY',
                      'RKK6YNQXPR', 'QVCPFT05KO', 'BPJ5D3JVPH',
                      'Y9QR5H4QDG', 'N73KNXDSNT', 'N0IVC7T7PP',
                      'SJ2P37I3YW', '4AP7LQCH2K', 'RO4IZYZAK2',
                      'AS6YX61N1X', 'TLDRB8LGWY', 'R1M0L0XKX6',
                      'Y61F3V8RQP', '07O9KZIN8L', 'ON0A2YGCFA',
                      'I6OF3NO6SJ', '0ZNG62LKH9', 'X8BZUJQ2M2',
                      'I59JEGGPOC', '51J2V9I0W3', 'KUMU3S8QAF',
                      'I6CLHGLBOU', 'G43G6G5G4M', '5TFN80LFXJ',
                      '9XDGS6T6I9', 'P7B7XFY9TF', '0T1RQ5FXUM',
                      'FS5ZZVLMC9', '0FCEBT44U3', 'ZSLAPHRYMY']

        return self.encrypt_text(char, rus_cipher)

    def str_table_33(self, char):

        rus_cipher = ['FPGHLSBGDX', '1LLSTGRZC2', 'J4PKT3Y48O',
                      'AWVFTRLYP1', '6P3HMWDUPU', 'B6CHSLR2BZ',
                      'NXXVUIWSVY', '7S2W8DVMU8', 'WBK9UHL4PR',
                      'DMZEC4NC1T', 'V1ETEMEYTX', 'G7G2AMWIFA',
                      'W9RNL2RQW9', 'OUHR1AER5W', 'DHL8M9PBAT',
                      'YB3TPRUQ4M', 'GRXAY0LZV6', 'YTNRK49C9J',
                      'B9QH3WEA99', '6EXW0D9VRN', 'KM8G6CEZL9',
                      'CPFY5L5LVN', 'A4OZJXTFQG', 'Q7Y8U3PHKT',
                      'PE1Z90N9RS', 'XZ9JX8RXT7', 'WJPCFVE4NO',
                      'WHUYNH7SZK', 'ZAHW50OW2H', 'DTHNXNAJKA',
                      'DZZK8IPKRG', 'XK1UO5KAXF', 'V9M8CTG93S']

        return self.encrypt_text(char, rus_cipher)

    def str_table_34(self, char):

        rus_cipher = ['L78UCNE008', 'JBJG09LSAY', '2R06E9KP82',
                      'XJWGCJGEJ5', 'UAA86HMQMH', 'Y97UKJ8W81',
                      '2V9OTI0VGX', '8AWUQIE9MD', 'X0PV6ZEP8P',
                      'T77EZNS1KL', '7JXG2Y8H90', 'R9P4RUM2UB',
                      'ZWTTGNY4MP', 'MPAC9RWZ2O', 'GVOCE6JP0X',
                      'GVOQX0T2IM', 'BL5NR4C3NJ', 'HHJ0RPFECG',
                      '4JXX46G0PO', 'T8PLNPKITG', '94FZFY9SL4',
                      'O8SPAX1ZMS', 'NC6RGZIDNY', 'VJ3IYCGX70',
                      'YENLFDA1C6', 'BJMBRMG8TN', '7HFSDDULPQ',
                      'X2A3P53SL8', 'KLSNAXP4NP', 'WH5QMEI5RI',
                      'TFFZBHWXKP', 'L82MK04T3P', 'S0RZ8CQK6V']

        return self.encrypt_text(char, rus_cipher)

    def str_table_35(self, char):

        rus_cipher = ["JWK14B8OKV", "3MKUPY461I", "ZQCD9572IS",
                      "ACWASKEFEX", "QT3SKOAF52", "30CACMIK1D",
                      "QRMH5ETY3B", "MXTBD3ZUQF", "SJLP8RD489",
                      "8JI7A94X0F", "H8BRRD1WUH", "TB40T212PT",
                      "9U9W2H19NQ", "ZG4ZSDAZ0T", "Z1B2NCUI2W",
                      "O8H729FZF8", "192UKUMF3T", "QCGY1KX359",
                      "7P0J8NHKLN", "YARHE8ONK9", "DQ9J4DKE8V",
                      "5DSIV6CCNT", "V2EAWRLJJB", "5E7RCH4AFY",
                      "DHIL4ZS8KX", "ZJ8SQVGV97", "K44OCHYZH3",
                      "98VSFKDBQW", "X53NP0VKX4", "O1ZDZJ3GEL",
                      "S3XW0ANUX5", "JEAPDAXEG5", "L75LQL8GQA"]

        return self.encrypt_text(char, rus_cipher)

    def str_table_36(self, char):

        rus_cipher = ["5BIGY50DHN", "SI7339V3JQ", "I5N7NHHBX0",
                      "AKWQ84E3AJ", "OWV7IOO4H3", "N6HDN7UOR1",
                      "R9UU9UBELX", "B0QP3NRLLB", "N3G31FH06P",
                      "U9QBHAVQOF", "TON9J74C5G", "HT3QZ983FS",
                      "ACR447CC5H", "Q27PSWM7OW", "DIL1JLJYIM",
                      "ZQ6HE6AICT", "8CS8SXHO90", "IA5L4J2W0B",
                      "AHEO4W9YYK", "IL1914HT1H", "U4Z7V795Y7",
                      "BY88WRDDPE", "RR9ATNTSJL", "DGW1C7XST3",
                      "U352NEJG9Z", "4KIJ14191P", "MC0MS8OT41",
                      "LZQOKWV3YP", "PJJ0XMBUUT", "5R21C4WV2L",
                      "EUVIMWORJ3", "SEONC8MQDM", "PJY021HSYF"]

        return self.encrypt_text(char, rus_cipher)

    def str_table_37(self, char):

        rus_cipher = ["6UKA2VOSCQ", "5Z8I8JL6U4", "0VQ63ILP8F",
                      "L1W46FLWDW", "F4C2BHRKEP", "L5AK0FJBRT",
                      "0X13R9S7Q7", "A5R549XD6X", "VKRPR09NK8",
                      "BH5DOIEE8H", "C2Y4FRDAMO", "NH2KS3X2H0",
                      "LS0M3MWF2P", "ONJE9PYUX3", "BXUUAY4UIP",
                      "WS2YOVQ4OH", "I8CQZ8Z1UT", "42RM3HOZVU",
                      "IWE6DXOIAU", "JUG1N5V9CL", "J76ZNGR5NL",
                      "SV9A96OIXL", "6SIOA2OZTB", "RCRGL2GPLY",
                      "8MIZNTZN3N", "EDSU2JTO3D", "H9BW4IUYJB",
                      "MFU3SUADJX", "EHLMBIIS9R", "H933NWMEBD",
                      "8EAZZE8EO4", "90B1XCKRSV", "Y9DWIMQAD4"]

        return self.encrypt_text(char, rus_cipher)

    def str_table_38(self, char):

        rus_cipher = ["MSPA57ALEG", "VNWU06HTG1", "Z51GKSL1ND",
                      "MFI59QN0Z4", "OSC6O5G82E", "D2KSP86QYG",
                      "WLN95XBGWO", "WLV76IX3SX", "5OABKFXI9M",
                      "DOE1WKCB2W", "7S34UVMEHI", "VVMG6AQZJA",
                      "MGZ35OP1WS", "NUO4VKKCQC", "OT1D5SPC9W",
                      "JUIVZ5VJZ5", "U7QA2RVZNW", "QJNL920ZUJ",
                      "ZQFC0Z32L8", "152VVUPHAT", "PAAY1XBJ71",
                      "O4WQJ927OO", "QV5XGDN3O6", "KPYJHPQTGA",
                      "EBG8NVSFYM", "CJ6BCQQU6T", "WJXRUU1P0E",
                      "WI534Z0HK0", "7D4ODX24N7", "0VILASOAVY",
                      "6CND8RVCUS", "M917Z6MY2A", "0PJ1Y99O6X"]

        return self.encrypt_text(char, rus_cipher)

    def str_table_39(self, char):

        rus_cipher = ["ZHR355J5TS", "4I2RVXRDBP", "6ZENWEEU63",
                      "PSW1IEXGVP", "FAW2Y0O8RZ", "PBI3D9NFZN",
                      "UW8ZGT0KIY", "DAOJ50UTQ4", "AG5NEUWWTP",
                      "GO3UVRZQ62", "2O9YNAV183", "WSLHPXH59R",
                      "9K54E5QJRI", "Y3Q6S5G7JH", "V2NRIM85LG",
                      "SGO972GEZ1", "3GPPS9E1PY", "J8VGJJCP18",
                      "Q4FX5TG41S", "2KLKE0PGKU", "7YNNBVBCQN",
                      "AOA5FOVLFS", "38O91X5ZSD", "G206SR8FI1",
                      "JRYQW7PAWS", "1BFJ57QB6A", "5T2CR4WSU2",
                      "7KEGR2B05R", "6TAPINCCOR", "R2GK3UC8TB",
                      "DXK2T6FH03", "VOEWK3SUGP", "TAE4PKJ5VR"]

        return self.encrypt_text(char, rus_cipher)

    def str_table_40(self, char):

        rus_cipher = ["F8NGHF5P7T", "GQZ5QZXXDS", "3F7MNZNWZZ",
                      "WF7HS8HQ84", "KAS24LHQ6Z", "VS5D4RQDKJ",
                      "LZXUFBW8A9", "M4AZUXPN7H", "3XXYSCD954",
                      "QQG8D75MX2", "EENEX3E5CH", "4YREZUNWJ2",
                      "ML6GSX3DD5", "X4MRQXTBY6", "M3YHAY6KTN",
                      "5PZAJUBQD6", "HNYAXEWPA5", "V3RD68VZYK",
                      "MZNJ9AJU2H", "B87PB6TNGH", "LDMPLEAGM8",
                      "EFGKLB25ZX", "TFGTU2TU7H", "DDKBEX7HWY",
                      "R2Y9JPT3N5", "TPPWZP62EA", "CZSTVRR3LL",
                      "VQW9GUN48V", "6428KMHXY6", "VAMXMXGWEJ",
                      "8RXWCJLZBS", "D6ZM9CAHMN", "FA4BNZL3AR"]

        return self.encrypt_text(char, rus_cipher)

    def str_table_41(self, char):

        rus_cipher = ["77AQH6RWYM", "V7JZEKZ6C3", "QNFRSVC4J4",
                      "LMKNTXPEDE", "WXY9TC8H4L", "Y74QF6B97W",
                      "4QNNV7K4WW", "ZW5X9KYTA8", "73WR2QBGCN",
                      "MSJMV4T77U", "N87863NYB8", "3VVVZC5E5M",
                      "2Y3U6DGT9R", "6EZQE8E9XX", "N99V56EMYX",
                      "KAMB5BA4ZK", "MCM3HP45Q2", "GNE43C4SAQ",
                      "TAKMGSSQ5P", "K68VT9XCDB", "9VUL49HS6N",
                      "LHN4K5VSMH", "JDWFSL26QS", "B5ZWQXRM4P",
                      "64NR7MJRVU", "NWK73B6PM5", "T7ULGZWAJE",
                      "YB7YFLYWD7", "YC2PZSKQYN", "8HHFPZUYZK",
                      "JN6C2ZVZSN", "979LQGXHTV", "J4YEYMN76R"]

        return self.encrypt_text(char, rus_cipher)

    def str_table_42(self, char):

        rus_cipher = ["W7WEJZJYUK", "C237NPQS9S", "KHEXKN7H3F",
                      "HUN4AA272B", "AZLF3NN4U7", "NYWGYV5GZE",
                      "JMX5H65YUC", "2PLK2BP763", "QPY97PF22C",
                      "RHKTN95HJK", "LYDRVV7FXK", "3KZMUAMS9F",
                      "PFTSNGH7QA", "4Y95V3V46Q", "KLBM9N4BVN",
                      "V6CQ6S8ZSB", "Q37X5WGNY8", "3PNERSEHSR",
                      "WHGCAQN3QJ", "JCUX3H79NB", "V7TEM4FMV2",
                      "KPUQBC85SY", "EF6MUPBFAF", "GEDQ5JT2QY",
                      "EKJXSLEUN4", "DFEJ64HFQV", "SUAJ6RLLXW",
                      "DSCAGL5UNK", "858BGW2KBR", "3B6QNV6YMY",
                      "3QZMC9N8N3", "7VYJUCR9FL", "4KFKTM7XX8"]

        return self.encrypt_text(char, rus_cipher)

    def str_table_43(self, char):

        rus_cipher = ["4YNLGLUP9Q", "WYMTYXWC9F", "XWVD3T2VC7",
                      "XUHV2LUKW4", "4X7VA3RBWQ", "TKWGKV7YZP",
                      "BTAX8SGZH4", "JPM3H2HR3Q", "NLT236DA6F",
                      "F5UAAFRB5X", "NW9CNB6JT3", "4AJWM62LWZ",
                      "SCGE652BZN", "89SVLCYT8J", "3K8QW78ACU",
                      "GSYWSZAPUE", "QE7UJ34TNP", "D3AXSMZULK",
                      "YHRKJDPQGC", "HQK6MMTUNC", "MK8YGRNU63",
                      "PYLH66TYNX", "NWHHDCGNGD", "WD3EPPT2LQ",
                      "UV84VGTWK9", "FEDFZ97THU", "DHSNAD2YFX",
                      "7U4NV24Y26", "BTFRQXZJPK", "DPZTHF5AFC",
                      "436UG6MGLQ", "RH8RNBM9F5", "NG27TRT82F"]

        return self.encrypt_text(char, rus_cipher)

    def str_table_44(self, char):

        rus_cipher = ["LYV9C4LUPR", "JJNW2REM6D", "DNRL6MLRW4",
                      "CNP2T8YYDN", "YB8ZV4WS4Q", "HK8Q64ZNM5",
                      "E7R234PS2X", "38FH3HR2XU", "CG4UK85G8R",
                      "2M9U5EZBW3", "ZTYBLLUUS5", "PCJ9K2L4AH",
                      "HZTM4VC64K", "6YJBARYDUA", "8PUUCMGBNU",
                      "E2YKSLPG7J", "H7DPY69S5G", "7YRUAW4Q9N",
                      "FX2ZBNRSPZ", "X33XWB8A29", "2UJ8Z54CUX",
                      "NGQFX9ZD78", "4UJQEH547C", "VBG7HHW4TV",
                      "TV2XJZA53X", "2LXRW32TGP", "UXJGWVHWVP",
                      "4MW2ZCZE6U", "83MC37TMQG", "GVAV9AV67K",
                      "J58M9H4XL4", "V3GXC3UW2L", "WJAMHSDVDH"]

        return self.encrypt_text(char, rus_cipher)

    def str_table_45(self, char):

        rus_cipher = ["7G7P47RX9H", "KXA4L67RJC", "J794WVTSP5",
                      "LTXX9Y5NTK", "F2GXRH4BKY", "BBDUXWA9PC",
                      "5GVREDRCTS", "HHAC7R7XFA", "TPKRRCCAU5",
                      "7Z4UYTGLPZ", "WFJ88EGH64", "BPNRTFT2U7",
                      "RHRUCU2UYS", "94R2LCUP86", "M2LTA6JN7B",
                      "9JESFPC8SK", "F2AJXVKFR2", "Q9L5LR4VJ2",
                      "JN58KA67J9", "8ZKD2EY3DA", "CNFQ8QQMK6",
                      "A244DSALR2", "L75P3ZB488", "EVP4PT7LAA",
                      "QPFNTSQ7K7", "95V3GD4WTP", "4GTZY89Q79",
                      "LHQQYJV8B7", "2QVGMEXTGE", "B8W52P8ZUH",
                      "7LHZBBZEW8", "F6N6UV9KXQ", "9HKQU9MVV3"]

        return self.encrypt_text(char, rus_cipher)

    def str_table_46(self, char):

        rus_cipher = ["U2ANLGCHFA", "X74LXVJZ2P", "DSWHC6NMH6",
                      "ML6FVFVQUT", "WQXCQ3VS48", "E9CAY6ZMKV",
                      "PCARFA4F5L", "FJW69VXJBV", "ANHTZJHG6N",
                      "XMJF88TYTC", "96QAMQCLEV", "MGXWKUUHLJ",
                      "MJJB7F57CJ", "ARKT87LYFH", "LX5NNDBNB6",
                      "FS9SEFD7ZX", "XH9QTNSGGM", "NMR9B5JX73",
                      "QATNTM79TB", "53E7GVBUCV", "2T97FCTYXQ",
                      "BX8NQMTXDT", "Y9NE2FRLD8", "7JV2NTGTAS",
                      "7Y4DNSJCSD", "WMPSDYAX37", "UH6M7FED4J",
                      "UFGNH5GEZA", "NKR8FJYMBQ", "9BP5DCLYAD",
                      "JZQZAHNDJZ", "9ZTGTWCWZZ", "XUPJVHG3DW"]

        return self.encrypt_text(char, rus_cipher)

    def str_table_47(self, char):

        rus_cipher = ["GWZAPV5AZP", "ARRPB5EJ7M", "PZUSLH3NAX",
                      "G8VWYBF6BG", "3C3S8LZM6P", "8QMYGXG8Z7",
                      "65B83NSSJE", "8HLEFZWFXL", "9HQYUX6V9V",
                      "VKUV82M8FE", "MQDZ5WY2DK", "4UZD6B3B34",
                      "XBFAJW59AR", "6MUR8AK27Z", "B726PBVCS4",
                      "QEC46HYPJM", "Y5MH87ZR8V", "C47SE7QY5V",
                      "7ZUGXX49J9", "VTLZXQ78UE", "UBQ2KWPUA5",
                      "F24HNWZQ64", "NR4WUVQXE6", "XJC6GYLBNX",
                      "K3JRTUKXS4", "P7HT4KEM8W", "2THFDC54Z7",
                      "HMG6WRTAEQ", "EJD5BSUPQX", "BX5E7YCKLN",
                      "FS5BLAYFEP", "8KSLXE539H", "8HAB3LLP6H"]

        return self.encrypt_text(char, rus_cipher)

    def str_table_48(self, char):

        rus_cipher = ["GF76ZDHQW3", "4DZE7KQR6W", "LD7WSBHZXH",
                      "DB25D76G9P", "M9DSRZV2XM", "P8TAMQ8BY7",
                      "JTSYPRDCM6", "W8UM42WSX3", "UKLT9HJZJA",
                      "R54A8LNR22", "8HXXLUVPV9", "PDB5NVDZBS",
                      "FFCWMGWVYL", "M2CDSRMPF9", "N44W779FFB",
                      "3L4LEVC8R7", "PURV67YEL5", "LLVNYZJR9T",
                      "FW6NBKJ4CP", "NTU7BUMAVW", "6STVH2VBHD",
                      "SWGETLHXH3", "3KEKU3T2HZ", "SPGBWRZCWL",
                      "DQLFVASXPR", "MBJXQKN8TT", "X62NU6VLA4",
                      "RYEDJBBD5D", "KXTQVU5ABE", "2JVSR8HREW",
                      "TDZUM9S7SM", "SD5ADZ7VSD", "YPGYHR586A"]

        return self.encrypt_text(char, rus_cipher)

    def str_table_49(self, char):

        rus_cipher = ["HEJMG5U9SN", "GN5FYH8FB8", "BTF9WXGKW9",
                      "AYWPVJQ8P6", "RGMDLAJAHW", "FXAZK48BBK",
                      "NW3YPPSSYY", "FR8S4BCCK6", "JKRVNZFHPR",
                      "SY3Y4AC82Y", "Y3DVQJLLXQ", "RZKWVS8WCG",
                      "MA8LWLFBD9", "ZQE4EU32BT", "7562J2MFWK",
                      "JL4XZ8X265", "6GL99SDWN9", "KP64ESNG4D",
                      "GDRFGTXXPM", "LTZ6QSH65W", "2N34RZ9T3H",
                      "Z83GJ6Y4AH", "JYCS2BS88Z", "UJFPJ5FWU9",
                      "JXAKZW272S", "XYPQ8Z3PCM", "APXARQZBRE",
                      "JCAPPQNS7J", "QKDHXLWYLY", "XV48CSKDQL",
                      "NJ285YNDMH", "SR3J99G4XT", "548NW9NKZ2"]

        return self.encrypt_text(char, rus_cipher)

    def str_table_50(self, char):

        rus_cipher = ["VBKQ6PQGUI", "A4HLM8W9GU", "08PDVH4YDX",
                      "GYKP13AC4G", "FUXD6B7BK5", "H7H3W7CMRP",
                      "14VLIMRUPT", "T1UMSVROYC", "ZI4JKD1K32",
                      "F4E4NGEE0I", "IQQR94WKBV", "F1Q1IPMA3I",
                      "3W78W6IKRV", "DLKK5L099U", "AU0ZO5S63B",
                      "VS9D5VJ1KV", "XZ06Z826XD", "P76P4IY04U",
                      "0CGL94C94R", "7TY6Q4YMAT", "SQPDZDVB2K",
                      "QCM9P9CGRG", "VTKVESTMP7", "46IUY9VOLB",
                      "TBZHRX98QE", "4LBIQUI3FZ", "R9JBVA80XV",
                      "D8U3NH681I", "Z9L6SYG2GB", "SVEO9IVHZZ",
                      "H5AN6AB82V", "RVIB7NP5TI", "HHGUVMI4SK"]

        return self.encrypt_text(char, rus_cipher)

    def encrypt(self):

        encrypted_text = []
        rus_index = 0

        space_positions = [i for i, c in enumerate(self.text) if c == " "]

        for char in self.text:

            if char in self.rus_alphabet_lower + self.rus_alphabet_upper:

                rus_index += 1

                if rus_index <= 50:

                    method = self.table_methods[rus_index]
                    encrypted_char = method(char)

                else:
                    encrypted_char = self.dynamic_table(char, rus_index)

                encrypted_text.append(encrypted_char)
            else:
                encrypted_text.append(char)

        encrypted_str = ''.join(encrypted_text)
        russian_count = self.count_rus_chars()

        encoded_length = self.encode_length(russian_count, self.digital_length_map)
        encoded_space_poss = self.encode_space_positions(space_positions)

        return f"{encoded_length}-{encrypted_str}-{encoded_space_poss}"

    def dynamic_table(self, char, rus_index):

        block = (rus_index - 51) // 50

        shift_cycle = [13, -8, 21, -34, 47, 6, -15, 28, -9]

        shift = shift_cycle[block % len(shift_cycle)]

        base_i = (rus_index - 1) % 50 + 1

        shifted_i = ((base_i - 1 + shift) % 50) + 1

        table_method = self.table_methods[shifted_i]
        return table_method(char)

cipher = Cipher()
result = cipher.encrypt()
print(result)