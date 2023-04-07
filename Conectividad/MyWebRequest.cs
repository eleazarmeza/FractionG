using UnityEngine;
using UnityEngine.Networking;
using System.Collections;

public class MyWebRequest : MonoBehaviour
{
    [System.Serializable]
    private class UserData
    {
        public int Grupo;
        public int Numero_de_Lista;
        public string Password;
    }

    void Start()
    {
        StartCoroutine(SendJson());
    }

    IEnumerator SendJson()
    {
        // Define los datos a enviar como objeto
        UserData data = new UserData();
        data.Grupo = 5;
        data.Numero_de_Lista = 18;
        data.Password = "Hola123456";

        // Convierte el objeto a una cadena JSON
        string json = JsonUtility.ToJson(data);

        // Crea un objeto UnityWebRequest con el método HTTP POST
        UnityWebRequest www = UnityWebRequest.Post("http://20.214.106.153/api/CrearUsuario/", "POST");

        // Define la cabecera Content-Type para indicar que se envía JSON
        www.SetRequestHeader("Content-Type", "application/json");

        // Convierte la cadena JSON a bytes y define el cuerpo de la solicitud
        byte[] jsonBytes = System.Text.Encoding.UTF8.GetBytes(json);
        www.uploadHandler = (UploadHandler)new UploadHandlerRaw(jsonBytes);

        // Define el manejador de descarga para recibir la respuesta del servidor
        www.downloadHandler = (DownloadHandler)new DownloadHandlerBuffer();

        // Envía la solicitud y espera la respuesta
        yield return www.SendWebRequest();

        // Verifica si hubo un error y procesa la respuesta
        if (www.result != UnityWebRequest.Result.Success)
        {
            Debug.Log(www.error);
        }
        else
        {
            string txt = www.downloadHandler.text;
            Debug.Log(txt);
        }
    }
}
