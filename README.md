# Verification-of-validity
验证各种规则的有效性，比如身份证、密码等

一、身份证的验证
    
    1.身份证的规则
        根据《中华人民共和国国家标准GB 11643-1999》中有关公民身份号码的规定，公民身份号码是特征组合码，由十七位数字本体码
    和一位数字校验码组成。 排列顺序从左至右依次为：六位数字地址码，八位数字出生日期码，三位数字顺序码和一位数字校验码。顺序
    码的奇数分给男性，偶数分给女性。校验码是根据前面十七位数字码，按照ISO 7064:1983.MOD 11-2校验码计算出来的检验码。
    
    2.校验位数为18位
        第1位为1-9数字
        第2位到第6位为0-9数字
        第7位到第10位为 1980年到3999 中的一年   
        第11位12位为月份(01-12)  
        第13位14位日(01-31)
        第15位到第17位位0-9数字
        最后1位为0-9数字或者X
        
    3.保存有效身份证号为18位数字或者17位数字加大写X
    
    4.根据前17位计算最后一位校验位
    
    5.根据第7-10位及11-12位计算天数
    
    6.根据第17位计算性别
    
