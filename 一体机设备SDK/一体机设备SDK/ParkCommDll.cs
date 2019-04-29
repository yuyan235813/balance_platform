using System;
using System.Collections.Generic;
using System.Text;
using System.Runtime.InteropServices;

namespace BLL.Card
{

    public class ParkCommOperator
    {
        [DllImport("ParkComm.dll")]
        public static extern bool OpenCom(int AComNumber);
        //function OpenCom(AComNumber: integer): Boolean;  stdcall;

        [DllImport("ParkComm.dll")]
        public static extern bool CloseCom();
        //function CloseCom(): Boolean;  stdcall;

        [DllImport("ParkComm.dll")]
        public static extern int EquCheckWithTime();
        //function EquCheckWithTime(): integer;  stdcall;

        [DllImport("ParkComm.dll")]
        public static extern int EquCheck();
        //function EquCheck(): integer;  stdcall;

        [DllImport("ParkComm.dll")]
        public static extern int IssueCard(string cardNo, string validDate, bool antiBack, int cardType, bool isUse);
        //function IssueCard(ACardNo: Pchar; AValidDate: Pchar; AAntiBack: Boolean; ACardType: integer; AIsUse: Boolean = true): integer;

        [DllImport("ParkComm.dll")]
        public static extern int SetCardGrant(string cardNo, string inGrant, string outGrant);
        //function SetCardGrant(ACardNo, AInGrant,  AOutGrant: Pchar): integer;    stdcall;

        [DllImport("ParkComm.dll")]
        public static extern int ReadUserCard(ref string cardNo, ref int cardType, ref string validDate, ref bool isUse, ref bool antiBack);
        //function ReadUserCard(var ACardNo: Pchar;  var ACardType: integer; var AValidDate: Pchar; var AIsUse,   AAntiBack: Boolean): integer;

        [DllImport("ParkComm.dll")]
        public static extern int ManagerTime(string dateTime);
        //function ManagerTime(ADateTime: Pchar): integer;

        [DllImport("ParkComm.dll")]
        public static extern int ManagerSetPos(int posId, int posType, int inOutType);
        //function ManagerSetPos(APosId, APosType, AInOutType: integer): integer;

        [DllImport("ParkComm.dll")]
        public static extern int ManagerLost(string cardNo, int lostType);
        //function ManagerLost(ACardNo: Pchar;  ALostType: integer): integer;

        [DllImport("ParkComm.dll")]
        public static extern int ReadEquDateTime(ref string dateTime);
        //function ReadEquDateTime(var AEquDateTime: pchar): integer;

        [DllImport("ParkComm.dll")]
        public static extern int MultiPsw();
        //function MultiPsw: integer;

        [DllImport("ParkComm.dll")]
        public static extern int ClearPsw();
        //function ClearPsw: integer;

        [DllImport("ParkComm.dll")]
        public static extern int MultiStop();
        //function MultiStop: integer;

        [DllImport("ParkComm.dll")]
        public static extern int GetComResult();
        //function GetComResult: integer;

        [DllImport("ParkComm.dll")]
        public static extern int EmptyComData();
        //function EmptyComData: integer;

        [DllImport("ParkComm.dll")]
        public static extern int SetPsw(string password);
        //function SetPsw(APsw: PChar): integer;

        [DllImport("ParkComm.dll")]
        public static extern int ManagerDelayCard(string cardNo, string validDate);
        //function ManagerDelayCard(ACardNo, AValidDate: string): integer;

        [DllImport("ParkComm.dll")]
        public static extern int SetTmpCard(string cardNo, string startDatetime);
        //function SetTmpCard(ACardNo, AStartDateTime: string): integer;

