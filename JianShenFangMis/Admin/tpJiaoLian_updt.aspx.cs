﻿using System;
using System.Data;
using System.Configuration;
using System.Collections;
using System.Web;
using System.Web.Security;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Web.UI.WebControls.WebParts;
using System.Web.UI.HtmlControls;
using System.Data.SqlClient;
public partial class Admin_tpJiaoLian_updt : System.Web.UI.Page
{
    public string sql, dID;

    SqlHelper data = new SqlHelper();
    protected void Page_Load(object sender, EventArgs e)
    {
        dID = Request.QueryString["id"].ToString().Trim();
        if (!IsPostBack)
        {
            DropDownList1.DataSource = data.GetDataReader("select * from JiaoLianType");
            DropDownList1.DataValueField = "id";
            DropDownList1.DataTextField = "name";
            DropDownList1.DataBind();
            sql = "select * from JiaoLian where id=" + dID;
            getdata(sql);
        }
    }
    private void getdata(string sql)
    {
        SqlDataReader dr = data.GetDataReader(sql);
        if (dr.Read())
        {
            title.Text = dr["name"].ToString();
           content1.Value = dr["content"].ToString();
           DropDownList1.Items.FindByValue(dr["typeid"].ToString()).Selected = true;
           DropDownList1.Items.FindByText(dr["TypeName"].ToString()).Selected = true; 
        }

    }
    protected void Button1_Click(object sender, EventArgs e)
    {
        sql = "update JiaoLian set name='" + title.Text.ToString().Trim() + "',content='" + content1.Value + "',typeid='" + DropDownList1.SelectedValue + "',TypeName='"+DropDownList1.SelectedItem.Text+"' where id=" + dID;
        data.RunSql(sql);
        Alert.AlertAndRedirect("修改成功", "JiaoLianList.aspx");
    }
}
