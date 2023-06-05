import { StyleSheet } from "react-native";


const styles = StyleSheet.create({
    container:{
      flex:1, 
      backgroundColor: '#FFC9AB'
    },
    alignItemsCenter:{
      alignItems: 'center'
    },
    text: {
      marginTop: '5%',
      fontSize: 24,
      textAlign: 'center',
      width: '70%',
      fontFamily: 'serif',
      fontWeight: '700'
    },
    subText: {
      fontSize: 18,
      fontFamily: 'serif',
      marginTop: '3%'
    },
    containerTextButton: {
      backgroundColor: '#f0f0f0',
      margin: 25,
      width: '20%',
      height: '7%',
      borderRadius: 20,
      justifyContent: 'center',
      paddingLeft: '3%'
    },
    textButton: {
      color: '#741B47',
      fontSize: 23,
    },
    titletoMedicines:{
      alignItems: 'center',
      backgroundColor: '#521332',
      padding: 20,
      width: '89.9%',
      marginLeft: 20,
      borderTopStartRadius:5,
      borderTopEndRadius: 5,
    },
  });

export default styles;