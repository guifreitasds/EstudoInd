import { StatusBar } from 'expo-status-bar';
import { useState } from 'react';
import { StyleSheet, Text, View, ScrollView, FlatList, TouchableOpacity } from 'react-native';

export default function App() {
  const [users, setUsers] = useState([
    {nome: 'One', key: 1},
    {nome: 'Two', key: 2},
    {nome: 'Three', key: 3},
    {nome: 'Four', key: 4},
    {nome: 'Five', key: 5},
    {nome: 'Six', key: 6},
    {nome: 'Seven', key: 7},
    {nome: 'Eight', key: 8},
    {nome: 'Nine', key: 9},
    {nome: 'Ten', key: 10},
    {nome: 'Eleven', key: 11},
    {nome: 'Twelve', key: 12},
    {nome: 'Thirteen', key: 13},
    {nome: 'Fourteen', key: 14},
    {nome: 'Fifteen', key: 15}
  ])

  const apertarBotao=(key)=>{
    setUsers(
      (pessoasAnteriores) => {
        return pessoasAnteriores.filter(users => users.key != key)
      }
    )
  }
  return (
    <FlatList
        style={styles.container}
        numColumns={3}
        keyExtractor={(item)=>{item.key}}
        data={users}
        renderItem={({item}) => (
          <TouchableOpacity
          onPress={()=>{apertarBotao(item.key)}}
          style={styles.touchContainer}
          >
            <Text style={styles.item}>{item.nome}</Text>
          </TouchableOpacity>
        )
      }
    />
  );
}

const styles = StyleSheet.create({
  container: {
    display: 'flex',
    verticalAlign: 'middle',
    flex: 1,
    backgroundColor: '#fff',
  },
  touchContainer:{
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  item: {
    display: 'flex',
    verticalAlign: 'middle',
    textAlign: 'center',
    color: 'white',
    padding: 15,
    backgroundColor: '#22bbff',
    width: 145,
    height: 165,
    margin: 15,
    fontSize: 24
  }
});
