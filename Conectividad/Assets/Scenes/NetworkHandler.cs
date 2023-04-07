using UnityEngine;
using UnityEngine.Networking;
using System.Collections;

public class WebRequest : MonoBehaviour
{
    void Start()
    {
        StartCoroutine(Upload());
    }

    IEnumerator Upload()
    {
        WWWForm form = new WWWForm();
        //form.AddField("listNumber","2");
        //form.AddField("group","1");
        //form.AddField("number", "one");
        form.AddField("number", "all");

        using (UnityWebRequest www = UnityWebRequest.Post("http://192.168.8.238:8000/json", form))
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
                
                //Cuando es uno solo, le debo de quitar los brackets cuadrado []
                /*

                // Quitamos los brackets cuadrados:
                txt = txt.Substring(1);
                txt = txt.Substring(0, txt.Length - 2);
                Debug.Log(txt);
                //cuando se hace clase serializable, puedo transformar y extraer del texto Json al usuario
                // Transformar el texto limpio a objeto
                User u = JsonUtility.FromJson<User>(txt);
                Debug.Log(u.username);
                Debug.Log(u.theme);
                Debug.Log(u.image);
                */

                // para muchos usuarios:
                string txt2 = "{\"users\":" + txt + "}";
                Debug.Log(txt2);
                ManyUsers mu = JsonUtility.FromJson<ManyUsers>(txt2);
                foreach(User u in mu.users)
                {
                    Debug.Log(u.username);
                    //Debug.Log(u.theme);
                    //Debug.Log(u.image);
                }
                
            }
        }
    }
}