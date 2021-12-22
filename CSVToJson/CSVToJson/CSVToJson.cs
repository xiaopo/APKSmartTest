using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Newtonsoft.Json.Linq;
using System.IO;

namespace CSVToJson
{

    class CSVToJson
    {
        public static string CsvToJson(string filePath,string title = "神都伏魔录", string title2 ="设备名称")
        {
            JObject csvJson = new JObject();
          
            csvJson["title"] = new JObject(new JProperty("text", title),new JProperty("subtext", title2));
            csvJson["tooltip"] = new JObject(new JProperty("trigger", "axis"));

            //toolbox
            JArray toolboxs = new JArray();
            JObject toolbox = new JObject(new JProperty("show",true));
            JObject feature = new JObject();
            feature["mark"] = new JObject(new JProperty("show", true));
            feature["dataView"] = new JObject(new JProperty("show",true),new JProperty("readOnly", false));
            feature["magicType"] = new JObject(new JProperty("show", true), new JProperty("type", "[\"line\",\"bar\"]"));
            feature["restore"] = new JObject(new JProperty("show", true));
            feature["saveAsImage"] = new JObject(new JProperty("show", true));
            toolbox["feature"] = feature;

            csvJson["toolbox"] = toolbox;
            csvJson.Add(new JProperty("calculable",true));

            //滚动设置
            JArray dataZoom = new JArray();
            dataZoom.Add(new JObject(new JProperty("show", true), new JProperty("realtime", true),new JProperty("start",0),new JProperty("end",20)));
            dataZoom.Add(new JObject(new JProperty("type", "inside"), new JProperty("realtime", true), new JProperty("start", 0), new JProperty("end", 20)));


            csvJson["dataZoom"] = dataZoom;
            StreamReader reader = new StreamReader(filePath, System.Text.Encoding.UTF8, false);    //读取CSV文件
          
            List<string[]> totals = new List<string[]>();
            while (!reader.EndOfStream)
            {
                string str = reader.ReadLine();
                string[] split = str.Split(',');
                totals.Add(split);
            }
            reader.Close();

            JArray legend = new JArray();
            JArray xAxis = new JArray();
           

            List<List<string>> yAxdatas = new List<List<string>>();

            for (int i = 0;i< totals.Count;i++)
            {
                string[] split = totals[i];
                if (i % 10 != 0) continue;
                if (i == 0)
                {
                    //标题
                    for (int c = 1; c < split.Length; c++)
                    {
                        legend.Add(split[c]);

                        //y轴必须和legend对应
                        List<string> ylist = new List<string>();
                        yAxdatas.Add(ylist);
                    }
                }
                else
                {

                    //数据
   
                    JArray yAxis = new JArray();
                    for (int c = 0; c < split.Length; c++)
                    {
                       
                        if (c == 0)
                            //第一个数据为 X轴的
                            xAxis.Add(float.Parse(split[c]));
                        else
                        {
                            //其他数据为 y轴的
                            //必须和legend对应
                            List<string> ylist = yAxdatas[c - 1];
                            ylist.Add(split[c]);

                        }
                        
                        
                    }

                }
            }


            JArray yAxises = new JArray();
            for(int i = 0;i< yAxdatas.Count;i++)
            {
                JObject yaxObj = new JObject();
                yaxObj["name"] = legend[i];
                if(i == 3)
                    yaxObj["type"] = "bar";
                else
                    yaxObj["type"] = "line";

                List<string> parses = new List<string>();
                for(int j = 0;j< yAxdatas[i].Count;j++)
                {
                    float a = 0;
                    //float.TryParse(yAxdatas[i][j], out a);
                    parses.Add(yAxdatas[i][j]);
                }

                yaxObj.Add(new JProperty("data", parses));

                yAxises.Add(yaxObj);
            }

            reader.Close();   //关闭流
            //第一排显示
            csvJson["legend"]=  new JObject(new JProperty("data", legend));
            //X轴
            JObject xAxisO = new JObject(new JProperty("type", "category"), new JProperty("data", xAxis));
            xAxisO["axisLabel"] = new JObject(new JProperty("formatter", "{value} (帧)"));
            csvJson["xAxis"] = xAxisO;

            //Ｙ轴
            JObject yAxiso = new JObject(new JProperty("type", "value"));
            yAxiso["axisLabel"] = new JObject(new JProperty("formatter", "{value} (单位)"));
            csvJson["yAxis"] = yAxiso;

            csvJson["series"] = yAxises;
            string jsonStr = csvJson.ToString();
     

            string jsonPath = Path.GetDirectoryName(filePath);
            jsonPath += "/profiler.txt";
            FileStream file = new FileStream(jsonPath, FileMode.Create);
            StreamWriter wr = new StreamWriter(file);
            wr.Write(jsonStr);
            wr.Close();

            Console.WriteLine("[CSVToJson] scucess out json text: " + jsonPath);

            return jsonStr;
        }


        public static void Main(string[] args)
        {
             CsvToJson(args[0], args[1], args[2]);
        }
    }
}
