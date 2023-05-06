import { StyleSheet, Text, View, Button, Image } from 'react-native';
import { CoroaImgText } from '../components/CoroaImgText/CoroaImgText';
import { TextAndSubText } from '../components/TextAndSubText/TextAndSubText';
import {ButtonOpt} from '../components/ButtonOpt/ButtonOpt'

export function HomeScreen({ navigation }) {
  return(
    <View style={styles.container}>
      <View style={styles.header}>
        <CoroaImgText></CoroaImgText>
      </View>
      <View style={styles.containerTextMain}>
        <TextAndSubText></TextAndSubText>
      </View>
      <View style={styles.optionsButtons}>
        <ButtonOpt source={require('../assets/pills.png')} title='Agendar meus Remédios'/>
        <ButtonOpt source={require('../assets/doctor.png')} title='Cadastrar meu cuidador'/>
        <ButtonOpt source={require('../assets/file.png')} title='Abrir relatório diário'/>
        <ButtonOpt source={require('../assets/letter.png')} title='Chat com Cuidador'/>
      </View>
      <Button 
        title='Go to Details' 
        onPress={() => { 
          navigation.navigate('Details', {
            itemId: 86,
            otherParam: 'Informações extras',
          }); 
        }}
      />   
    </View>
  );
}

const styles = StyleSheet.create({
  container:{
    flex:1,
    alignItems: 'center',
    textAlign: 'center',
    backgroundColor: '#FFC9AB'
  },
  header:{
    justifyContent: 'center',
    alignItems:'center',
    
  },
  containerTextMain:{
    marginTop: '5%',
    width: '57%'
  },
})