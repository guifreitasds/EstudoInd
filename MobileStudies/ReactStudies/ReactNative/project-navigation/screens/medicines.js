import { StyleSheet, Text, View } from 'react-native';
import { CoroaImgText } from '../components/CoroaImgText/CoroaImgText';

import { MedicinesList } from '../components/MedicineList/MedicinesList';

const data = [
  {key: 1, name: 'Dipirona', hour: '11:00', source: require('../assets/dipirona.jpg')},
  {key: 2, name: 'Paracetamol', hour: '14:00', source: require('../assets/paracetamol.webp')},
  {key: 3, name: 'Amoxicilina', hour: '13:00', source: require('../assets/amoxicilina.jpg')},
  {key: 4, name: 'Genérico 4', hour: '12:00', source: require('../assets/generico.jpeg')}
]
export function MedicinesScreen({route, navigation}) {

  return(
    <View style={styles.container}>
      <CoroaImgText/>
      <Text style={styles.text}>Vamos agendar os horários de todos os seus remédios?</Text>
      <Text style={styles.subText}>É para não se esquecer!</Text>
      <MedicinesList data={data}/>
    </View>
  );
}

const styles = StyleSheet.create({
  container:{
    flex:1, 
    alignItems:'center', 
    backgroundColor: '#FFC9AB'
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
  }
});