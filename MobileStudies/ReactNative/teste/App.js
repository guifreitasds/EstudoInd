import { Text, View, StyleSheet, Image, ScrollView, FlatList, Button } from 'react-native';
import React, { useState } from "react"
import { MaterialCommunityIcons } from '@expo/vector-icons';

export default function App() {

  const [data, setData] = useState([
    {
      id: '1',
      text: 'Monitoramento de Saúde em tempo real',
      icon: 'heart-pulse',
    },
    {
      id: '2',
      text: 'Comunicação direta com cuidadores e família',
      icon: 'account-multiple-outline',
    },
    {
      id: '3',
      text: 'Dicas de alimentação personalizadas',
      icon: 'food-apple-outline',
    },
    {
      id: '4',
      text: 'Prontuário Online',
      icon: 'clipboard-outline',
    },
  ]);

  const renderItem = ({ item }) => (
    <View style={styles.item}>
      <MaterialCommunityIcons name={item.icon} size={30} color="#911746" style={{textAlign:'center'}} />
      <Text style={styles.paragraph3}>{item.text}</Text>
    </View>
  );

  return (
    <ScrollView>
      <View style={styles.container}>
        <View style={styles.containerBox}>
          <Image style={styles.imgPrin} source={require('./assets/COROA-nofill.png')} />
          <View style={styles.textos}>
            <Text style={styles.paragraph}>
              C.O.R.O.A
            </Text>
            <Text style={styles.subparag}>O aplicativo que cuida de você!</Text>
          </View>
        </View>
        <Text style={styles.welcome}>Seja bem vindo ao COROA!</Text>
        <View style={styles.textos}>
          <Text style={styles.paragraph3}>
            Aqui você cuida da sua saúde atráves de diversas funcionalidades!
          </Text>
          <FlatList
            data={data}
            renderItem={renderItem}
            keyExtractor={item => item.id}
          />
        </View>
        <View style={styles.containerBox2}>
          <Image style={styles.imgPrin2} source={require('./assets/COROA-nofill.png')} />
          <View style={styles.textos}>
            <Text style={styles.paragraph2}>
              C.O.R.O.A
            </Text>
            <Text style={styles.subparag2}>O aplicativo que cuida de você!</Text>
          </View>
          <View style={styles.appButtonContainer}>
            <Button title="Faça seu login!!" />
          </View>
        </View>
        <Text style={styles.subparag}>Todos os direitos Reservados</Text>
      </View>
    </ScrollView>

  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#FFC9AB',
    alignItems: 'center',
  },
  appButtonContainer:{
    background: '#0099FF',
    border: 2,
    borderRadius: 3,
    color: '#FDFDFD',
    marginLeft: 50 
  },
  containerBox: {
    marginTop: '6%',
    marginRight:'11%',
    width: 200,
    height: 130,
    backgroundColor: '#FFC9AB',
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',
  },
  containerBox2: {
    marginTop: '6%',
    marginRight:'11%',
    width: 200,
    height: 130,
    backgroundColor: '#FFC9AB',
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center', 
  },
  containerList:{
    backgroundColor:'#911746',
    justifyContent:'flex-start',
  },
  textos:{
      flexDirection:'column',
  },
  
  paragraph: {
    fontSize: 37.5,
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
  paragraph2: {
    fontSize: 18.75,
    fontWeight: '500',
    fontFamily: 'serif',
    color: '#911746'
  },
  subparag2: {
    fontSize: 5.5,
    fontWeight: '400',
    fontFamily: 'serif',
    color: '#911746'
  },
  paragraph3: {
    fontSize: 25.5,
    marginTop: 20,
    marginBottom: 10,
    padding: 10,
    fontWeight: '500',
    fontFamily: 'serif',
    color: '#FFC9AB',
    backgroundColor: '#911746',
    borderRadius: 10,
    justifyContent: 'center',
    textAlign: 'center',
    width: 400,
    shadowColor: "#000",
  shadowOffset: {
	width: 0,
	height: 2,
},
  shadowOpacity: 0.35,
  elevation: 3,
  },

  imgPrin: {
    width: 125,
    height: 125
  },
  imgPrin2:{
    width: 62.5,
    height: 62.5
  },
  welcome:{
    fontSize: 25,
    fontWeight: '500',
    fontFamily: 'serif',
    color: '#911746',
    padding: 10
  }
});
