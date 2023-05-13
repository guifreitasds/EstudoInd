import { StyleSheet, Text, View, Button, Image, ScrollView, TextInput } from 'react-native';
import { CoroaImgText } from '../components/CoroaImgText/CoroaImgText';
import { TextAndSubText } from '../components/TextAndSubText/TextAndSubText';
import { ButtonOpt } from '../components/ButtonOpt/ButtonOpt'
import { HelpButton } from '../components/HelpButton/HelpButton';

export function HelpScreen({ navigation }) {
  return(
    <ScrollView style={styles.container}>
      <View style={styles.header}>
        <CoroaImgText></CoroaImgText>
      </View>
      <View style={styles.containerTextMain}>
        <Text style={styles.titleHelp}>Página de Ajuda</Text>
        <Text style={styles.titleSupport}>Como podemos lhe ajudar?</Text>
      </View>
      <View style={styles.containerInput}>
        <TextInput placeholder='Qual a sua dúvida?' style={styles.inputHelp}></TextInput>
      </View>
      <View style={styles.containerHelpButtons}>
        <HelpButton title='Fazer Login' source={require('../assets/login.png')} func={()=>navigation.navigate('Login')}/>
      </View>
      <View style={styles.containerHelpButtons}>
        <HelpButton title='Segurança' source={require('../assets/security.png')}/>
        <HelpButton title='Assinatura' source={require('../assets/coin.png')}/>
      </View>
      <View style={styles.containerHelpButtons}>
        <HelpButton title='Perguntas Frequentes' source={require('../assets/conversation.png')}/>
        <HelpButton title='Resolução Problemas' source={require('../assets/search.png')}/>
      </View>
      <View style={styles.containerHelpButtons}>
        <HelpButton title='Dados da Conta' source={require('../assets/badge.png')} func={()=>navigation.navigate('Profile')}/>
        <HelpButton title='Sobre o C.O.R.O.A' source={require('../assets/crown.png')} func={()=>navigation.navigate('About')}/>
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container:{
    flex:1,
    textAlign: 'center',
    backgroundColor: '#FFC9AB'
  },
  header:{
    justifyContent: 'center',
    alignItems:'center',
    
  },
  containerTextMain:{
    alignItems: 'center',
  },
  titleHelp:{
    fontFamily: 'serif',
    fontSize: 30,
    fontWeight: 'bold'
  },
  titleSupport: {
    fontSize:16,
    marginTop: '3%'
  },
  containerInput:{
    marginTop: '3%',
    alignItems: 'center',
  },
  inputHelp:{
    backgroundColor: '#f0f0f0',
    paddingLeft: 10,
    width: 200,
    height: 50,
    borderColor: '#000',
    borderWidth: 1,
    borderRadius: 5
  },
  containerHelpButtons: {
    display:'flex',
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',
  }
})