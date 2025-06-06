import { useForm, SubmitHandler } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import { ZodTypeAny } from 'zod'

type Field<T> = {
  name: keyof T
  label: string
  type?: string
}

interface AuthFormProps<T> {
  schema: ZodTypeAny
  onSubmit: SubmitHandler<T>
  fields: Field<T>[]
  buttonText: string
}

export function AuthForm<T extends Record<string, unknown>>({
  schema,
  onSubmit,
  fields,
  buttonText,
}: AuthFormProps<T>) {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<T>({
    resolver: zodResolver(schema),
  })

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
      {fields.map((field) => (
        <div key={String(field.name)}>
          <label className="block text-sm font-medium">{field.label}</label>
          <input
            type={field.type || 'text'}
            {...register(field.name as import('react-hook-form').Path<T>)}
            className="w-full border border-gray-300 rounded-md p-2 mt-1"
          />
          {errors[field.name as string] && (
            <p className="text-red-500 text-sm mt-1">
              {String((errors[field.name as string]?.message || ''))}
            </p>
          )}
        </div>
      ))}
      <button
        type="submit"
        className="w-full bg-indigo-600 text-white py-2 rounded-md hover:bg-indigo-700"
      >
        {buttonText}
      </button>
    </form>
  )
}
