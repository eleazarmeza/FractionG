using System;
using UnityEngine;
using System.Collections.Generic;


[Serializable]
public class User 
{
    // Start is called before the first frame update
   public string username;
   public string theme;
   public string image;
   

}


[System.Serializable]
//contenedor para un arreglo de
public class ManyUsers
{
    public List<User> users;

}

/*

[System.Serializable]
//contenedor para un arreglo de
public class History
{
    public List<History> history;

}
*/

[System.Serializable]
public class Player
{
    public int group;
    public int listNumber;
    public List<Level> history;
}


[System.Serializable]
public class Level
{
    public string level;
    public int score;

}


[System.Serializable]
public class Student
{
    public int group;
    public int listNumber;
    public int studentId;
}