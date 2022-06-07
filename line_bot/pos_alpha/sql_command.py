class mssql_command :
    def __init__ (self) :
        print ('ส่วนการเรียกใช้งานคำสั่ง SQL ของระบบ')
    def SMB_create_view(self):
        data = """USE [SUSCOBOS]
                                   GO

                                   /****** Object:  View [dbo].[ThaiPak_AllTransactionV2]    Script Date: 4/1/2565 13:31:38 ******/
                                   SET ANSI_NULLS ON
                                   GO

                                   SET QUOTED_IDENTIFIER ON
                                   GO


                                   CREATE VIEW [dbo].[ThaiPak_AllTransactionV2_Tyche]
                                   AS
                                   WITH DATEGAP AS
                                   (
                                   --ให้เปลี่ยน ตัวเลขให้ตรงตามจำนวนวันที่ต้องการ
                                   SELECT DATEADD(day,-180,CURRENT_TIMESTAMP) STARTDATE
                                   --SELECT DATEADD(day,-10,(SELECT MAX(InsTim) FROM SUSCOBOS..Sale)) STARTDATE
                                   )
                                   , STARTNO AS
                                   (
                                   --SELECT MIN(FFIS) MAXFFIS, MIN(MGSTHID) MAXMgSthID FROM SUSCOBOS..Sale \
                                   SELECT TOP 1 FFIS MaxFFIS, MgSthid MaxMgSthId
                                   FROM SUSCOBOS..Sale WITH (NOLOCK)
                                   WHERE InsTim > (SELECT STARTDATE FROM DATEGAP)
                                   --WHERE InsTim > DATEADD(day,-30,CURRENT_TIMESTAMP)
                                   ORDER BY FFIS ASC
                                   )
                                   SELECT  
                                                 SS.InsTim AS SaleTime
                                                 , EvrQProtekt FullTxnNo
                                                 , MgE.EvrFFIS AS TxnNo
                                   , STK.StokNam
                                                 , SS.FLITRE SaleQTY
                                                 , MgSsh.SthMiktar AS Quantity
                                                 , SS.FBIRIM AS PricePerUnit
                                                 , MgSsh.SthYrlNetTut AS SaleAmount
                                                 , MGE.VatAmt VATFromDB
                                                 , MGE.TotalAmt CheckTotalAmt
                                                 , MGSKH.KasDvzTut  CheckTotalAmtMOP
                                                 , MgE.EvrIdent
                                                 , SS.FCPU AS PumpNo
                                                 , RTRIM(SS.FNOZ) AS NozzleNo
                                                 , SS.FFIS
                                                 , MgE.EvrFFIS
                                                 , SS.MgSthId
                                                 , MgE.EvrInsTim PaidDateTime
                                                 , SS.InsTim DeliveryDate
                                                 , SS.COMP POSNAME
                                                 , MOPId.BankIdent
                                                 , ISNULL(MOPId.BankPosKod, 'CASH') BankPosKod
                                                 , ISNULL(MOPId.BankPosNam, 'เงินสด') BankPosNam
                                                 ,  'หน้า ' + CONVERT(VARCHAR(6), SS.FCPU + '/' + RTRIM(SS.FNOZ) ) PumpNozNo
                                                 , CONVERT(VARCHAR(10), SS.VrdTar, 120) AS BusinessDate
                                                 , SS.VrdNo ShiftNo
                                                 , MGE.KapEvrIdent ShiftID
                                                 , BtpIdent
                                                 , BtpPtsEarned
                                                 , BtpPtsSpent
                                                 , BtpValue SpentAmount

                                   FROM sale SS
                                   --(SELECT * FROM sale WITH (NOLOCK) WHERE InsTim > DATEADD(day,(SELECT NUMBEROFDAY *-1 FROM DATEGAP),CURRENT_TIMESTAMP)) SS  
                                   ---- Main Link 1 ----
                                   JOIN (
                                          SELECT --TOP 10 
                                                 SthIdent,SthEvrIdent, SthStok, SthMiktar, SthYrlNetTut 
                                                 ,SthKdvMat, SthKdvTut
                                          FROM Mg_SilStokHareket WITH (NOLOCK)  
                                          WHERE SthInsTim >  (SELECT STARTDATE FROM DATEGAP)  
                                                                             --WHERE SthTarih >= DATEADD(day,-30,CURRENT_TIMESTAMP)
                                          UNION
                                          SELECT --TOP 10 
                                                 SthIdent,SthEvrIdent, SthStok, SthMiktar, SthYrlNetTut 
                                                 ,SthKdvMat, SthKdvTut
                                          FROM Mg_StokHareket WITH (NOLOCK)
                                          --WHERE SthInsTim >  DATEADD(day,(SELECT NUMBEROFDAY *-1 FROM DATEGAP),CURRENT_TIMESTAMP)
                                                 ) MgSSH  ON MgSSH.SthIdent=SS.MgSthId   
                                   LEFT JOIN (
                                          SELECT EvrIdent, EvrTarih, EvrFFIS, EvrKasID, KapEvrIdent, EvrNum MgeEvrNum, EvrMiktar QTY, EvrKdv VatAmt, EvrTutar TotalAmt,EvrPlaka PlateNo
                                                 ,EvrEvrIdent, EvrStatu, EvrRefTP,EvrRefNo, KapEvrIdent AS ShiftNoRunning
                                                 ,EvrTahTp, EvrInsUsr
                                                 ,EvrPumpNo, EvrinsTim, EvrModtim, EvrCompName, EvrQProtekt, EvrKhdIdent
                                          FROM Mg_SilEvrak WITH (NOLOCK) WHERE (EvrFFIS IS NOT NULL) AND (EvrStatu = 'A')
                                          AND EvrTarih >= (SELECT STARTDATE FROM DATEGAP) 
                                          --AND EvrTarih >= DATEADD(day,-30,CONVERT(DATE,CURRENT_TIMESTAMP))
                                          UNION
                                          SELECT EvrIdent, EvrTarih, EvrFFIS, EvrKasID, EvrOztEvrId, EvrNum MgeEvrNum, EvrMiktar QTY, EvrKdv VatAmt, EvrTutar TotalAmt,EvrPlaka PlateNo
                                                 ,EvrEvrIdent, EvrStatu, EvrRefTP,EvrRefNo,EvrOztEvrId AS ShiftNoRunning
                                                 ,EvrTahTp, EvrInsUsr
                                                 ,EvrPumpNo, EvrinsTim, EvrModtim, EvrCompName, EvrQProtekt, EvrKhdIdent
                                          FROM Mg_Evrak WITH (NOLOCK)  WHERE (EvrFFIS IS NOT NULL) AND (EvrStatu = 'A')

                                   ) MGE ON MGE.EvrIdent=MgSSH.SthEvrIdent  -- ถูกแน่นอน
                                   LEFT JOIN ( SELECT * FROM Mg_EvrComment WITH (NOLOCK) 
                                                               ) R_comment ON MGE.EvrIdent=R_comment.EcoEvrIdent
                                   LEFT JOIN ( SELECT * FROM Evrak WITH (NOLOCK) WHERE EvrStatu='A' 
                                                                             AND EvrTarih >=(SELECT CONVERT(DATE,STARTDATE) FROM DATEGAP) 
                                                                             --AND EvrTarih >= DATEADD(day,-30,CURRENT_TIMESTAMP)
                                                               ) EVR ON EVR.EvrIdent=Mge.KapEvrIdent
                                   LEFT JOIN (
                                          SELECT KasEvrIdent,KasIdent, KasPosId, KasDvzTut, KasDvzPaid,KasLogId CreditCardTxnId 
                                                 FROM MG_KasaHareket WITH (NOLOCK) 
                                          UNION
                                          SELECT KasEvrIdent,KasIdent, KasPosId, KasDvzTut, KasDvzPaid,KasLogId CreditCardTxnId
                                                                                                  FROM Mg_SilKasaHareket WITH (NOLOCK) 
                                                                                                  WHERE KasInsTim >= (SELECT STARTDATE FROM DATEGAP)
                                                                                                  --WHERE KasInsTim >= DATEADD(day,-30,CURRENT_TIMESTAMP)

                                          ) MGSKH ON MGSKH.KasEvrIdent=MgE.EvrIdent 
                                   ---- END OF Main Link 1 ----
                                   ---- Link TO MASTER TABLE  ----
                                   LEFT JOIN Stoklar STK WITH (NOLOCK) ON STK.StokIdent=MgSSH.SthStok
                                   LEFT JOIN Bnz_Tabancalar BTBCL WITH (NOLOCK) ON BTBCL.GunKod=(FNOZ*100+ FCPU)
                                   LEFT JOIN Bnz_Tanklar TANK WITH (NOLOCK) ON TANK.TnkIdent=BTBCL.GunTnkId
                                   LEFT JOIN dbo.Mg_Kasiyer AS att WITH (NOLOCK) ON SS.FATTENDANT = att.KasTag 
                                   Left JOIN dbo.Mg_Kasiyer AS chs WITH (NOLOCK) ON MGE.EvrKasId = chs.KasIdent 

                                   -- TUNE PERFORMANCE
                                   LEFT JOIN Evrak              CADetail WITH (NOLOCK) ON CADetail.EvrIdent = Mge.EvrEvrIdent
                                   LEFT JOIN Cariler            Customer WITH (NOLOCK) ON Customer.CariKod = CADetail.EvrCariKod 
                                                               AND Customer.CariIdent=CADetail.EvrCari
                                   LEFT JOIN Mg_CreditResultLog EdcLog   WITH (NOLOCK) ON EdcLog.LogIdent = CreditCardTxnId
                                   LEFT JOIN Mg_BankPos MOPId WITH (NOLOCK) ON MOPid.BankIdent=MGSKH.KasPosId
                                   ---- Add Link Tyche Loyalty
                                   LEFT JOIN Bnz_TychePoints Tyche WITH (NOLOCK) ON Tyche.BtpEvrIdent=MGE.EvrIdent AND BtpStatu!='X'
                                   ---- End of Tyche Loyalty

                                   GO
                                   """
        return data
    def SMB_get_report_data(self):
           data = """DECLARE @BUSINESSDATE DATE =%s
                                   DECLARE @SHIFTNO INT = %s

                                          SELECT A.BusinessDate, A.ShiftNo, A.StokNam, SUM(CountTransaction) CountTransaction 
                                , sum(SumQTY) SumQTY, sum(SumSaleAmount) SumSaleAmount
                                , COUNT(BtpPtsEarned) CountTycheTransaction
                                     , sum(ISNULL(A.Quantity,0)) SumTycheQTY
                                     , sum(ISNULL(A.SaleAmount,0)) SumTycheQTY
                                , sum(ISNULL(BtpPtsEarned,0)) TotalPointEarned
                                , sum(ISNULL(BtpPtsSpent,0)) TotalPointSpent
                                , sum(ISNULL(SpentAmount,0)) TotalSpentAmount

FROM [ThaiPak_AllTransactionV2_Tyche] A
JOIN 
(
                SELECT BusinessDate, ShiftNo, StokNam, COUNT(*) CountTransaction 
                                , sum(ISNULL(quantity,0)) SumQTY, sum(ISNULL(SaleAmount,0)) SumSaleAmount
                FROM [ThaiPak_AllTransactionV2_Tyche] 
                group by BusinessDate, ShiftNo, StokNam

) TXN ON TXN.BusinessDate=A.BusinessDate AND TXN.ShiftNo=A.ShiftNo AND TXN.StokNam=A.StokNam
                                   WHERE A.BusinessDate IN (@BUSINESSDATE)   
                                   AND A.ShiftNo IN (@SHIFTNO)

                                   group by A.BusinessDate, A.ShiftNo, A.StokNam
                                   ORDER BY A.BusinessDate, A.ShiftNo, A.StokNam
                                   """
           return data
    def SMB_get_report_data_per_EOD(self):
           data = """DECLARE @BUSINESSDATE DATE =%s
                                   

                                          SELECT A.BusinessDate, A.ShiftNo, A.StokNam, SUM(CountTransaction) CountTransaction 
                                , sum(SumQTY) SumQTY, sum(SumSaleAmount) SumSaleAmount
                                , COUNT(BtpPtsEarned) CountTycheTransaction
                                     , sum(ISNULL(A.Quantity,0)) SumTycheQTY
                                     , sum(ISNULL(A.SaleAmount,0)) SumTycheQTY
                                , sum(ISNULL(BtpPtsEarned,0)) TotalPointEarned
                                , sum(ISNULL(BtpPtsSpent,0)) TotalPointSpent
                                , sum(ISNULL(SpentAmount,0)) TotalSpentAmount

FROM [ThaiPak_AllTransactionV2_Tyche] A
JOIN 
(
                SELECT BusinessDate, ShiftNo, StokNam, COUNT(*) CountTransaction 
                                , sum(ISNULL(quantity,0)) SumQTY, sum(ISNULL(SaleAmount,0)) SumSaleAmount
                FROM [ThaiPak_AllTransactionV2_Tyche] 
                group by BusinessDate, ShiftNo, StokNam

) TXN ON TXN.BusinessDate=A.BusinessDate AND TXN.ShiftNo=A.ShiftNo AND TXN.StokNam=A.StokNam
                                   WHERE A.BusinessDate IN (@BUSINESSDATE)   
                                   

                                   group by A.BusinessDate, A.ShiftNo, A.StokNam
                                   ORDER BY A.BusinessDate, A.ShiftNo, A.StokNam
                                   """
           return data
    def current_price(self):

           data = """USE SUSCOBOS
                            select FpdEvrIdent DocNo, FpeRefNo,  StokKod,StokNam,FuelPrices.FuelPrice CurrentPrice
                                   , FpdIniPrice PreviousPrice, FpdFinPrice PriceInDoc,FpeInsTim DocumentCreatedDate
                                   , Bnz_FuelPriceEvr.FpeExpTim ActivateDateTime
                                   , CASE 
                                                 WHEN FpeActTim is null and FpeImmediate=0 THEN 'ปรับราคาเมื่อปิดกะ'
                                                 WHEN FpeActTim is not null and FpeImmediate=0 THEN 'ตั้งเวลาปรับราคา'
                                                 WHEN FpeImmediate=1 THEN 'ทันที'
                                          END PriceChange
                                   , FpeActTim TimeToUpdate
                                   , FpeExp Active

                                   --,*
                            from Bnz_FuelPriceDet
                            JOIN Bnz_FuelPriceEvr ON FpeIdent=FpdEvrIdent
                            --JOIN Mg_MgzPriceEvr ON Mg_MgzPriceEvr.PrcIdent = FpdEvrIdent
                            LEFT JOIN Stoklar ON StokIdent = FpdStok
                            LEFT JOIN FuelPrices on FuelType= FpdStok
                            WHERE FpdEvrIdent IN (
                                          select top 1 FpeIdent from Bnz_FuelPriceEvr 
                                          where  (FpeExp IS NULL OR FpeExp NOT IN ('X')) order by 1 desc
                                          )"""
           return data       

    def get_x_report_per_id (self) :
        data = """EXEC Mg_PH_XZReport_THAI %s,'Z',1"""
        return data
    def get_meter_report_per_EOD(self): # ค้นหารายการปิดกะ ตามวันที่ต้องการ
        data = """DECLARE @BusinessDate date =%s
                                        select * from Evrak where EvrTarih in (@BusinessDate) and EvrStatu='A' and EvrNum NOT LIKE '%z%' order by EvrIdent desc"""
        return data
    def get_x_report_close_shift_per_EOD(self):
        data = """USE SUSCOBOS
                            DECLARE @BusinessDate date = %s
                            DECLARE @LastShiftId int = (select TOP 1  EvrIdent
                                                    from Evrak
                                                    where EvrTarih <= DATEADD(DAY,-1,@BusinessDate) and EvrStatu = 'A'
                                                    ORDER BY EvrNum DESC
                                                    )

                            DECLARE @StartBusinessDateTime datetime = (select Min( EvrInsTim) StartBusinessDateFrom 
                                                                        from Evrak
                                                                        where EvrTarih in (@BusinessDate) and EvrStatu = 'A'
                                                                        or EvrIdent in (@LASTSHIFTID)
                                                                        )
                            DECLARE @EndBusinessDateTime datetime = (select Max( EvrInsTim) StartBusinessDateFrom 
                                                                        from Evrak
                                                                        where EvrTarih in (@BusinessDate) and EvrStatu = 'A'
                                                                        or EvrIdent in (@LASTSHIFTID)
                                                                        )

                            --select EvrTarih, EvrIdent, EvrNum, EvrInsTim
                            ----,* 
                            --from Evrak
                            --where EvrTarih in (@BusinessDate) and EvrStatu = 'A'
                            --or EvrIdent in (@LASTSHIFTID)

                            select top 10 * 
                            from Mg_KsyHesDet 
                            where KhdBasTime between @StartBusinessDateTime and @EndBusinessDateTime
                            order by 1 ,KhdModTim desc"""
        return data
    def get_thai_key (self):
        data = """SELECT A.BusinessDate, A.ShiftNo, A.StokNam, SUM(CountTransaction) CountTransaction 
                                , sum(quantity) SumQTY, sum(SaleAmount) SumSaleAmount
                                , COUNT(BtpPtsEarned) CountTycheTransaction
                                , sum(BtpPtsEarned) TotalPointEarned
                                , sum(BtpPtsSpent) TotalPointSpent
                                , sum(SpentAmount) TotalSpentAmount
                                --, Sum(
FROM [ThaiPak_AllTransactionV2_Tyche] A
JOIN 
(
                SELECT BusinessDate, ShiftNo, StokNam, COUNT(*) CountTransaction 
                FROM [ThaiPak_AllTransactionV2_Tyche] 
                group by BusinessDate, ShiftNo, StokNam

) TXN ON TXN.BusinessDate=A.BusinessDate AND TXN.ShiftNo=A.ShiftNo AND TXN.StokNam=A.StokNam

WHERE A.ShiftId IN (
                                                                                                SELECT EvrIdent 
                                                                                                FROM EVRAK 
                                                                                                WHERE EVRTIP IN (91,98) and EvrIdent>324154
                                                                                ) AND A.BtpIdent IS NOT NULL
group by A.BusinessDate, A.ShiftNo, A.StokNam
ORDER BY A.BusinessDate, A.ShiftNo, A.StokNam"""
        return data
    def get_meter_by_transection_id (self):
        data = """DECLARE @TODAY DATE = %s
declare @EvrnumFilter VARCHAR(12) =  %s

SELECT        ISNULL(CONVERT(VARCHAR(10),MBusinessdate, 103),
                        CONVERT(VARCHAR(10),@TODAY, 103) )      Businessdate, 
			  Evrnum,
              ShiftNo, 
              --GunCode, 
              PumpNo, NozNo, TankNo,     
                                                
              ISNULL(
                     (SELECT TOP 1 ProductLineNoInWeb FROM TP_ProductMappingInWebSusco T1 
                           WHERE CONVERT(INT,T1.PumpNo) = CONVERT(INT,ForMeter.PumpNo) and CONVERT(INT,T1.NozzleNo) = CONVERT(INT,NozNo)
                           ORDER BY PumpNo, NozzleNo) 
                     ,ROW_NUMBER () OVER (PARTITION BY ProductCode,ShiftNo ORDER BY PumpNo, NozNo) )
              hose_no,
              ProductAltID ProductId,RTRIM(ProductName) Product,
              ISNULL(PreviousTotalizerVol,0) Stat_Volume, ISNULL(TbdTotal,0) End_Volume,
              '' Start_Amount, '' End_Amount, 
              FORMAT(
              ISNULL((SELECT SUM(SALE.FLITRE) TESTVOLUME 
                      FROM SALE 
                      LEFT JOIN Mg_SilEvrak MgSE on MgSE.EvrFFIS = SALE.FFIS
                      WHERE SALE.VrdTar = @TODAY AND MgSE.EvrRefNo = '*METROL' AND SALE.TXNTYPE = 'A'
                               AND SALE.VRDNO = ShiftNo and SALE.FCPU = PUMPNO AND SALE.FNOZ = NozNo
                GROUP BY SALE.VRDNO ,SALE.FCPU , SALE.FNOZ),0)
              ,'0.000000')
              Test_Volume, -- 'Check from *Metro'

              --ISNULL(CashierId,'') UserName, 
              coNVERT(VARCHAR(10),rtrim(ISNULL(All_CashierInShift,''))) AllUserName,
              CONVERT(VARCHAR(10),CloseShiftOn, 103) CloseShiftDate,
              CONVERT(VARCHAR(5),CloseShiftOn, 108) CloseShiftTime,
              --AVGPRICE,
              CONVERT(VARCHAR(11),ROUND(
                     ISNULL(AVGPrice,
                           (SELECT FpdFinPrice FROM Bnz_FuelPriceDet 
                            WHERE FpdEvrIdent = 
                                  (select TOP 1 FpeIdent from BNZ_FUELPRICEEVR WHERE FpeExpTim <= CloseShiftOn AND FpeExp = '*' ORDER BY FpeExptim Desc)
                                  AND FpdStok = ForLinkLastPrice)
              ),2)) Price

FROM
(
Select Meters.TbdEvrIdent MEvrIdent
              , Meters.TbdGunId GunId                                       
           ,(SELECT Top 1 TbdEvrIdent from Bnz_TabancaDetay PT1 where PT1.TbdEvrIdent < Meters.TbdEvrIdent and PT1.TbdGunId = Meters.TbdGunId Order by PT1.TbdEvrIdent desc)  PreviousEvrIdent                                
           ,(SELECT Top 1 TbdTotal from Bnz_TabancaDetay PT1 where PT1.TbdEvrIdent < Meters.TbdEvrIdent and PT1.TbdGunId = Meters.TbdGunId Order by PT1.TbdEvrIdent desc)  PreviousTotalizerVol                            
              , Meters.TbdTotal          
              , BVrd.VrdTarih MBusinessdate            
              , CONVERT(VARCHAR(8),BVrd.VrdTarih,112) + '_' + CAST(BVrd.VrdNo AS CHAR) MFullShiftNo
              ,(SELECT Top 1 MotUpdTime FROM Mg_MusPuanEvr WHERE MotEvrNo = CONVERT(VARCHAR(8),BVrd.VrdTarih,112) + '_' + CAST(BVrd.VrdNo AS CHAR)) MCloseShiftOn
              , Onshift.MotTarih Businessdate
              , Onshift.MotEvrNo FullShiftNo
              , OnShift.MotUpdTime CloseShiftOn
			  , BVrd.VrdNo ShiftNo
			  , Evrak.EvrNum				
              , Evrak.EvrIdent RefEvrIdent2                          
              , (SELECT TOP 1 EvrInsUsr 
                from (SELECT KapEvrIdent,EvrInsUsr FROM Mg_SilEvrak MgSE 
                      WHERE MgSE.KapEvrIdent in(select Evrident from Evrak where EvrStatu='A' and evrtarih = @today) 
                           group by MgSe.KapEvrIdent, Mgse.EvrInsUsr) FCashier
                WHERE FCashier.KapEvrIdent = Evrak.EvrIdent) 
               CashierID
              , (SELECT  RTRIM(CashierInShift) AllCashierInShift
                From (
                           SELECT KapEvrIdent
                           , (ISNULL([2001]+ ' ','')+ISNULL([2002] + ' ','')+ISNULL([2003]+ ' ','')+ISNULL([2004]+ ' ','')
                           +ISNULL([2005]+ ' ','')+ISNULL([2006]+ ' ','')+ISNULL([2007]+ ' ','')+ISNULL([2008]+ ' ','')
                           +ISNULL([2009]+ ' ','')+ISNULL([3001]+ ' ','')+ISNULL([3002]+ ' ','')+ISNULL([3003]+ ' ','')) CashierInShift
                           FROM(
                                  SELECT *
                                  FROM ( SELECT KapEvrIdent,EvrInsUsr FROM Mg_SilEvrak MgSE 
                                  WHERE MgSE.KapEvrIdent in(select Evrident from Evrak where EvrStatu='A' and evrtarih = @today) 
                                  group by MgSe.KapEvrIdent, Mgse.EvrInsUsr) tFCashier  
                           PIVOT ( MAX(EvrInsUsr) FOR EvrInsUsr IN ([2001],[2002],[2003],[2004],[2005],[2006],[2007],[2008],[2009],[3001],[3002],[3003])
                                    )    PVT    
                                  ) CashierInShift
                           ) CashierInShiftText
                WHERE CashierInShiftText.KapEvrIdent  = Evrak.EvrIdent) All_CashierInShift
                           
              , BVrd.VrdMinFFIS MinFFIS
              , Bvrd.VrdMaxFFIS MaxFFis                       
              , GunRef.GunKod GunCode
              --, GunRef.GunPmpId PumpNo
              , CONVERT(INT,RIGHT(STR(GunRef.GunKod,3),2)) PumpNo
              , LEFT(CONVERT(VARCHAR(3),GunRef.GunKod),1) NozNo
              , GunRef.GunTnkId TankNo
              , GunRef.GunStkId ProductId 
              , Stoklar.StokIdent ForLinkLastPrice
              , Stoklar.StokOz1Kod ProductAltID               
              , Stoklar.StokKod ProductCode
              , Stoklar.StokNam ProductName                          
              , PPVAVG.AVGPrice                        
from Bnz_TabancaDetay Meters                                         
LEFT JOIN Bnz_Vardiya BVrd                                    
       ON BVrd.EvrIdent = Meters.TbdEvrIdent                                
LEFT JOIN Evrak                                        
       ON Evrak.EvrNum = CONVERT(VARCHAR(8),BVrd.VrdTarih,112) + '_' + CAST(BVrd.VrdNo AS CHAR)                                 
LEFT JOIN Mg_MusPuanEvr OnShift                                      
       --ON Onshift.MotIdent = Meters.TbdEvrIdent      
       ON OnShift.MotEvrNo=CONVERT(VARCHAR(8),BVrd.VrdTarih,112) + '_' + CAST(BVrd.VrdNo AS CHAR)   
LEFT JOIN Bnz_Tabancalar GunRef                                      
       ON GunRef.GunIdent = Meters.TbdGunId                                 
LEFT JOIN Stoklar                                      
       ON Stoklar.StokIdent = Gunref.GunStkId                               
LEFT JOIN (select iPPVAVG.VRDTAR, iPPVAVG.VrdNo, iPPVAVG.Gunid, iPPVAVG.FCPU AS PumpNo, iPPVAVG.FNOZ AS NozNo, AVg(iPPVAVG.FBIRIM) AVGPrice                                      
                     FROM (               
                                  Select RTRIM(FNOZ) + FCPU GunId,* 
                                  from Sale     
                                  where TXNTYPE = 'A'        
                                           AND VrdTar = @TODAY
                           ) iPPVAVG           
                     group by  iPPVAVG.VRDTAR, iPPVAVG.VrdNo,iPPVAVG.Gunid, iPPVAVG.FCPU, iPPVAVG.FNOZ               
                 ) PPVAVG                       
ON PPVAVG.GunId = gUNREF.GunKod AND PPVAVG.VrdTar = bVRD.VrdTarih AND PPVAVG.VrdNo = BVrd.VrdNo                                      
where Meters.TbdEvrIdent                                      
              in (SELECT EvrIdent  from Bnz_Vardiya where VrdTarih = @Today ) 
	AND EvrNum LIKE '%' + @EvrnumFilter +'%'
) ForMeter           

order by Businessdate, ShiftNo, PumpNo, NozNo                                     
"""
        return data
    def get_thai_key_per_request(self):
        data = """SELECT A.BusinessDate, A.ShiftNo, A.StokNam, SUM(CountTransaction) CountTransaction 
                                , sum(SumQTY) SumQTY, sum(SumSaleAmount) SumSaleAmount
                                , COUNT(BtpPtsEarned) CountTycheTransaction
                                , sum(ISNULL(A.Quantity,0)) SumTycheQTY
                                , sum(ISNULL(A.SaleAmount,0)) SumTycheSaleAmount
                                , sum(ISNULL(BtpPtsEarned,0)) TotalPointEarned
                                , sum(ISNULL(BtpPtsSpent,0)) TotalPointSpent
                                , sum(ISNULL(SpentAmount,0)) TotalSpentAmount

FROM [ThaiPak_AllTransactionV2_Tyche] A
JOIN 
(
                SELECT BusinessDate, ShiftNo, StokNam, COUNT(*) CountTransaction 
                                , sum(ISNULL(quantity,0)) SumQTY, sum(ISNULL(SaleAmount,0)) SumSaleAmount
                FROM [ThaiPak_AllTransactionV2_Tyche] 
                group by BusinessDate, ShiftNo, StokNam

) TXN ON TXN.BusinessDate=A.BusinessDate AND TXN.ShiftNo=A.ShiftNo AND TXN.StokNam=A.StokNam

WHERE A.BusinessDate IN (%s)
AND A.ShiftNo IN (%s)

group by A.BusinessDate, A.ShiftNo, A.StokNam
ORDER BY A.BusinessDate, A.ShiftNo, A.StokNam
"""
        return data