import { StyleSheet, Text, View } from 'react-native';


export function DetailsScreen({route, navigation}) {
  const {itemId, otherParam} = route.params;

  return(
    <View style={{flex:1, alignItems:'center', justifyContent:'center'}}>
      <Text>Details Screen {itemId}, {otherParam}</Text>
    </View>
  );
}