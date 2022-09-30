<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format">
    <xsl:output method="text" omit-xml-declaration="yes" indent="no"/>
    <xsl:template match="/">
        <xsl:text>CITY1,CITY2,STREET,POLICY_ID,CORR_TYPE,CORR_KEY,BUSINESS_PARTNER,CD_VTREF,CD_INSURED_PRSN,CD_FAEDN,CD_DEDUCTN_DATE,CD_CURRENCY,CD_DEDUCTN_AMOUNT,CD_BANK_NAME,CD_CARDTYPE,CD_AC_CARD_NUMBER,CD_CARD_MM_YY,CD_PYMNT_YEAR,CD_PYMNT_COUNT,CD_PAYMENT_MODE&#xa;</xsl:text>
        <xsl:for-each select="//T_POLICY/_-NSL_-CD_INVOICE_POLICY_S/T_POLY_PREM/_-NSL_-CD_INVOICE_POLY_PREM_S/WA_POLY_PREM">
            <xsl:value-of select=
            "concat(
            ../../../../../WA_REC_ADRESS/CITY1,',',
            ../../../../../WA_REC_ADRESS/CITY2,',',
            ../../../../../WA_REC_ADRESS/STREET,',',
            ../../../../../WA_CORR_HEAD/SEARCH_TAGS/POLICY_ID,',',
            ../../../../../WA_CORR_KEY/CORR_TYPE,',',
            ../../../../../WA_CORR_KEY/CORR_KEY,',',
            ../../../../../WA_CORR_KEY/BUSINESS_PARTNER,',',
            CD_VTREF,',' ,
            CD_INSURED_PRSN,',' ,
            CD_FAEDN,',' ,
            CD_DEDUCTN_DATE,',' ,
            CD_CURRENCY,',' ,
            CD_DEDUCTN_AMOUNT,',' ,
            CD_BANK_NAME,',' ,
            CD_CARDTYPE,',' ,
            CD_AC_CARD_NUMBER,',' ,
            CD_CARD_MM_YY,',' ,
            CD_PYMNT_YEAR,',' ,
            CD_PYMNT_COUNT,',' ,
            CD_PAYMENT_MODE, '&#xa;')"/>
        </xsl:for-each>
    </xsl:template>
</xsl:stylesheet>

