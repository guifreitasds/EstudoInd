import { StyleSheet, Text, View } from 'react-native';
import {ProfileCard} from '../components/ProfileCard/ProfileCard'
import { CoroaImgText } from '../components/CoroaImgText/CoroaImgText';

export function ProfileScreen({route, navigation}) {

  return(
    <View style={styles.container}>
      <View style={styles.containerImgText}>
        <CoroaImgText/>
      </View>
      <ProfileCard/>
    </View>
  );


}

const styles = StyleSheet.create({
    container:{
      flex:1,
      backgroundColor: '#FFC9AB',
    },
    containerImgText:{
      alignItems: 'center'
    },
})