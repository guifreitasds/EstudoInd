import { StyleSheet, Text, View, ScrollView, TouchableOpacity } from 'react-native';
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
      <TouchableOpacity style={styles.containerTextButton}>
        <Text style={styles.textButton}>+</Text>
      </TouchableOpacity>
      <View>
        <View style={styles.titletoMedicines}>
          <Text style={{color: '#f0f0f0', fontSize: 22, fontFamily: 'serif', fontWeight: 'bold'}}>Remédios Cadastrados</Text>
        </View>
      </View>
      <MedicinesList data={data}/>
    </View>
  );
}
