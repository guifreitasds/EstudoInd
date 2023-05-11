import { StyleSheet, Text, View, ScrollView } from 'react-native';
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
      <View style={styles.alignItemsCenter}> 
        <CoroaImgText/>
      </View>   
      <View style={styles.alignItemsCenter}>
        <Text style={styles.text}>Vamos agendar os horários de todos os seus remédios?</Text>
      </View>     
      <View style={styles.alignItemsCenter}>
        <Text style={styles.subText}>É para não se esquecer!</Text>
      </View>
      <View style={styles.containerTextButton}>
        <Text style={styles.textButton}>+</Text>
      </View>
      <View>
        <View style={styles.titletoMedicines}>
          <Text style={{color: '#f0f0f0', fontSize: 22, fontFamily: 'serif', fontWeight: 'bold'}}>Remédios Cadastrados</Text>
        </View>
      </View>
      <MedicinesList data={data}/>
    </View>
  );
}

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
    padding: '3%',
    margin: 25,
    width: '20%',
    height: '7%',
    borderRadius: 20,
    justifyContent: 'center'
  },
  textButton: {
    color: '#741B47',
    fontSize: 20
  },
  titletoMedicines:{
    alignItems: 'center',
    backgroundColor: '#741B47',
    padding: 20,
    width: '89.9%',
    marginLeft: 20,
    borderTopStartRadius:5,
    borderTopEndRadius: 5
  },
});