using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using UnityEngine.Networking;
using UnityEngine.SceneManagement;

public class HacerLogin : MonoBehaviour
{
    //en los slots van estos input fields y tengo acceso al texto que guardan
    public TMP_InputField grupo;
    public TMP_InputField lista;
    public TMP_InputField id;

    //func publica para asignar al boton
    public void Ingresar()
    {
        string n = lista.text;
        string g = grupo.text;
        string i = id.text;

        //manda llamar al server con los datos ue recupero
        StartCoroutine(SendLoginData(n, g, i)); //esta funcion dendlogndata esta en webrequest (NetworkHandling)
    }

    //prepara forma web (este es el upload traido de network hadling)
    IEnumerator SendLoginData(string gr, string nl, string id)
    {
        WWWForm form = new WWWForm();
        form.AddField("group", gr);
        form.AddField("listNumber", nl);
        form.AddField("studentId", id);

        using (UnityWebRequest www = UnityWebRequest.Post("http://127.0.0.1:8000/login", form))
        {
            // Get the CSRF token from PlayerPrefs and set it in the request headers
            string csrfToken = PlayerPrefs.GetString("csrftoken");
            www.SetRequestHeader("X-CSRFToken", csrfToken);

            yield return www.SendWebRequest();

            if (www.result != UnityWebRequest.Result.Success)
            {
                Debug.Log(www.error);
            }
            else
            {
                string txt = www.downloadHandler.text;
                //Cuando es uno solo, le debo de quitar los brackets cuadrado []

                // Quitamos los brackets cuadrados:

                txt = txt.Substring(1);
                txt = txt.Substring(0, txt.Length - 2);

                Student s = JsonUtility.FromJson<Student>(txt);
                GameObject po = GameObject.Find("PlayerX");
                PlayerData pd = po.GetComponent<PlayerData>();
                pd.student.group = s.group;
                pd.student.listNumber = s.listNumber;
                pd.student.studentId = s.studentId;

                SceneManager.LoadScene("LoginOK");
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















/*

using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using UnityEngine.Networking;
using UnityEngine.SceneManagement;

public class HacerLogin : MonoBehaviour
{
    //en los slots van estos input fields y tengo acceso al texto que guardan
    public TMP_InputField grupo;
    public TMP_InputField lista;
    public TMP_InputField id;

//func publica para asignar al boton
    public void Ingresar()
    {
        string n = lista.text;
        string g = grupo.text;
        string i = id.text;

//manda llamar al server con los datos ue recupero
        StartCoroutine(SendLoginData(n, g, i)); //esta funcion dendlogndata esta en webrequest (NetworkHandling)

    }

//prepara forma web (este es el upload traido de network hadling)
 IEnumerator SendLoginData(string gr, string nl, string id)
    {
        WWWForm form = new WWWForm();
        form.AddField("group",gr);
        form.AddField("listNumber",nl);
        form.AddField("studentId", id);
        


        using (UnityWebRequest www = UnityWebRequest.Post("http://127.0.0.1:8000/login", form))
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
                //Debug.Log(txt);
                //Cuando es uno solo, le debo de quitar los brackets cuadrado []
                
                // Quitamos los brackets cuadrados:
                
                txt = txt.Substring(1);
                txt = txt.Substring(0, txt.Length - 2);

                Student s = JsonUtility.FromJson<Student>(txt);
                GameObject po = GameObject.Find("PlayerX");
                PlayerData pd = po.GetComponent<PlayerData>();
                pd.student.group = s.group;
                pd.student.listNumber = s.listNumber;
                pd.student.studentId = s.studentId;

*/

/*
                Player p = JsonUtility.FromJson<Player>(txt);
                GameObject po = GameObject.Find("PlayerX");
                PlayerData pd = po.GetComponent<PlayerData>();
                pd.player.group = p.group;
                pd.player.listNumber = p.listNumber;
*/

/*
                SceneManager.LoadScene("LoginOK");
                



                
                
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


*/