        [DllImport("ParkComm.dll")]
        public static extern int OpenPos(int posId, int posType, int inOutType);
        //function OpenPos(APosId: Integer; APosType: integer; AInOutType: integer): integer;
        /*
         * 
          ER_Suc: integer = 0;             //执行成功
          ER_NoReturn: integer = 2;        //无返回值
          ER_SumErr: integer = 3;          //校验和错误
          ER_TimeOut: integer = 4;         //超时
          ER_ErrData: integer = 5;         //无效数据
          ER_NoData: integer = 6;          //无返回数据
          ER_OtherData: integer = 7;       //其它数据
          ER_ErrDateTime: integer = 8;         //无效日期时间
          ER_UserStop: integer = 9;        //用户终止
          ER_EquInUse: Integer = 100;       //设备占用
          ER_EquNotAvailable: Integer = 101;  //设备找不到
          ER_EquExcept: integer = 102; //设备通讯异常
          ER_EquTypeInUse: Integer = 103;       //设备类型在使用
         
          ER_NoObject: Integer = 200;       //soyal没有创建
          ER_ComClose: Integer = 201;       //串口没打开
          ER_OhterExcept: Integer = 202;       //未知异常
         */

        public ParkCommOperator()
        {

        }

        /// <summary>
        /// 打开串口
        /// </summary>
        /// <param name="comNumber">串口号</param>
        /// <returns></returns>
        public bool DllOpenCom(int comNumber)
        {
            return OpenCom(comNumber);
        }

        /// <summary>
        /// 关闭串口
        /// </summary>
        public bool DllCloseCom()
        {
            return CloseCom();
        }

        /// <summary>
        /// 检测设备在线，并下传时间
        /// </summary>
        /// <returns></returns>
        public int DllEquCheckWithTime()
        {
            return EquCheckWithTime();
        }

        /// <summary>
        /// 检测设备在线
        /// </summary>
        /// <returns></returns>
        public int DllEquCheck()
        {
            return EquCheck();
        }

        /// <summary>
        /// 发行卡片
        /// </summary>
        /// <param name="cardNo">卡号 16进制8个字符</param>
        /// <param name="validDate">有效日期 yyyy-mm-dd</param>
        /// <param name="antiBack">是否反潜回限制</param>
        /// <param name="cardType">卡片类型 1月卡2临时卡3免费卡</param>
        /// <param name="isUse">是否授权</param>
        /// <returns></returns>
        public int DllIssueCard(string cardNo, string validDate, bool antiBack, int cardType, bool isUse=true)
        {
            return IssueCard(cardNo, validDate, antiBack, cardType, isUse);
        }

        /// <summary>
        /// 发行卡片
        /// </summary>
        /// <param name="cardNo">卡号 16进制8个字符</param>
        /// <param name="AInGrant">0000000000000000 16个0或1 0-15入口</param>
        /// <param name="AOutGrant">0000000000000000 16个0或1 16-31出口</param>
        /// <returns></returns>
        public int DllSetCardGrant(string cardNo, string AInGrant, string AOutGrant)
        {
            return SetCardGrant(cardNo, AInGrant, AOutGrant);
        }

        /// <summary>
        /// 读取用户卡
        /// </summary>
        /// <param name="cardNo">卡号 8位16进制字符</param>
        /// <param name="cardType">卡片类型 1月卡2临时卡3免费卡 </param>
        /// <param name="validDate">有效期  yyyy-mm-dd</param>
        /// <param name="isUse">是否授权  </param>
        /// <param name="antiBack">是否限制反潜回</param>
        /// <returns></returns>
        public int DllReadUserCard(ref string cardNo, ref int cardType, ref string validDate, ref bool isUse, ref bool antiBack)
        {
            try
            {
                return ReadUserCard(ref cardNo, ref cardType, ref validDate, ref isUse, ref antiBack);
            }
            catch
            {
                System.Windows.Forms.MessageBox.Show("DllReadUserCard");
                return -1;
            }
        }

