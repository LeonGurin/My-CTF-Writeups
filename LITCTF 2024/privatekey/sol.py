from Crypto.Util.number import long_to_bytes
import owiener

n = 91222155440553152389498614260050699731763350575147080767270489977917091931170943138928885120658877746247611632809405330094823541534217244038578699660880006339704989092479659053257803665271330929925869501196563443668981397902668090043639708667461870466802555861441754587186218972034248949207279990970777750209
e = 89367874380527493290104721678355794851752244712307964470391711606074727267038562743027846335233189217972523295913276633530423913558009009304519822798850828058341163149186400703842247356763254163467344158854476953789177826969005741218604103441014310747381924897883873667049874536894418991242502458035490144319
c = 71713040895862900826227958162735654909383845445237320223905265447935484166586100020297922365470898490364132661022898730819952219842679884422062319998678974747389086806470313146322055888525887658138813737156642494577963249790227961555514310838370972597205191372072037773173143170516757649991406773514836843206
d = owiener.attack(e, n)

print(long_to_bytes(pow(c, d, n)))



