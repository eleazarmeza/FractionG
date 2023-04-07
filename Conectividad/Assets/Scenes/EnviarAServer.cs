using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using UnityEngine.Networking;
using UnityEngine.SceneManagement;


public class EnviarAServer : MonoBehaviour
{
    public void SendToServer()
    {
        GameObject px = GameObject.Find("PlayerX");
        PlayerData pd = px.GetComponent<PlayerData>();
        //UserData ud = px.GetComponent<UserData>();
        
        //Player p = new Player();
        //p.group = pd.group;
        //p.listNumber = pd.listNumber;
        string message = JsonUtility.ToJson(pd.player);
        //string message = JsonUtility.ToJson(ud.user);
        Debug.Log(message);
        StartCoroutine(SendPlayerData(message));
        // El server recibira, mediante POST, una version JSON del estado del jugador:
        // {'player':{'group':2,'listNumber':1,'history':[{level':1,'score':20},{'level':2,'score':5},{'level':3,'score':-1}]}}
    }

    IEnumerator SendPlayerData(string data)
    {
        WWWForm form = new WWWForm();
        form.AddField("player", data);
        //form.AddField("group",gr);
        //form.AddField("number", "one");
        //form.AddField("number", "all");

        using (UnityWebRequest www = UnityWebRequest.Post("http://192.168.8.238:8000/logout", form))
        {
            yield return www.SendWebRequest();

            if (www.result != UnityWebRequest.Result.Success)
            {
                Debug.Log(www.error);
            }
            else
            {
                //Debug.Log("Form upload complete!");
                string txt = www.downloadHandler.text;
                Debug.Log(txt);
                Application.Quit();
             
        
                
            }
        }
    }
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
