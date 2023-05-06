import { StyleSheet, Text, View, Button } from 'react-native';

export function HomeScreen({ navigation }) {
  return(
    <View style={{flex:1,alignItems:'center',justifyContent:'center'}}>
      <Text style={{marginBottom:'7%'}}>HomeScreen</Text>
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