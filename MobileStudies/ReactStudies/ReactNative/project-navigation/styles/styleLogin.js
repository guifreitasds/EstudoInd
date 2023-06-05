import { StyleSheet } from "react-native";


const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: '#FFC9AB',
      alignItems: 'center',
    },
    containerBox: {
      marginTop: '50%',
      width: 500,
      height: 130,
      backgroundColor: '#FFC9AB',
      flexDirection: 'column',
      justifyContent: 'center',
      alignItems: 'center'
    },
    containerInput: {
      marginTop: '20%',
      flexDirection: 'column',
      alignItems: 'center'
    },
    paragraph: {
      fontSize: 45,
      fontWeight: '500',
      fontFamily: 'serif',
      color: '#911746'
    },
    subparag: {
      fontSize: 11,
      fontWeight: '400',
      fontFamily: 'serif',
      color: '#911746'
    },
    imgPrin: {
      width: 150,
      height: 150
    },
    inputcpf: {
      flexDirection: 'row',
      borderRadius: 5,
      padding: 13,
      backgroundColor: '#f0f0f0',
      width: 290,
      height: 50,
      borderWidth:1,
      borderColor: '#777'
    },
    inputpassw: {
      flexDirection: 'row',
      marginTop: 20,
      borderRadius: 5,
      padding: 14,
      backgroundColor: '#f0f0f0',
      width: 290,
      height: 50,
      borderWidth:1,
      borderColor: '#777'
    },
    cpfTextInp: {
      marginLeft: 10,
      fontSize: 17,
    },
    passTextInp: {
      marginLeft: 10,
      fontSize: 17,
    },
    logButton: {
      flexDirection: 'column',
      justifyContent: 'center',
      alignItems: 'center',
      textAlign: 'center',
      borderRadius: 7,
      display: 'flex',
      marginTop: '7%',
      backgroundColor: '#741B47',
      width: '40%',
      height: 50,
  
    },
    textButton:{
      fontWeight: 'bold',
      fontSize: 18,
      color: '#fafafa',
      textAlign: 'center',
    },
  
    viewSubText: {
      // View do 'Esqueceu a senha?'
    },
    subTextForm: {
      // Text do 'Esqueceu a senha?'
      textAlign: 'right',
      alignItems: 'flex-end',
      color: '#741B47',
  
    },
  
    textRegisterinForm: {
      color: '#741B36',
    },
  });

export default styles