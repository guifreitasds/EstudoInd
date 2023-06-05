import * as React from 'react';
import { Text, View, StyleSheet,Image, TextInput, Touchable, TouchableOpacity } from 'react-native';
import {FontAwesome} from '@expo/vector-icons';
import Constants from 'expo-constants';
import styles from '../styles/styleLogin';



export function LoginScreen() {
  const [textoLoginInput, mudaTextoLogin] = React.useState('')
  const [mostrarTexto, setMostrarTexto] = React.useState(false);

  const handleLoginPress = () => {
    setMostrarTexto(true);
  }

  const [textoInput, mudaTexto] = React.useState('')

  return (
    <View style={styles.container}>
      <View style={styles.containerBox}>
        <Image style={styles.imgPrin} source={require('../assets/COROA-nofill.png')} />
        <Text style={styles.paragraph}>
          C.O.R.O.A
        </Text>
        <Text style={styles.subparag}>O aplicativo que cuida de você!</Text>
      </View>
      <View style={styles.containerInput}>
        <View style={styles.inputcpf}>
          <FontAwesome name='user' size={20} color="#505050"></FontAwesome>
          <TextInput style={styles.cpfTextInp} placeholder='Digite seu CPF' onChangeText={mudaTexto}></TextInput>
        </View>
        <View style={styles.inputpassw}>
          <FontAwesome name='lock' size={20} color="#505050"></FontAwesome>
          <TextInput style={styles.passTextInp} placeholder='Digite sua senha'></TextInput>
        </View>
        <TouchableOpacity style={styles.viewSubText}>
          <Text style={styles.subTextForm}>Esqueceu a senha?</Text>
        </TouchableOpacity>
      </View>
      <TouchableOpacity style={styles.logButton} onPress={handleLoginPress}>
        <Text style={styles.textButton}>Login</Text>
      </TouchableOpacity>
      <View style={{flexDirection: 'row', alignItems:'center', marginTop: '5%'}}>
        <Text>Não possui uma conta? 
          <Text style={styles.textRegisterinForm}> Registre-se clicando aqui</Text>
        </Text>
      </View>
      <View style={{marginTop: '5%'}}>
        <Text style={{color: '#a11a4d'}}>Confirme seu CPF: {textoInput}</Text>
      </View>
      {mostrarTexto && (
        <View style={{marginTop: '5%'}}>
          <Text style={{color: '#a11a4d'}}>Faça seu login!</Text>
        </View>
      )}
    </View>
  );
}
