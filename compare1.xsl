<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="text" encoding="utf-8"/>
<xsl:template match="/">
          <xsl:text>CITY1,CITY2,STREET,POLICY_ID,CORR_TYPE,CORR_KEY,BUSINESS_PARTNER&#xa;</xsl:text>

<xsl:for-each select="//PWB_DATA">


<xsl:value-of select="WA_REC_ADRESS/CITY1"/><xsl:text>,</xsl:text>
<xsl:value-of select="WA_REC_ADRESS/CITY2"/><xsl:text>,</xsl:text>
<xsl:value-of select="WA_REC_ADRESS/STREET"/><xsl:text>,</xsl:text>
<xsl:value-of select="WA_CORR_HEAD/SEARCH_TAGS/POLICY_ID"/><xsl:text>,</xsl:text>
<xsl:value-of select="WA_CORR_KEY/CORR_TYPE"/><xsl:text>,</xsl:text>
<xsl:value-of select="WA_CORR_KEY/CORR_KEY"/><xsl:text>,</xsl:text>
<xsl:value-of select="WA_CORR_KEY/BUSINESS_PARTNER"/>



<xsl:text>
</xsl:text>




</xsl:for-each>
</xsl:template>
</xsl:stylesheet>