        /// <summary>
        /// 管理卡校时 
        /// </summary>
        /// <param name="dateTime">校时时间 yyyy-mm-dd hh:nn:ss</param>
        /// <returns></returns>
        public int DllManagerTime(string dateTime)
        {
            return ManagerTime(dateTime);
        }

        /// <summary>
        /// 管理卡设置机号
        /// </summary>
        /// <param name="posId">机号 0~15对应入口的1~16号进，16~31对应出口的1~16号出</param>
        /// <param name="posType">大小场 1：大车场；2：小车场</param>
        /// <param name="inOutType">进出类型 1：进口  0： 出口</param>
        /// <returns></returns>
        public int DllManagerSetPos(int posId, int posType, int inOutType)
        {
            return ManagerSetPos(posId, posType, inOutType);
        }

        /// <summary>
        /// 管理卡挂失解挂
        /// </summary>
        /// <param name="cardNo">卡号</param>
        /// <param name="lostType">操作类型 0：挂失；1：解挂</param>
        /// <returns></returns>
        public int DllManagerLost(string cardNo, int lostType)
        {
            return ManagerLost(cardNo, lostType);
        }

        /// <summary>
        /// 读取设备时间
        /// </summary>
        /// <param name="dateTime">设备时间 yyyy-mm-dd hh:nn:ss</param>
        /// <returns></returns>
        public int DllReadEquDateTime(ref string dateTime)
        {
            return ReadEquDateTime(ref dateTime);
        }

        /// <summary>
        /// 开始批量加密
        /// </summary>
        /// <returns></returns>
        public int DllMultiPsw()
        {
            return MultiPsw();
        }

        /// <summary>
        /// 开始批量清除密码
        /// </summary>
        /// <returns></returns>
        public int DllClearPsw()
        {
            return ClearPsw();
        }

        /// <summary>
        /// 批量操作停止
        /// </summary>
        /// <returns></returns>
        public int DllMultiStop()
        {
            return MultiStop();
        }
        /// <summary>
        /// 批量结果读取
        /// </summary>
        /// <returns></returns>
        public int DllGetComResult()
        {
            return GetComResult();
        }
        /// <summary>
        /// 批量结果清除
        /// </summary>
        /// <returns></returns>
        public int DllEmptyComData()
        {
            return EmptyComData();
        }

        /// <summary>
        /// 下发密码到发卡器
        /// </summary>
        /// <param name="password">密码 6个字节 16进制的12个字符</param>
        /// <returns></returns>
        public int DllSetPsw(string password)
        {
            return SetPsw(password);
        }

        /// <summary>
        /// 制作无卡延期用的管理卡
        /// </summary>
        /// <param name="cardNo">要延期的卡片号码 16进制8位字符</param>
        /// <param name="validDate">延期卡片的新有效期 yyyy-mm-dd</param>
        /// <returns></returns>
        public int DllManagerDelayCard(string cardNo, string validDate)
        {
            return ManagerDelayCard(cardNo, validDate);
        }

        /// <summary>
        /// 临时卡进出场写卡，入场写入场时间、有效期、出入口权限；出场写入场时间为0，有效期为昨天，出入口权限为空
        /// </summary>
        /// <param name="cardNo">卡片号码 16进制8位字符</param>
        /// <param name="startDatetime">入场时间 yyyy-mm-dd hh:nn:ss</param>
        /// <returns></returns>
        public int DllSetTmpCard(string cardNo, string startDatetime)
        {
            return SetTmpCard(cardNo, startDatetime);
        }


        /// <summary>
        /// 临时卡发卡后，开闸命令
        /// </summary>
        /// <param name="posId">车场编号 0-31</param>
        /// <param name="posType">大小场 1：大车场；2：小车场</param>
        /// <param name="inOutType">进出类型 1：进口  0： 出口</param>
        /// <returns></returns>
        public int DllOpenPos(int posId, int posType, int inOutType)
        {
            return OpenPos(posId,posType,inOutType);
        }
    }
}
